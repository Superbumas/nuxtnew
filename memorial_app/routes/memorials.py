from flask import request, jsonify
from werkzeug.utils import secure_filename
import os
from memorial_app import db
from memorial_app.models import MemorialProfile
from memorial_app.app import bp
from utils import secure_file_name 

@bp.route('/api/memorials', methods=['POST'])
def create_memorial():
    data = request.form
    files = request.files

    # Save profile photo
    profile_photo = files.get('profile_photo_url')
    if profile_photo:
        profile_photo_filename = secure_file_name(profile_photo.filename)
        profile_photo.save(os.path.join('uploads', profile_photo_filename))
    else:
        profile_photo_filename = None

    # Save cover photo
    cover_photo = files.get('cover_photo_url')
    if cover_photo:
        cover_photo_filename = secure_file_name(cover_photo.filename)
        cover_photo.save(os.path.join('uploads', cover_photo_filename))
    else:
        cover_photo_filename = None

    new_profile = MemorialProfile(
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        biography=data.get('biography'),
        profile_photo_url=profile_photo_filename,
        cover_photo_url=cover_photo_filename,
        date_of_birth=data.get('date_of_birth'),
        date_of_death=data.get('date_of_death'),
        country=data.get('country'),
        city=data.get('city'),
        timeline_events=data.get('timeline_events')
    )
    db.session.add(new_profile)
    db.session.commit()
    return jsonify(new_profile.to_dict()), 201
