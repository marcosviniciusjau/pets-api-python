from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.main.composer.person_create_composer import person_create_composer

person_route_bp = Blueprint("person_routes", __name__)

@person_route_bp.route("/people", methods=["POST"])
def create_person():
        http_request = HttpRequest(body=request.json)
        view = person_create_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
  