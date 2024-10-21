from flask import Blueprint, current_app

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")

@auth_blueprint.route("/logout", methods=["GET"])
def logout():
    current_app.logger.info("Logout successfully!")
    return {
        "message": "Logout successfully!"
    }
