from flask import Blueprint, jsonify

pets_routes_bp = Blueprint("pets_routes", __name__)

@pets_routes_bp.route("/pets", methods=["GET"])
def list_pets():
  return jsonify({"message": "List of pets"}), 200