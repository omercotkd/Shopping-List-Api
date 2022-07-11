from flask import Blueprint

registration_routes = Blueprint("registration_routes", __name__, url_prefix="/api/register")

@registration_routes.route("")
def register_new_user():
    pass