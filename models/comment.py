from init import db, ma
from marshmallow import fields

class Comment(db.Model):
    __tablename__ = "comments"

    comment_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    date = db.Column(db.Date) # Created date

    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.post_id"), nullable=False)

    user = db.relationship("User", back_populates="comments")
    post = db.relationship("Post", back_populates="comments")

class CommentSchema(ma.Schema):

    user = fields.Nested("UserSchema", only=["name", "email"])
    post = fields.Nested("PostSchema", exclude=["comments"])

    class Meta:
        fields = ("comment_id", "message", "date", "user", "post")

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)