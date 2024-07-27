from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.likes import Like, like_schema, likes_schema
from models.post import Post

# /posts/<int:post_id>/likes
likes_bp = Blueprint("likes", __name__, url_prefix="/<int:single_post_id>/likes")

# We already get the likes while fetching posts - so, no need for "get likes" route here

# Create like route
@likes_bp.route("/", methods=["POST"])
@jwt_required()
def like_post(single_post_id):
    # Get the user ID from the JWT token
    user_id = get_jwt_identity()
    # Check if the post exists
    stmt = db.select(Post).filter_by(post_id = single_post_id)
    post = db.session.scalar(stmt)

    if not post:
        return {"error": f"Post with id: {single_post_id} was not found"}, 404

    # Check if the user has already liked the post
    stmt = db.select(Like).filter_by(user_id=user_id, post_id=single_post_id)
    existing_like = db.session.scalar(stmt)
    if existing_like:
        return {"error": "You have already liked this post"}, 400

    # Create a new like
    like = Like(user_id=user_id, post_id=single_post_id)
    db.session.add(like)
    db.session.commit()

    return like_schema.dump(like), 201


# Delete Comment - /posts/post_id/likes/like_id
@likes_bp.route("/", methods=["DELETE"])
@jwt_required()
def unlike_post(single_post_id):
    # Get the user ID from the JWT token
    user_id = get_jwt_identity()

    # Check if the like exists
    stmt = db.select(Like).filter_by(user_id=user_id, post_id=single_post_id)
    like = db.session.scalar(stmt)
    if not like:
        return {"error": "Like not found"}, 404

    # Delete the like
    db.session.delete(like)
    db.session.commit()

    return {"message": "Like deleted successfully"}, 200
    
