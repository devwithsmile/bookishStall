# app/  auth/models.py


from datetime import datetime
from app import db, bcrypt
from app import login_manager
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20))
    user_email = db.Column(db.String(60), unique=True, index=True)
    user_password = db.Column(db.String(80))
    registration_date = db.Column(db.DateTime, default=datetime.now)

    @classmethod
    def create_user(cls, user_name, user_email, user_password):
        user = cls(user_name=user_name,
                   user_email=user_email,
                   user_password=bcrypt.generate_password_hash(user_password).decode('utf-8'))

        db.session.add(user)
        db.session.commit()

        return user
    
    def check_password(self,password):
        return bcrypt.check_password_hash(self.user_password,password)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
