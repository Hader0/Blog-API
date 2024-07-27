from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.comment import Comment, comment_schema, comments_schema
from models.post import Post

# /posts/<int:post_id>/comments
comments_bp = Blueprint("comments", __name__, url_prefix="/<int:single_post_id>/comments")

# We already get the comments while fetching posts - so, no need for "get comments" route here

# Create comment route
@comments_bp.route("/", methods=["POST"])
@jwt_required()
def create_comment(single_post_id):
    # Get the comment message from the request body
    body_data = request.get_json()
    # Fetch the post with that particular ID - post_id
    stmt = db.select(Post).filter_by(post_id = single_post_id)
    post = db.session.scalar(stmt)
    # If Post exists
    if post:
        # Create an intance of the Comment model
        comment = Comment(
            message = body_data.get("message"),
            date = date.today(),
            post = post,
            user_id = get_jwt_identity()
        )
        # Add and commit the session
        db.session.add(comment)
        db.session.commit()
        # Return the created commit
        return comment_schema.dump(comment), 201
    # Else
    else:
        # Return an error like the post does not exist
        return {"error": f"Post with id: {single_post_id} was not found"}, 404

# Delete Comment - /posts/post_id/comments/comment_id
@comments_bp.route("/<int:single_comment_id>", methods=["DELETE"])
@jwt_required()
def delete_comment(single_post_id, single_comment_id):
    # Fetch the comment from the database with that id - comment_id
    stmt = db.select(Comment).filter_by(comment_id = single_comment_id)
    comment = db.session.scalar(stmt)
    # If the comment exists
    if comment:
        # Delete the comment
        db.session.delete(comment)
        db.session.commit()
        # Return a message
        return {"message": f"Comment '{comment.message}' delete successfully"}
    # Else
    else:
        # Return an error saying comment does not exist
        return {"error": f"Comment with id: {single_comment_id} was not found"}, 404

# Update comment - /posts/post_id/comments/comment_id
@comments_bp.route("/<int:single_comment_id>", methods=["PUT", "PATCH"])
@jwt_required()
def edit_comment(single_post_id, single_comment_id):
    # Get the values from the body of the request
    body_data = request.get_json()
    # Find the comment in the database with the id - comment_id
    stmt = db.select(Comment).filter_by(comment_id = single_comment_id)
    comment = db.session.scalar(stmt)
    # If comment exists
    if comment:
        # Update the fields
        comment.message = body_data.get("message") or comment.message
        # Commit
        db.session.commit()
        # Return some response to the client
        return comment_schema.dump(comment)
    # Else
    else:
        # Return an error saying the comment does not exist
        return {"error": f"Comment with id: {single_comment_id} was not found"}, 404