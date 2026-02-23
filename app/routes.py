"""
Application routes
"""
from flask import render_template, request, jsonify, redirect, url_for, current_app
from datetime import datetime


def register_routes(app):
    """Register all application routes"""
    
    @app.route('/')
    def index():
        """Home page"""
        return render_template('pages/home.html', 
                             current_page='home',
                             year=datetime.now().year)
    
    @app.route('/about')
    def about():
        """About page"""
        return render_template('pages/about.html',
                             current_page='about',
                             year=datetime.now().year)
    
    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        """Contact page with form handling"""
        if request.method == 'POST':
            form_data = {
                'first_name': request.form.get('fname'),
                'last_name': request.form.get('lname'),
                'email': request.form.get('email'),
                'phone': request.form.get('phone'),
                'service': request.form.get('service'),
                'message': request.form.get('message')
            }
            
            # In production: send email, save to database
            return render_template('pages/contact.html',
                                 current_page='contact',
                                 year=datetime.now().year,
                                 form_submitted=True)
        
        return render_template('pages/contact.html',
                             current_page='contact',
                             year=datetime.now().year,
                             form_submitted=False)
    
    @app.route('/api/contact', methods=['POST'])
    def api_contact():
        """API endpoint for AJAX contact form"""
        try:
            data = request.get_json()
            
            required = ['fname', 'lname', 'email']
            for field in required:
                if not data.get(field):
                    return jsonify({'success': False, 'error': f'{field} required'}), 400
            
            # Process form (send email, save to DB, etc.)
            
            return jsonify({
                'success': True,
                'message': 'Thank you! We will respond within one business day.'
            })
        
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)}), 500
    
    @app.route('/health')
    def health():
        """Health check"""
        return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})
    
    @app.errorhandler(404)
    def not_found(error):
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return render_template('errors/500.html'), 500


# Auto-register routes when imported
from flask import current_app
if current_app:
    register_routes(current_app)
