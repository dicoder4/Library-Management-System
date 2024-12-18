from flask import Flask
from flask_cors import CORS
from routes.book_routes import book_bp
from routes.user_routes import user_bp

app = Flask(__name__)
CORS(app)

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/library_db"

# Register routes
app.register_blueprint(book_bp, url_prefix="/api/books")
app.register_blueprint(user_bp, url_prefix="/api/users")

if __name__ == "__main__":
    app.run(debug=True)
