from typing import Dict, Union

from flask import Blueprint, jsonify, abort
from flask_jwt_extended import create_access_token, jwt_required, current_user
from webargs import fields, validate
from webargs.flaskparser import use_args

from api import jwt
from api.data_providers import DataProvider
from api.models import User

bp = Blueprint("auth", __name__, url_prefix="/auth")

login_schema = {
    "username": fields.Str(required=True, validate=validate.Length(equal=8), location="form"),
    "password": fields.Str(required=True, location="form")
}


@jwt.user_identity_loader
def user_identity_lookup(user: User) -> str:
    return user.identikey


@jwt.user_loader_callback_loader
def user_loader_callback(identity: str) -> Union[User, None]:
    return User.query.get(identity)


@bp.route("/login", methods=["POST"])
@use_args(login_schema)
def login(args: Dict):
    user = User(identikey=args["username"])

    user_session = DataProvider.base_login(user.identikey, args["password"])

    if user_session is not None:
        user.session = user_session
    else:
        abort(401)

    user.save()

    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token), 200
