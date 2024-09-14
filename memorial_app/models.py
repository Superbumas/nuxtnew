from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin
import uuid
from datetime import datetime, date, time, timedelta
from extensions import db

db = SQLAlchemy()

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    google_id = db.Column(db.String(128))
    facebook_id = db.Column(db.String(128))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    profile_photo_url = db.Column(db.String(256))
    email_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    role = db.Column(db.String(64))
    subscription_status = db.Column(db.String(64))
    fs_uniquifier = db.Column(db.String(64), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

class MemorialProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    date_of_birth = db.Column(db.Date)
    date_of_death = db.Column(db.Date)
    biography = db.Column(db.Text)
    timeline_events = db.Column(db.JSON)  # Optional: Use a separate table if needed
    profile_photo_url = db.Column(db.String(256))
    qr_code_url = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    visibility_status = db.Column(db.String(64))

class TimelineEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('memorial_profile.id'), nullable=False)
    year = db.Column(db.Integer)
    event = db.Column(db.Text)

class Tribute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('memorial_profile.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    tribute_message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class PaymentSubscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    stripe_customer_id = db.Column(db.String(128))
    subscription_id = db.Column(db.String(128))
    payment_amount = db.Column(db.Float)
    payment_status = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    subscription_start = db.Column(db.DateTime)
    subscription_end = db.Column(db.DateTime)

class Media(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('memorial_profile.id'), nullable=False)
    media_type = db.Column(db.String(64))
    media_url = db.Column(db.String(256))
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

class QRCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('memorial_profile.id'), nullable=False)
    qr_code_url = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ActivityLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey('memorial_profile.id'), nullable=False)
    action = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)