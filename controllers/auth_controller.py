from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta

from init import bcrypt, db
from models.user import User, user_schema, UserSchema

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=["POST"])
def register_user():
    try:
        # get the data from the body of the request
        body_data = UserSchema().load(request.get_json())

        # create an instance of the User model
        user = User(
            name=body_data.get("name"),
            email=body_data.get("email")
        )
        # extract the password from the body
        password = body_data.get("password")

        # hash the password
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")

        # add and commit to the DB
        db.session.add(user)
        db.session.commit()

        # respond back
        return user_schema.dump(user), 201

    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            # Not null violation
            return {"error": f"The column {err.orig.diag.column_name} is required"}, 409
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            # Unique violation
            return {"error": "Email address already in use"}, 409

@auth_bp.route("/login", methods=["POST"])
def login_user():
    # Get the data from the body of the request
    body_data = request.get_json()
    # Find the user in the DB with the email address
    stmt = db.select(User).filter_by(email=body_data.get("email"))
    user = db.session.scalar(stmt)
    # If the user exists and password is correct
    if user and bcrypt.check_password_hash(user.password, body_data.get("password")):
        # Create JWT Token
        token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(days=1))
        # Respond back
        return {"email": user.email, "is_admin": user.is_admin, "token": token}

    # Else
    else:
        # Respond with an error message
        return {"error": "Invalid email or password"}, 401

# /auth/users/user_id
@auth_bp.route("/users", methods=["PUT", "PATCH"])
@jwt_required()
def update_user():
    # Get the fields from the body of the request
    body_data = UserSchema().load(request.get_json(), partial=True)
    password = body_data.get("password")
    # Fetch the user from the database
    stmt = db.select(User).filter_by(user_id=get_jwt_identity())
    user = db.session.scalar(stmt)
    # If the user exists
    if user:
        # Update the fields
        user.name = body_data.get("name") or user.name
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")
        # Commit to the database
        db.session.commit()
        # Return a response
        return user_schema.dump(user)
    # Else
        # Return an error
        return {"error": "User does not exist"}