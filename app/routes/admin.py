from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

bp = Blueprint('admin', __name__)

@bp.route('/admin/dashboard', methods=['GET'])
@jwt_required()
def admin_dashboard():
    return jsonify({"message": "Welcome to the Admin Dashboard!"}), 200


@bp.route('/protected-route', methods=['GET'])
@jwt_required()
def protected():
    return {"message": "You are viewing a protected route"}

