from flask import Flask
from config import Config
from extensions import db, migrate, login, cors, mail, security
from routes import auth, memorials, payments
from models import User, MemorialProfile, TimelineEvent, Tribute, PaymentSubscription, Media, QRCode, ActivityLog

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    cors.init_app(app)
    mail.init_app(app)
    security.init_app(app)

    app.register_blueprint(auth.bp)
    app.register_blueprint(memorials.bp)
    app.register_blueprint(payments.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)