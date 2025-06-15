from flask_smorest import Blueprint, abort
from app.api.schemas import UserSchema, GetUserSchema,UserUpdateSchema
from app.crud.user import create_user, get_users, soft_delete_user, get_user_by_id,update_user
from flask_jwt_extended import jwt_required
from app.core.security import admin_required
from flask.views import MethodView

blp = Blueprint("Users", __name__, url_prefix="/users", description="User Management")


@blp.route("/")
class UserList(MethodView):
    @blp.response(status_code=200, schema=GetUserSchema(many=True))
    @jwt_required()
    def get(self):
        return get_users()

    @blp.arguments(UserSchema)
    @blp.response(status_code=201, schema=GetUserSchema)
    def post(self, new_user_data):
        return create_user(new_user_data)


@blp.route("<string:user_id>")
class UserDetail(MethodView):
    @blp.response(status_code=200, schema=GetUserSchema)
    @jwt_required()
    def get(self, user_id):
        return get_user_by_id(user_id)

    @jwt_required()
    @blp.response(status_code=204)
    def delete(self, user_id):
        user = soft_delete_user(user_id)
        if not user:
            abort(404, description="User not found")
        return {"message": "Successful"}
    
    @jwt_required()
    @admin_required("admin")
    @blp.arguments(UserUpdateSchema)
    @blp.response(200,UserSchema)
    def patch(self,data,user_id):
        user = update_user(user_id,data)
        return user 
