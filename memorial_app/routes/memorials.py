from flask import Blueprint, request, jsonify
from models import MemorialProfile
from extensions import db

bp = Blueprint('memorials', __name__)

@bp.route('/api/memorials', methods=['POST'])
def create_memorial():
    data = request.get_json()
    new_profile = MemorialProfile(
        name=data['name'],
        birthdate=data['birthdate'],
        deathdate=data['deathdate'],
        biography=data['biography']
    )
    db.session.add(new_profile)
    db.session.commit()
    return jsonify(new_profile.to_dict()), 201

@bp.route('/api/memorials', methods=['GET'])
def get_memorials():
    profiles = MemorialProfile.query.all()
    return jsonify([profile.to_dict() for profile in profiles])

@bp.route('/api/memorials/<int:id>', methods=['DELETE'])
def delete_memorial(id):
    profile = MemorialProfile.query.get_or_404(id)
    db.session.delete(profile)
    db.session.commit()
    return '', 204