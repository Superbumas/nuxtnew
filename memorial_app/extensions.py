from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from flask_mail import Mail
from flask_security import Security

db = SQLAlchemy()
login = LoginManager()
cors = CORS()  # Initialize CORS
mail = Mail()
security = Security()