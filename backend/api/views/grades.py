from flask import Blueprint, jsonify
from flask import request
from flask_jwt_extended import jwt_required, current_user

from api import cache
from api.data_providers import CanvasDataProvider

bp = Blueprint("grades", __name__, url_prefix="/grades")

# key_prefix needs to be lambda to provide proper application context
@bp.route('/overview', methods=['GET'])
@jwt_required
@cache.cached(key_prefix=lambda: f"{current_user.identikey}:view/{request.path}", timeout=180)
def overview():
    return jsonify(CanvasDataProvider().get_overview(current_user.session)), 200
