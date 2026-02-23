"""
Flask application initialization
"""
from flask import Flask
from app.images_data import IMAGES


def create_app(config_name='default'):
    """Application factory"""
    app = Flask(__name__)
    
    # Load config
    app.config.from_object(f'config.{config_name}Config')
    
    # Register context processors
    @app.context_processor
    def inject_images():
        """Make images available to all templates"""
        def get_image(name):
            """Get image data by name"""
            return ''.join(IMAGES.get(name, ('',)))
        
        return {
            'get_image': get_image,
            'logo': ''.join(IMAGES.get('logo', ('',))),
        }
    
    # Register routes
    from app import routes
    
    return app
