from flask_smorest import Blueprint, abort
from app.api.schemas import LoginSchema
from app.core.security import authenticate
from flask.views import MethodView

blp = Blueprint("Auth", __name__, url_prefix="/auth", description="Authentication")


@blp.route("/login")
class Login(MethodView):
    @blp.arguments(LoginSchema)
    @blp.response(status_code=200)
    def post(self, data):
        token = authenticate(data["username"], data["password"])
        if not token:
            abort(401, message="Invalid credentials")
        return {"access_token": token}
