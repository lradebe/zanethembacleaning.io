"""
Application routes
"""
from flask import render_template, request, jsonify, redirect, url_for, current_app, flash
from datetime import datetime
from flask import current_app as app
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import Service, Testimonial, Inquiry, AdminUser


def register_routes(app):
    """Register all application routes"""
    
    @app.route('/')
    def index():
        # Fetch all services and approved testimonials from the database
        services = Service.query.all()
        testimonials = Testimonial.query.filter_by(is_approved=True).all()
    
        # We pass them to the template
        return render_template('pages/home.html', services=services, testimonials=testimonials, current_page='home', year=datetime.now().year)
    

    @app.route('/about')
    def about():
        """About page"""
        return render_template('pages/about.html',
                             current_page='about',
                             year=datetime.now().year)
    
    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        if request.method == 'POST':
            # Grab data from the HTML form
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            service = request.form.get('service')
            message = request.form.get('message')
        
        # Create a new inquiry object (set attributes individually to avoid constructor keyword-mismatch)
            new_inquiry = Inquiry()
            new_inquiry.name = name
            new_inquiry.email = email
            new_inquiry.phone = phone
            new_inquiry.service_requested = service
            new_inquiry.message = message
        
        # Save it to the database
            db.session.add(new_inquiry)
            db.session.commit()
        
        # Redirect back to contact with a success message (you'll need to set up flash messages in HTML later)
            flash("Thank you! Your message has been received.")
            return redirect(url_for('contact'))
        
        return render_template('pages/contact.html', current_page='contact')
    
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
        

    @app.route('/login', methods=['GET', 'POST'])
    def login():
    # If they are already logged in, send them straight to the dashboard
        if current_user.is_authenticated:
            return redirect(url_for('admin_dashboard'))
        
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
        
        # Look up the user in the database
            user = AdminUser.query.filter_by(username=username).first()
        
        # Check if user exists and password matches
            if user and user.check_password(password):
                login_user(user)
                return redirect(url_for('admin_dashboard'))
            
            flash('Invalid username or password')
        
        return render_template('pages/login.html')
    

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))
    


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
    
    @app.route('/admin')
    @login_required
    def admin_dashboard():
    # A simple route to view inquiries (We will add login protection later!)
        inquiries = Inquiry.query.order_by(Inquiry.timestamp.desc()).all()
        return render_template('pages/admin.html', inquiries=inquiries) # You will need to create this HTML file


# Auto-register routes when imported
from flask import current_app
if current_app:
    register_routes(current_app)

# The Inquiry model is defined in app.models (imported at the top of this file).
# Do not redefine the model here to avoid type conflicts with app.models.Inquiry.
