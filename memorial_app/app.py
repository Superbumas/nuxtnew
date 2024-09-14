import sys
import os
import logging
from logging.handlers import RotatingFileHandler

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask import Flask, request
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
    cors.init_app(app, resources={r"/api/*": {"origins": "http://127.0.0.1:3000"}})  # Configure CORS for API routes
    mail.init_app(app)

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)

    app.register_blueprint(auth.bp)
    app.register_blueprint(memorials.bp)
    app.register_blueprint(payments.bp)

    with app.app_context():
        db.create_all()  # Ensure the database tables are created

    # Set up logging
    if not app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/memorial_app.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Memorial App startup')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='127.0.0.1', port=5000)  # Ensure the host and port match your configuration