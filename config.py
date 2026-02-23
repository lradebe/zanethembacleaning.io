"""
Flask Application Configuration
"""
import os
from datetime import timedelta

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
class Config:
    # This creates a file called 'app.db' in your root folder
#    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-secret-key-change-this-later'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    """Base configuration"""
    # Secret key for sessions
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # App settings
    DEBUG = False
    TESTING = False
    
    # Session configuration
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Security headers
    SEND_FILE_MAX_AGE_DEFAULT = 31536000  # 1 year for static files
    
    # Email configuration (for contact form)
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or 'info@zanethembacleaning.co.za'


class defaultConfig(Config):
    DEBUG = True

class developmentConfig(Config):
    DEBUG = True


# class DevelopmentConfig(Config):
#     """Development configuration"""
#     DEBUG = True
#     SESSION_COOKIE_SECURE = False
#     TEMPLATES_AUTO_RELOAD = True


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    
    # Require HTTPS in production
    SESSION_COOKIE_SECURE = True
    
    # Additional security headers
    PREFERRED_URL_SCHEME = 'https'


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    WTF_CSRF_ENABLED = False


# Configuration dictionary
config = {
    'development': developmentConfig,
#    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': developmentConfig
#    'default': DevelopmentConfig
}





import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
    DEBUG = False
    TESTING = False

class developmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    # You can add other development‑specific settings here

class productionConfig(Config):
    """Production configuration."""
    DEBUG = False
    # Add production settings (e.g., database URIs, etc.)

class testingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DEBUG = True
