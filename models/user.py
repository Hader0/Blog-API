from init import db, ma

# Creating a table in the database
class User(db.Model):
    # Name of the table
    __tablename__ = "user"
    # Attributes of the table
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullabe=False)
    is_admin = db.Column(db.Boolean, default=False)

class UserSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "name", "email", "password", "is_admin")

# To handle a single user object
user_schema = UserSchema(exclude=["password"])

# To handle a list of user objects
users_schema = UserSchema(many=True, exclude=["password"])