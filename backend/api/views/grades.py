from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, current_user

from api.data_providers import CanvasDataProvider

bp = Blueprint("grades", __name__, url_prefix="/grades")


@bp.route('/overview', methods=['GET'])
@jwt_required
def overview():
    return jsonify(CanvasDataProvider().get_overview(current_user.session)), 200
