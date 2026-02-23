"""
Flask application initialization
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize the database globally, but don't attach it to the app yet
db = SQLAlchemy()
login_manager = LoginManager()
# Use setattr to avoid static type check errors when assigning the login_view
setattr(login_manager, 'login_view', 'login')

def create_app(config_name='default'):
    """Application factory"""
    app = Flask(__name__)
    
    # Load config
    app.config.from_object(f'config.{config_name}Config')
    db.init_app(app)
    login_manager.init_app(app)
    
    # Register routes
    from app import routes
    
    return app
