import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask import Flask
from config import Config
from extensions import db, migrate, login, cors, mail, security
from routes import auth, memorials, payments
from models import User, Role, MemorialProfile, TimelineEvent, Tribute, PaymentSubscription, Media, QRCode, ActivityLog
from flask_security import SQLAlchemyUserDatastore
from flask_cors import CORS  # Import Flask-CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})  # Configure CORS for API routes
    mail.init_app(app)

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)

    app.register_blueprint(auth.bp)
    app.register_blueprint(memorials.bp)
    app.register_blueprint(payments.bp)

    with app.app_context():
        db.create_all()  # Ensure the database tables are created

    # Enable CORS for all routes
    CORS(app, resources={r"/api/*": {"origins": "http://172.104.224.207:3000"}})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='127.0.0.1', port=5000)  # Ensure the host and port match your configuration