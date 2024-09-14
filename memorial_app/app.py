import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask import Flask
from config import Config
from extensions import db, migrate, login, cors, mail, security
from routes import auth, memorials, payments
from models import User, Role, MemorialProfile, TimelineEvent, Tribute, PaymentSubscription, Media, QRCode, ActivityLog
from flask_security import SQLAlchemyUserDatastore

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    cors.init_app(app)
    mail.init_app(app)

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)

    app.register_blueprint(auth.bp)
    app.register_blueprint(memorials.bp)
    app.register_blueprint(payments.bp)

    with app.app_context():
        db.create_all()  # Ensure the database tables are created

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)