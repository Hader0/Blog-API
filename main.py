from flask import Flask

from init import db, ma, bcrypt, jwt

def create_app():
    app = Flask(__name__)

    # Connect to Database Blog_db as user Blog_dev
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://blog_dev:123456@localhost:5432/blog_db"

    app.config["JWT_SECRET_KEY"] = "secret"

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    return app