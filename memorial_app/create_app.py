import os
from flask import Flask
from config import Config
from extensions import db
from models import User, Role, MemorialProfile, TimelineEvent, Tribute, PaymentSubscription, Media, QRCode, ActivityLog

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        print("Database tables created successfully.")

    return app

if __name__ == '__main__':
    app = create_app()