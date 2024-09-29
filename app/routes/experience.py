from flask import Blueprint, request, jsonify
from ..models.experience import Experience
from .. import db
from flask_jwt_extended import jwt_required
import logging

bp = Blueprint('experience', __name__, url_prefix='/experience')

# Get all experiences
@bp.route('/', methods=['GET'])
def get_experiences():
    experiences = Experience.query.all()
    return jsonify([experience.to_dict() for experience in experiences])

# Add a new experience
@bp.route('/', methods=['POST'])
def add_experience():
    data = request.json
    logging.info(f"Received data: {data}")

    # Validate input data
    required_fields = ['company_name', 'role', 'duration']
    for field in required_fields:
        if field not in data:
            logging.error(f"Missing required field: {field}")
            return jsonify({'message': f'Missing required field: {field}'}), 400

    # Create new experience
    try:
        new_experience = Experience(
            company_name=data['company_name'],  # Adjusted to match frontend
            role=data['role'],
            duration=data['duration'],
            description=data.get('description', '')  # Optional field
        )
        db.session.add(new_experience)
        db.session.commit()
        return jsonify(new_experience.to_dict()), 201
    except Exception as e:
        logging.error(f"Error adding experience: {e}")
        return jsonify({'message': 'Error adding experience'}), 500

# Update an experience
@bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_experience(id):
    data = request.json
    experience = Experience.query.get_or_404(id)
    
    # Update experience fields
    try:
        experience.company_name = data.get('company', experience.company_name)  # Optional update
        experience.role = data.get('role', experience.role)
        experience.duration = data.get('duration', experience.duration)
        experience.description = data.get('description', experience.description)
        
        db.session.commit()
        return jsonify(experience.to_dict())
    except Exception as e:
        logging.error(f"Error updating experience {id}: {e}")
        return jsonify({'message': 'Error updating experience'}), 500

# Delete an experience
@bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_experience(id):
    experience = Experience.query.get_or_404(id)
    try:
        db.session.delete(experience)
        db.session.commit()
        return jsonify({'message': 'Experience deleted successfully'}), 200
    except Exception as e:
        logging.error(f"Error deleting experience {id}: {e}")
        return jsonify({'message': 'Error deleting experience'}), 500
