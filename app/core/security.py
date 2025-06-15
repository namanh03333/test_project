from flask_jwt_extended import create_access_token, get_jwt, verify_jwt_in_request
from werkzeug.security import check_password_hash
from functools import wraps
from flask_smorest import abort
from app.database.models.user_model import User


def authenticate(username, password):
    user = User.query.filter_by(username=username, is_deleted=False).first()
    if user and check_password_hash(user.password, password):
        claims = {"role": user.role}
        return create_access_token(identity=user.id,additional_claims=claims)
    return None


def admin_required(required_role):
    def wrapper(fn):
        @wraps(fn)
        def decorated(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims.get("role") != required_role:
                abort(403, message="Admin role required.")
            return fn(*args, **kwargs)

        return decorated

    return wrapper
