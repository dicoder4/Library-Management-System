from flask import Blueprint, request, jsonify
from services.user_service import UserService

user_bp = Blueprint("user_bp", __name__)
user_service = UserService()

@user_bp.route("/", methods=["GET"])
def get_users():
    return jsonify(user_service.get_all_users()), 200
