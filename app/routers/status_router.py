from flask import Blueprint

status_bp = Blueprint('status', __name__)
@status_bp.route("/")
def health_check():
    return "OK", 200