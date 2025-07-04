from flask_smorest import abort
from app.database.models.user_model import User
from app.core.extensions import db
from werkzeug.security import generate_password_hash
import uuid


def create_user(data):
    user_id = data.get("id")
    if user_id:
        existing_user = User.query.filter_by(id=user_id).first()
        if existing_user:
            abort(400, message="User with this ID already exists.")
    else:
        user_id = str(uuid.uuid4())

    if User.query.filter_by(email=data.get("email")).first():
        abort(400, message="Email already exists.")

    if User.query.filter_by(username=data.get("username")).first():
        abort(400, message="Username already exists.")

    data["password"] = generate_password_hash(data["password"])
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return user


def get_users():
    return User.query.all()


def get_user_by_id(id):
    return User.query.filter_by(id=id, is_deleted=False).first()


def soft_delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        user.is_deleted = True
        db.session.delete(user)
        db.session.commit()
    return user


def update_user(user_id, data):
    user = User.query.filter_by(id=user_id).first_or_404()
    for k, v in data.items():
        setattr(user, k, v)
    db.session.commit()
    return user
