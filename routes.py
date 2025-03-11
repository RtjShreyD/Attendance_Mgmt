# routes.py
from flask import Blueprint, request, jsonify
from models import db, User

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@user_routes.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return jsonify([user.__dict__ for user in users if '_sa_instance_state' not in user.__dict__])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = User.query.get(user_id)
        if user:
            return jsonify({k: v for k, v in user.__dict__.items() if k != '_sa_instance_state'})
        return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': 'User not found'}), 404
        data = request.get_json()
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        return jsonify({'message': 'User updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@user_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': 'User not found'}), 404
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500