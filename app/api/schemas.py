from marshmallow import Schema, fields, validate, EXCLUDE


class LoginSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    username = fields.Str(required=True)
    password = fields.Str(required=True)


class UserSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    full_name = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.Email()
    phone = fields.String()
    avatar = fields.String()
    role = fields.String(
        validate=validate.OneOf(["admin", "user"]), load_default="user"
    )


class GetUserSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.String()
    full_name = fields.String()
    username = fields.String()
    email = fields.Email()
    phone = fields.String()
    avatar = fields.String()
    status = fields.String()


class UserUpdateSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    full_name = fields.String()
    username  = fields.String() 
    email = fields.Email()
    phone = fields.String()
    avatar = fields.String()
    status = fields.String()
