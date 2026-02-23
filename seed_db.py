from app import create_app, db
from app.models import Service

app = create_app()

def seed_services():
    services = [
        {"name": "Residential Cleaning", "description": "Thorough home cleaning services tailored to your needs.", "icon_or_number": "01"},
        {"name": "Commercial Cleaning", "description": "Professional office and retail space cleaning.", "icon_or_number": "02"},
        {"name": "Industrial Cleaning", "description": "Specialized cleaning for warehouses and factories.", "icon_or_number": "03"},
        {"name": "Deep Cleaning", "description": "Intensive cleaning for move-ins and renovations.", "icon_or_number": "04"},
        {"name": "Equipment Hire & Sales", "description": "Professional-grade cleaning equipment.", "icon_or_number": "05"},
        {"name": "Hygiene Solutions", "description": "Complete washroom and sanitization services.", "icon_or_number": "06"}
    ]

    with app.app_context():
        # Check if services already exist to prevent duplicates
        if Service.query.count() == 0:
            for s in services:
                new_service = Service()
                new_service.name = s['name']
                new_service.description = s['description']
                new_service.icon_or_number = s['icon_or_number']
                db.session.add(new_service)
            db.session.commit()
            print("Successfully added services to the database!")
        else:
            print("Services already exist in the database.")

if __name__ == '__main__':
    seed_services()