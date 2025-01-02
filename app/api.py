from flask import Flask, jsonify, request
from app.services.user_service import UserService
from app.services.post_service import PostService

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def get_users():
    """
    Endpoint to retrieve all users.
    """
    user_service = UserService(app)
    users = user_service.get_all_users()
    return jsonify([user.to_dict() for user in users])

@app.route("/users", methods=["POST"])
def create_user():
    """
    Endpoint to create a new user.
    """
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    email = data.get('email')
    
    user_service = UserService(app)
    user_service.create_user(name, age, email)
    return jsonify({"message": "User created successfully!"}), 201

@app.route("/posts", methods=["GET"])
def get_posts():
    """
    Endpoint to retrieve all posts.
    """
    post_service = PostService(app)
    posts = post_service.get_all_posts()
    return jsonify([post.to_dict() for post in posts])

@app.route("/posts", methods=["POST"])
def create_post():
    """
    Endpoint to create a new post.
    """
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    user_id = data.get('user_id')
    
    post_service = PostService(app)
    post_service.create_post(title, content, user_id)
    return jsonify({"message": "Post created successfully!"}), 201

if __name__ == "__main__":
    app.run(debug=True)
