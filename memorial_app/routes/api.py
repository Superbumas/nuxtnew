from flask import Blueprint, jsonify
from extensions import db  # Import db from extensions.py
from models import MemorialProfile

bp = Blueprint('api', __name__)

# Define your routes here
@bp.route('/example')
def example():
    return "This is an example endpoint"

@bp.route('/memorial_profiles', methods=['GET'])
def get_memorial_profiles():
    memorial_profiles = MemorialProfile.query.all()
    return jsonify(memorial_profiles)

