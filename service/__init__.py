from flask import Flask
from flask_talisman import Talisman

def create_app():
    app = Flask(__name__)

    # Security Headers
    talisman = Talisman(app)

    return app