from flask import Blueprint

login_routes = Blueprint("login_routes", __name__, url_prefix="/api/login")

@login_routes.route("", methods=["POST"])
def login_user():
    pass

