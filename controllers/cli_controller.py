from flask import Blueprint

from datetime import date

from init import db, bcrypt
from models.user import User
from models.post import Post
from models.comment import Comment

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables Created!")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables Dropped!")

@db_commands.cli.command("seed")
def seed_tables():
    # Create a list of User instances
    users = [
        User( # Admin User
            email="admin@email.com",
            password=bcrypt.generate_password_hash("123456").decode("utf-8"),
            is_admin=True
        ),
        User( # Normal User
            name="User 1",
            email="user1@email.com",
            password=bcrypt.generate_password_hash("123456").decode("utf-8")
        )
    ]

    db.session.add_all(users)

    posts = [
        Post(
            title = "Post 1",
            content = "Post 1 Content",
            date = date.today(),
            user = users[0] # The first user from the above User list is the one creating this post
        ),
        Post(
            title = "Post 2",
            content = "Post 2 Content",
            date = date.today(),
            user = users[0] # The first user from the above User list is the one creating this post
        ),
        Post(
            title = "Post 3",
            content = "Post 3 Content",
            date = date.today(),
            user = users[1] # The second user from the above User list is the one creating this post
        )
    ]

    db.session.add_all(posts)

    comments = [
        Comment(
            message="Comment 1",
            date=date.today(),
            user=users[1],
            post=posts[0]
        ),
        Comment(
            message="Comment 2",
            date=date.today(),
            user=users[0],
            post=posts[0]
        ),
        Comment(
            message="Comment 3",
            date=date.today(),
            user=users[0],
            post=posts[2]
        )
    ]

    db.session.add_all(comments)

    db.session.commit()

    print("Tables Seeded!")