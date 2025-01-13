from flask import Blueprint, Response
import time

name_bp = Blueprint("name", __name__)


@name_bp.route("/test/getName", methods=["GET"])
def get_name():
    time.sleep(2)
    response = Response(
        response='{"name": "John Doe"}', status=200, mimetype="application/json"
    )
    return response
