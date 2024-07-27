from init import db, ma
from marshmallow import fields

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

class PostSchema(ma.Schema):

    user = fields.Nested('UserSchema', only=["name"]) # Recieving only the name attribute from the user
    comments = fields.List(fields.Nested("CommentSchema", exclude=["post"]))

    class Meta:
        fields = ("post_id", "title", "content", "date", "user", "comments")
        ordered = True

post_schema = PostSchema()
posts_schema = PostSchema(many=True)