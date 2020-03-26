from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
mail = Mail(app)

from app.main import bp as main_bp
app.register_blueprint(main_bp)