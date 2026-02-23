"""
Flask application initialization
"""
from flask import Flask

def create_app(config_name='default'):
    """Application factory"""
    app = Flask(__name__)
    
    # Load config
    app.config.from_object(f'config.{config_name}Config')
    
    # Register routes
    from app import routes
    
    return app