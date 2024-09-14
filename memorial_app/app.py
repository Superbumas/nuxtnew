from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_dance.contrib.google import make_google_blueprint
from flask_dance.contrib.facebook import make_facebook_blueprint
from config import Config
from dotenv import load_dotenv
import os
from extensions import db, login  # Import db and login from extensions.py

load_dotenv()  # Load environment variables from .env file

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)  # Enable CORS

    db.init_app(app)
    migrate = Migrate(app, db)
    login.init_app(app)
    login.login_view = 'auth.login'

    # Social login blueprints
    google_bp = make_google_blueprint(client_id=os.getenv('GOOGLE_CLIENT_ID'), client_secret=os.getenv('GOOGLE_CLIENT_SECRET'))
    facebook_bp = make_facebook_blueprint(client_id=os.getenv('FACEBOOK_CLIENT_ID'), client_secret=os.getenv('FACEBOOK_CLIENT_SECRET'))
    app.register_blueprint(google_bp, url_prefix='/login')
    app.register_blueprint(facebook_bp, url_prefix='/login')

    with app.app_context():
        from routes import auth, api, payments
        app.register_blueprint(auth.bp)
        app.register_blueprint(api.bp)
        app.register_blueprint(payments.bp)

    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to the Flask API"})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)