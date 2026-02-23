"""
Zanethemba Cleaning Services - Flask Application
Main entry point
"""
from app import create_app
from app.routes import register_routes

# Create application instance
app = create_app('development')

# Register routes
register_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
