from typing import Dict, Union

from flask import Blueprint, jsonify, abort
from flask_jwt_extended import create_access_token, jwt_refresh_token_required, current_user, create_refresh_token, \
    jwt_required
from webargs import fields, validate
from webargs.flaskparser import use_args

from api import jwt
from api.models import User
from api.sessions import FedauthSession

bp = Blueprint("auth", __name__, url_prefix="/auth")

login_schema = {
    "username": fields.Str(required=True, validate=validate.Regexp(regex=r"^[a-z]{4}[0-9]{4}$"), location="form"),
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

    user_session = FedauthSession().login(args["username"], args["password"])

    if user_session is not None:
        user.session = user_session
    else:
        abort(401)

    user.save()

    ret = {
        'access_token': create_access_token(identity=user),
        'refresh_token': create_refresh_token(identity=user)
    }

    return jsonify(ret), 200


@bp.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    ret = {
        'access_token': create_access_token(identity=current_user)
    }
    return jsonify(ret), 200


@bp.route('/user', methods=['GET'])
@jwt_required
def user():
    ret = {
        "data": {
            'identikey': current_user.identikey
        }
    }

    return jsonify(ret), 200
