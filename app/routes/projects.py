from flask import Blueprint, request, jsonify
from ..models.project import Project
from .. import db
from flask_jwt_extended import jwt_required

bp = Blueprint('projects', __name__, url_prefix='/projects')

# Get all projects (open to anyone)
@bp.route('/', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([project.to_dict() for project in projects])

# Add a new project (protected route)
@bp.route('/', methods=['POST'])
@jwt_required()  # Only authenticated users can add projects
def add_project():
    data = request.json
    new_project = Project(
        title=data['title'],
        description=data['description'],
        technologies=data['technologies']
    )
    db.session.add(new_project)
    db.session.commit()
    return jsonify(new_project.to_dict()), 201

# Delete a project (protected route)
@bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()  # Only authenticated users can delete projects
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'Project deleted successfully'}), 200
