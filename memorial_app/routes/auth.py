from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from models import User
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('auth', __name__)

@bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "User already exists"}), 400

    user = User(
        email=data['email'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        password_hash=generate_password_hash(data['password'])
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Registration successful"}), 201

@bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password_hash, data['password']):
        login_user(user)
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid email or password"}), 401

@bp.route('/api/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successful"}), 200

@bp.route('/api/user', methods=['GET'])
@login_required
def get_user():
    user = {
        "email": current_user.email,
        "first_name": current_user.first_name,
        "last_name": current_user.last_name
    }
    return jsonify(user), 200