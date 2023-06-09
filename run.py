from app import create_app, db
from app.auth.models import User

flask_app = create_app('prod')

with flask_app.app_context():
    db.create_all()
    if not User.query.filter_by(user_name="Harry").first():
        User.create_user("Harry", "harry@potter.com", "passwordofharry")

flask_app.run()
