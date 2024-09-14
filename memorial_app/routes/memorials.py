from flask import Blueprint, request, jsonify
from models import MemorialProfile
from extensions import db
from flask_login import login_required, current_user

bp = Blueprint('memorials', __name__)

@bp.route('/api/memorials', methods=['GET'])
def get_memorials():
    memorials = MemorialProfile.query.filter_by(is_public=True).all()
    return jsonify([memorial.to_dict() for memorial in memorials])

@bp.route('/api/memorials', methods=['POST'])
@login_required
def create_memorial():
       data = request.get_json()
       memorial = MemorialProfile(
           user_id=current_user.id,
           first_name=data['first_name'],
           last_name=data['last_name'],
           date_of_birth=data['date_of_birth'],
           date_of_death=data['date_of_death'],
           biography=data['biography'],
           timeline_events=data['timeline_events'],
           tributes=data['tributes'],
           is_public=data['is_public']
    )
    db.session.add(memorial)
    db.session.commit()
    return jsonify({'message': 'Memorial created successfully'})

@bp.route('/api/memorials/<int:id>', methods=['PUT'])
   @login_required
   def update_memorial(id):
       memorial = MemorialProfile.query.get_or_404(id)
       if memorial.user_id != current_user.id:
           return jsonify({'message': 'Unauthorized'}), 403
       data = request.get_json()
       memorial.first_name = data['first_name']
       memorial.last_name = data['last_name']
       memorial.date_of_birth = data['date_of_birth']
       memorial.date_of_death = data['date_of_death']
       memorial.biography = data['biography']
       memorial.timeline_events = data['timeline_events']
       memorial.tributes = data['tributes']
       memorial.is_public = data['is_public']
       db.session.commit()
       return jsonify({'message': 'Memorial updated successfully'})

   @bp.route('/api/memorials/<int:id>', methods=['DELETE'])
   @login_required
   def delete_memorial(id):
       memorial = MemorialProfile.query.get_or_404(id)
       if memorial.user_id != current_user.id:
           return jsonify({'message': 'Unauthorized'}), 403
       db.session.delete(memorial)
       db.session.commit()
       return jsonify({'message': 'Memorial deleted successfully'})