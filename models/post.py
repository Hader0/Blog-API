from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class Post(db.Model):
    __tablename__ = "posts"

    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    date = db.Column(db.Date) # Created Date

    # Foreign Key
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    # Get the Foreign Key User's information
    user = db.relationship('User', back_populates="posts")
    comments = db.relationship('Comment', back_populates="post", cascade="all, delete")
    likes = db.relationship('Like', back_populates="post", cascade="all, delete")

class PostSchema(ma.Schema):

    user = fields.Nested('UserSchema', only=["name"]) # Recieving only the name attribute from the user
    comments = fields.List(fields.Nested("CommentSchema", exclude=["post"]))
    likes = fields.List(fields.Nested("LikeSchema"))

    title = fields.String(required=True, validate=And(
        Length(min=2, error="Title must be at least 2 characters long"),
        Regexp('^[A-Za-z0-9 ]+$', error="Title must only include alphanumeric characters")
    ))

    class Meta:
        fields = ("post_id", "title", "content", "date", "user", "comments", "likes")
        ordered = True

post_schema = PostSchema()
posts_schema = PostSchema(many=True)
