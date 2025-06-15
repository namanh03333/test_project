from app.core.extensions import db
from datetime import datetime
import uuid


def generate_uuid():
    return str(uuid.uuid4())


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.String, primary_key=True, default=generate_uuid())
    full_name = db.Column(db.String(100))
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(20))
    avatar = db.Column(db.String(1000))
    status = db.Column(db.String(20))
    is_deleted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    role = db.Column(db.String(20),default="user")

    def __repr__(self):
        return f"<User(id='{self.id}', username='{self.username}', email='{self.email}', status='{self.status}')>"
