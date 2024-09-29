from flask import Blueprint, request, jsonify
from ..models.skills import Skill
from .. import db
from flask_jwt_extended import jwt_required

bp = Blueprint('skills', __name__, url_prefix='/skills')

# Get all skills (open to anyone)
@bp.route('/', methods=['GET'])
def get_skills():
    skills = Skill.query.all()
    return jsonify([skill.to_dict() for skill in skills])

# Add a new skill (protected route)
@bp.route('/', methods=['POST'])
@jwt_required()  # Only authenticated users can add skills
def add_skill():
    data = request.json
    new_skill = Skill(
        name=data['name'],
        level=data['level']  # Example: Beginner, Intermediate, Expert
    )
    db.session.add(new_skill)
    db.session.commit()
    return jsonify(new_skill.to_dict()), 201

# Delete a skill (protected route)
@bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()  # Only authenticated users can delete skills
def delete_skill(id):
    skill = Skill.query.get_or_404(id)
    db.session.delete(skill)
    db.session.commit()
    return jsonify({'message': 'Skill deleted successfully'}), 200
