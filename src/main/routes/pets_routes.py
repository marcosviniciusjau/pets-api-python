from flask import Blueprint, jsonify
from src.errors.error_handler import handle_errors
from src.main.composer.pet_delete_composer import pet_delete_composer
from src.views.http_types.http_request import HttpRequest
from src.main.composer.pet_list_composer import pet_list_composer

pets_routes_bp = Blueprint("pets_routes", __name__)

@pets_routes_bp.route("/pets", methods=["GET"])
def list_pets():
    try:
        http_request = HttpRequest()
        view = pet_list_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@pets_routes_bp.route("/pets/<name>", methods=["DELETE"])
def delete_pet(name):
    try: 
        http_request = HttpRequest(param={"name": name})
        view = pet_delete_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response =handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code