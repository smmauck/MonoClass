from flask import Blueprint, jsonify
from flask import request
from flask_jwt_extended import jwt_required, current_user

from api import cache
from api.data_providers import CanvasDataProvider, MoodleDataProvider

bp = Blueprint("grades", __name__, url_prefix="/grades")


# key_prefix needs to be lambda to provide proper application context
@bp.route('/overview', methods=['GET'])
@jwt_required
@cache.cached(key_prefix=lambda: f"{current_user.identikey}:view/{request.path}", timeout=180)
def overview():
    user_session = current_user.session
    return jsonify(
        CanvasDataProvider().get_overview(user_session) + MoodleDataProvider().get_overview(user_session)), 200


@bp.route('/<string:course_type>/<int:course_id>', methods=['GET'])
@jwt_required
@cache.cached(key_prefix=lambda: f"{current_user.identikey}:view/{request.path}", timeout=180)
def assignments(course_type: str, course_id: int):
    if course_type == "canvas":
        return jsonify(CanvasDataProvider().get_grade_data(current_user.session, course_id)), 200
    elif course_type == "moodle":
        return jsonify(MoodleDataProvider().get_grade_data(current_user.session, course_id)), 200
