from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from models import User
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import url_for, jsonify, request, Blueprint
from utils import secure_file_name 
from flask_wtf.csrf import generate_csrf, validate_csrf

bp = Blueprint('auth', __name__)

@bp.route('/api/csrf-token', methods=['GET'])
def get_csrf_token():
    token = generate_csrf()
    return jsonify({'csrf_token': token})

@bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()

    # Check if data is None or missing required fields
    if not data or not all(key in data for key in ('email', 'username', 'password', 'confirm_password', 'csrf_token')):
        return jsonify({"error": "Missing fields"}), 400

    # Validate CSRF token
    csrf_token = data.get('csrf_token')
    try:
        validate_csrf(csrf_token)  # Validate the CSRF token
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    # Check if passwords match
    if data['password'] != data['confirm_password']:
        return jsonify({"error": "Passwords do not match"}), 400

    # Check if user already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "User already exists"}), 400

    user = User(
        email=data['email'],
        username=data['username'],
        password_hash=generate_password_hash(data['password'])
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Registration successful", "redirect": url_for('auth.login')}), 201

@bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    print("Received data:", data)  # Log the received data

    # Validate CSRF token
    csrf_token = data.get('csrf_token')
    if not csrf_token:
        return jsonify({'error': 'CSRF token is missing.'}), 400

    try:
        validate_csrf(csrf_token)  # Validate the CSRF token
    except Exception as e:
        return jsonify({'error': str(e)}), 400

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

