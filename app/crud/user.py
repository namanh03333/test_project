from flask import abort
from app.database.models.user_model import User
from app.core.extensions import db
from werkzeug.security import generate_password_hash


def create_user(data):
    user_id = data.get("id")
    if user_id and User.query.filter_by(id=user_id).first():
        abort(400, description="User with this ID already exists.")

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
        db.session.commit()
    return user


def update_user(user_id, data):
    user = User.query.filter_by(id = user_id).first_or_404()
    for k, v in data.items():
        setattr(user, k, v)
    db.session.commit()
    return user
