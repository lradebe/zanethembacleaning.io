# Zanethemba Cleaning Services - Flask Application

Complete Flask web application with identical functionality to the static HTML version.

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python app.py
```

### 3. Access the Site
```
http://localhost:5000
```

## 📁 Project Structure

```
zanethemba_flask/
├── app/
│   ├── __init__.py           # App initialization
│   ├── routes.py             # URL routes
│   ├── images_data.py        # Base64 images
│   ├── static/
│   │   ├── css/
│   │   │   ├── main.css
│   │   │   ├── components.css
│   │   │   ├── pages.css
│   │   │   └── responsive.css
│   │   └── js/
│   │       └── main.js       # JavaScript functionality
│   └── templates/
│       ├── base.html         # Base template
│       ├── components/
│       │   ├── splash.html
│       │   ├── navigation.html
│       │   └── footer.html
│       ├── pages/
│       │   ├── home.html
│       │   ├── about.html
│       │   └── contact.html
│       └── errors/
│           ├── 404.html
│           └── 500.html
├── config.py                 # Configuration
├── app.py                    # Main entry point
├── requirements.txt          # Dependencies
└── README.md                 # This file
```

## ✨ Features

- ✅ Splash screen animation
- ✅ Responsive navigation with hamburger menu
- ✅ Three rotating carousels (hero, break, community)
- ✅ Contact form with validation
- ✅ About page with company story
- ✅ Mobile-responsive design
- ✅ B-BBEE Level 1 badges
- ✅ Trust bar with credentials
- ✅ Services grid (6 services)
- ✅ Statistics section
- ✅ Footer with contact info

## 🔧 Configuration

### Environment Variables

Create a `.env` file:

```bash
SECRET_KEY=your-secret-key-here
FLASK_ENV=development
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-email-password
```

### Production Configuration

For production, set:

```python
app = create_app('production')
```

## 📊 Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page with hero carousel |
| `/about` | GET | About page with company story |
| `/contact` | GET/POST | Contact page with form |
| `/api/contact` | POST | AJAX contact form endpoint |
| `/health` | GET | Health check endpoint |

## 🎨 Customization

### Adding Images

Edit `app/images_data.py`:

```python
IMAGES = {
    'logo': 'base64-string-here',
    'img_0': 'base64-string-here',
    # Add more images...
}
```

### Carousel Configuration

Edit `app/static/js/main.js`:

```javascript
// Hero carousel - 5 second intervals
createCarousel('heroCarousel', 5000, 'heroDots');

// Break carousel - 7 second intervals
createCarousel('breakCarousel', 7000, null);

// Community carousel - 6 second intervals
createCarousel('communityCarousel', 6000, null);
```

## 🚀 Deployment

### Option 1: Gunicorn (Production)

```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Option 2: Docker

Create `Dockerfile`:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

Build and run:

```bash
docker build -t zanethemba-flask .
docker run -p 5000:5000 zanethemba-flask
```

### Option 3: Platform as a Service

**Heroku:**
```bash
heroku create zanethemba-cleaning
git push heroku main
```

**Render / Railway / Fly.io:**
- Connect GitHub repository
- Set build command: `pip install -r requirements.txt`
- Set start command: `gunicorn app:app`

## 📧 Contact Form Integration

### Email Configuration

To enable email sending, install Flask-Mail:

```bash
pip install Flask-Mail
```

Then configure in `config.py` and update `routes.py`:

```python
from flask_mail import Mail, Message

mail = Mail(app)

@app.route('/api/contact', methods=['POST'])
def api_contact():
    # ... validation ...
    
    msg = Message(
        'New Contact Form Submission',
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=['info@zanethembacleaning.co.za']
    )
    msg.body = f"""
    Name: {data['fname']} {data['lname']}
    Email: {data['email']}
    Phone: {data['phone']}
    Service: {data['service']}
    Message: {data['message']}
    """
    mail.send(msg)
    
    return jsonify({'success': True})
```

## 🐛 Troubleshooting

### Images Not Loading

If images don't load, verify:
1. `app/images_data.py` exists
2. Base64 strings are complete
3. No syntax errors in image dict

### Carousel Not Working

Check:
1. JavaScript console for errors
2. Carousel IDs match in HTML and JS
3. `main.js` is loaded

### Form Not Submitting

Verify:
1. Flask route is registered
2. Form action URL is correct
3. CSRF protection (if enabled)

## 🔒 Security

Production checklist:
- ✅ Set strong `SECRET_KEY`
- ✅ Enable HTTPS
- ✅ Add rate limiting
- ✅ Validate all form inputs
- ✅ Use environment variables
- ✅ Enable CSRF protection
- ✅ Set security headers

## 📦 Dependencies

- Flask 3.0.0 - Web framework
- Gunicorn 21.2.0 - Production server
- Flask-Mail 0.9.1 - Email support (optional)
- python-dotenv 1.0.0 - Environment variables

## 🤝 Support

For issues or questions:
- Check logs: Flask outputs to console
- Review `config.py` for settings
- Verify all templates exist
- Check static file paths

## 📄 License

© 2026 Zanethemba Cleaning Services (Pty) Ltd

---

**Zanethemba Cleaning Services**  
*"Bringing Hope Through Cleanliness"*
