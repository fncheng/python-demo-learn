from flask import Blueprint, make_response, jsonify
import time

number_bp = Blueprint("number", __name__)


@number_bp.route("/test/getNumber", methods=["GET"])
def get_number():
    time.sleep(0.2)
    response = make_response(jsonify({"number": 999}), 200)
    response.headers.set("X-Custom-Header", "Test")
    return response
