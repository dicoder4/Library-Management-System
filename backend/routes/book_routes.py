from flask import Blueprint, request, jsonify
from services.book_service import BookService

book_bp = Blueprint("book_bp", __name__)
book_service = BookService()

@book_bp.route("/", methods=["GET"])
def get_books():
    return jsonify(book_service.get_all_books()), 200

@book_bp.route("/", methods=["POST"])
def add_book():
    data = request.json
    book_service.add_book(data)
    return jsonify({"message": "Book added successfully"}), 201
