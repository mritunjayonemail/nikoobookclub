from flask import request, Blueprint, jsonify, current_app, render_template
from server.error import ValidationException, InternalServerError
from common.constants import HOME_PAGE
from os import path

from common.util import get_logger

book_club_bp = Blueprint('book_club_bp', __name__)

head_path = path.join(path.dirname(__file__))

@book_club_bp.errorhandler(ValidationException)
@book_club_bp.errorhandler(InternalServerError)
def handle_validation_exception(ex):
    response = jsonify(ex.to_dict())
    get_logger().error(response)
    response.status_code = ex.status_code
    return response

@book_club_bp.route('/health/full', methods=['GET',])
def health():
    return "Health is OK"

@book_club_bp.route('/home', methods=['GET',])
def home():
    return render_template(HOME_PAGE)