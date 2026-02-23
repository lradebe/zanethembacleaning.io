from app import create_app, db
from app.models import AdminUser

app = create_app()

with app.app_context():
    # Check if an admin already exists
    if not AdminUser.query.filter_by(username='admin').first():
        admin = AdminUser(username='admin')
        # Setting the default password. You can change this later!
        admin.set_password('zanethemba2026') 
        db.session.add(admin)
        db.session.commit()
        print("Admin user created successfully!")
        print("Username: admin")
        print("Password: zanethemba2026")
    else:
        print("Admin user already exists.")