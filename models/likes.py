from init import db, ma
from marshmallow import fields

class Like(db.Model):
    __tablename__ = "likes"

    like_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.post_id"), nullable=False)

    user = db.relationship("User", back_populates="likes")
    post = db.relationship("Post", back_populates="likes")

class LikeSchema(ma.Schema):

    user = fields.Nested("UserSchema", only=["name", "email"])
    post = fields.Nested("PostSchema", only=["title"])

    class Meta:
        fields = ("like_id", "user", "post")

like_schema = LikeSchema()
likes_schema = LikeSchema(many=True)



