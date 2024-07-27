from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.post import Post, post_schema, posts_schema
from controllers.comment_controller import comments_bp

posts_bp = Blueprint('posts', __name__, url_prefix="/posts")
posts_bp.register_blueprint(comments_bp)

# /posts - GET/fetch all posts
# /post/<id> - GET/fetch a single post
# /posts - POST/Create a new post
# /posts/<id> - DELETE a post
# /posts/<id> - PUT, PATCH/edit a post

# /posts - GET/fetch all posts
@posts_bp.route("/") # / = /posts
def get_all_posts():
    # Fetch all posts then order then by date in descending order
    stmt = db.select(Post).order_by(Post.date.desc())
    posts = db.session.scalars(stmt)
    return posts_schema.dump(posts)

# /post/<id> - GET/fetch a single post
@posts_bp.route("/<int:single_post_id>")
def get_one_post(single_post_id):
    stmt = db.select(Post).filter_by(post_id=single_post_id)
    post = db.session.scalar(stmt)
    if post:
        return post_schema.dump(post)
    else:
        return {"error": f"Post with ID: {single_post_id} was not found"}, 404

# /posts - POST/Create a new post
@posts_bp.route("/", methods=["POST"])
@jwt_required() # Token is required by logging in via a created user and using the JWT Token
def create_post():
    # Get the data from the body of the request
    body_data = request.get_json()
    # Create a new Post Model instance
    post = Post(
        title = body_data.get("title"),
        content = body_data.get("content"),
        date = date.today(),
        user_id = get_jwt_identity()
    )
    # Add and commit to DB
    db.session.add(post)
    db.session.commit()
    # Respond
    return post_schema.dump(post)

# /posts/<id> - DELETE a post
@posts_bp.route("/<int:single_post_id>", methods=["DELETE"])
@jwt_required() # Token is required by logging in via a created user and using the JWT Token
def delete_post(single_post_id):
    # Fetch the post from the DataBase
    stmt = db.select(Post).filter_by(post_id = single_post_id)
    post = db.session.scalar(stmt)
    # If Post
    if post:
        # Delete a post
        db.session.delete(post)
        db.session.commit()
        return{"message": f"Post '{post.title}' deleted successfully"}
    # Else
    else:
        # Return an error
        return {"error": f"Post with ID: {single_post_id} was not found"}, 404
    
# /posts/<id> - PUT, PATCH/edit a post
@posts_bp.route("/<single_post_id>", methods=["PUT", "PATCH"])
def update_post(single_post_id):
    # Get the data from the body of the request
    body_data = request.get_json()
    # Get the post from the database
    stmt = db.select(Post).filter_by(post_id = single_post_id)
    post = db.session.scalar(stmt)
    # If Post
    if post:
        # Update the fields as required
        post.title = body_data.get("title") or post.title
        post.content = body_data.get("content") or post.content
        # Commit to the DataBase
        db.session.commit()
        # Return a response
        return post_schema.dump(post)
    # Else
    else:
        # Return an error
        return {"error": f"Post with ID: {single_post_id} was not found"}, 404