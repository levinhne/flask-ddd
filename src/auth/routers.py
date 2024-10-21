from flask import Blueprint, request

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")

@auth_blueprint.route("/logout", methods=["GET"])
def logout():
    return {
        "message": "Logout successfully!"
    }
