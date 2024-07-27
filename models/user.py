from init import db, ma
from marshmallow import fields

# Creating a table in the database
class User(db.Model):
    # Name of the table
    __tablename__ = "users"
    # Attributes of the table
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # Foreign Key relationship for the Post Table
    posts = db.relationship('Post', back_populates="user")
    comments = db.relationship('Comment', back_populates="user")


class UserSchema(ma.Schema):
    posts = fields.List(fields.Nested('PostSchema'), exclude=["user"]) # Retreive all information from the post except for the user attribute as we will already have it
    comments = fields.List(fields.Nested('CommentSchema'), exclude=["user"])# Retreive all information from the comment except for the user attribute as we will already have it

    class Meta:
        fields = ("user_id", "name", "email", "password", "is_admin", "posts", "comments")

# To handle a single user object
user_schema = UserSchema(exclude=["password"])

# To handle a list of user objects
users_schema = UserSchema(many=True, exclude=["password"])