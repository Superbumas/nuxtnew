from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
from flask_mail import Mail
from flask_security import Security
from flask_wtf import CSRFProtect


db = SQLAlchemy()
login = LoginManager()
cors = CORS()
mail = Mail()
security = Security()
migrate = Migrate()
csrf = CSRFProtect()




