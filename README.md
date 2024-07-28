# Blog-API

## Documentation

GitHub Repo: https://github.com/Hader0/Blog-API

---

### Setup

#### To run from local machine:

**Create a postgresql database:**
``CREATE DATABASE blog_db;``
**Create a new postgresql user and give permissions from within Postgre interface:**
``CREATE ROLE blog_dev && GRANT ALL ON blog_db TO blog_dev;``
**Edit ".env" file so "SQL_DATABASE_URI" matches user and database details:**
``DATABASE_URI="postgresql+psycopg2://blog_dev:123456@localhost:5000/blog_db"``
``JWT_SECRET_KEY="secret"``
**Start & activate virtual environment:**
``python3 -m venv venv && source .venv/bin/activate``
**Install requirements:**
``pip3 install -r requirements.txt``
**Create/seed tables:**
``python3 -m flask db drop && python3 -m flask db create && python3 -m flask db seed``
**Run flask app:**
``python3 -m flask run``

---

### 1. Explain the problem that this app will solve, and explain how this app solves or addresses the problem

The Blog API was created as an easy way to store data related to a social media platform/app that involves users, posts, comments and likes. By using this Blog API, it provides security for users by using Authentication and Authorisation, as well as Data Validation:

**Authentication and Authorization:** The API employs JWT tokens for secure user authentication and utilizes role-based access control to ensure that only authorized users can perform specific actions.
**Data Validation:** Input validation guarantees that only valid data is processed, minimizing the risk of errors and security vulnerabilities.

Not only does it give the user peace of mind that their data is protected, but the Blog API is efficient in the management of the content and can rely on the scalability and performance:

**Efficient Content Management:** The API offers clear and concise endpoints for managing blog posts, comments, and likes, allowing content to be easily created, updated, and deleted.

**Scalability and Performance:** The implementation of a relational database combined with optimized queries ensures the system can scale and maintain efficiency as the number of users and interactions grows.

---

### 2. Describe the way tasks are allocated and tracked in your project.

During my project, my planning was first initiated by creating an ERD Diagram which built the foundation of what tables are needed and the relatiosnhips between them. Using the ERD Diagram and having Simon's Trello API lessons as reference, since my project is quite similar in a technical aspect - I follow the directions in the lessons and made sure the rubric's were satisfied. 

Since the major difference between Simon's Trello API and my Blog API is only an additional table, I refollowed the previous lessons and adjusted code accordingly to make sure all bases were covered. This includes all error handling, validation, etc. 

As my brain works in mysterious ways, I preferred tracking what is needed to be done by using my ERD Diagram of what table is completed, what relationship does the table have, how would that table interact with other tables, ect. I personally felt, for this assignment and with little time over the past month due to workplace obligations, that it worked quite well for me, especially since I had the Trello Lessons available, which I was surprised to see how similar my API was.

---

### 3. List and explain the third-party services, packages and dependencies used in this app.

**psycopg2-binary:**

psycopg2-binary is a PostgreSQL database adapter for Python, facilitating the connection and execution of SQL commands in PostgreSQL databases. It provides a DB-API 2.0 compliant interface and supports advanced PostgreSQL features.

**flask_sqlalchemy:**

flask_sqlalchemy is an extension for Flask that adds SQLAlchemy ORM support, enabling easy database interactions using Python objects. It integrates seamlessly with Flask, supporting the application context and request lifecycle.

**flask_marshmallow:**

flask_marshmallow integrates the Marshmallow library with Flask for easy serialization and deserialization of data. It simplifies data validation and transformation, making it easier to work with complex data types.

**arshmallow_sqlalchemy:**

marshmallow_sqlalchemy provides an integration between SQLAlchemy and Marshmallow, allowing automatic schema generation from SQLAlchemy models. It supports nested schema relationships and custom field definitions.

**flask_bcrypt:**

flask_bcrypt is an extension for Flask that provides bcrypt hashing utilities for secure password storage. It offers a simple API for generating and verifying bcrypt hashes, enhancing user authentication security.

**flask_jwt_extended:**

flask_jwt_extended is a Flask extension that implements JSON Web Tokens (JWT) for user authentication, allowing secure, stateless authentication. It supports token creation, refreshing, and route protection with customizable token behavior.

**python-dotenv:**

python-dotenv reads key-value pairs from a .env file and sets them as environment variables, managing configuration settings and secrets. It helps keep sensitive information out of the codebase by loading environment-specific variables.

---

### 4. Explain the benefits and drawbacks of this app’s underlying database system. 

##### 1. Reliability and Stability

**Advantage:** PostgreSQL is renowned for its robustness and stability, reliably handling complex queries and large datasets without data corruption.
**Disadvantage:** The comprehensive feature set and stability can lead to a more intricate setup and configuration process compared to simpler database systems.

##### 2. Advanced Features
**Advantage:** PostgreSQL offers advanced features like full-text search, JSON support, spatial data support (PostGIS), and sophisticated indexing techniques.
**Disadvantage:** These advanced features may present a steeper learning curve for new users or those transitioning from simpler database systems.

##### 3. Complexity in Configuration and Management
**Disadvantage:** PostgreSQL can be complex to configure and manage, particularly for users unfamiliar with its advanced features and extensive configuration options.
**Advantage:** The complexity allows for fine-tuned performance optimization and security configurations.

##### 4. Resource Intensive
**Disadvantage:** PostgreSQL can be more resource-intensive than other database systems, requiring more memory and CPU resources for optimal performance.
**Advantage:** The resource intensity often translates to better performance in handling complex queries and large datasets.

---

### 5. Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app. 

##### Features of the ORM in the Blog API

**Data Modeling and Schema Definition:** SQLAlchemy enables the definition of database tables as Python classes. Each class represents a table, and class attributes correspond to columns in that table.
**Database Interaction:** It offers a high-level abstraction for executing SQL queries, allowing CRUD (Create, Read, Update, Delete) operations through Python code instead of raw SQL.
**Relationships:** It supports defining relationships between different models, facilitating complex queries and operations involving multiple tables.
**Migration Management:** With tools like Flask-Migrate, SQLAlchemy helps manage database schema changes over time, making it easy to evolve the database schema alongside the application.

##### Purpose and Functionalities
**Simplified Database Management:** An ORM allows developers to interact with the database using Python code, making the development process more intuitive and less prone to errors.
**Reduced Boilerplate Code:** It reduces the need for writing repetitive SQL queries, improving code maintainability.
**Enhanced Security:** ORMs typically include built-in protection against SQL injection attacks, enhancing the security of database operations.
**Automatic Data Validation and Serialization:** With libraries like Marshmallow, SQLAlchemy automates data validation and serialization/deserialization, ensuring data consistency and reducing manual validation efforts.

---

### 6. Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design. This should focus on the database design BEFORE coding has begun, eg. during the project planning or design phase.

![ERD Diagram](ERD.jpg "ERD Diagram")

##### Relationships

**User and Post:**
One-to-Many: A user can create multiple posts, but each post is created by a single user. This is 
represented by the user_id foreign key in the Post model linking to the user_ID in the User model.

**User and Comments:**
One-to-Many: A user can write multiple comments, but each comment is written by a single user. The user_id foreign key in the Comments model links to the user_ID in the User model.

**User and Likes:**
One-to-Many: A user can like multiple posts, but each like is from a single user. The user_id foreign key in the Likes model links to the user_ID in the User model.

**Post and Comments:**
One-to-Many: A post can have multiple comments, but each comment is associated with a single post. This is represented by the post_id foreign key in the Comments model linking to the blog_ID in the Post model.

**Post and Likes:**
One-to-Many: A post can have multiple likes, but each like is associated with a single post. The post_id foreign key in the Likes model links to the blog_ID in the Post model.

**User and Comments (Indirect Relationship through Post):**
Many-to-Many: Users can comment on multiple posts, and posts can have comments from multiple users. This relationship is handled through the Comments model which has foreign keys to both User and Post.

**User and Likes (Indirect Relationship through Post):**
Many-to-Many: Users can like multiple posts, and posts can be liked by multiple users. This relationship is handled through the Likes model which has foreign keys to both User and Post.

---

### 7. Explain the implemented models and their relationships, including how the relationships aid the database implementation.

#### User

**Fields:**
- user_ID (Primary Key): Unique identifier for each user.
- email: User's email address.
- password_hashed: User's hashed password.
- name: User's name.
**Relationships:**
- One-to-Many with Post: A user can create multiple posts.
- One-to-Many with Comments: A user can write multiple comments.
- One-to-Many with Likes: A user can like multiple posts.

#### Post

**Fields:**
- blog_ID (Primary Key): Unique identifier for each post.
- title: Title of the post.
- content: Content of the post.
- date: Date the post was created.
- user_id (Foreign Key): References the user who created the post.
**Relationships:**
- Many-to-One with User: Each post is created by a single user.
- One-to-Many with Comments: A post can have multiple comments.
- One-to-Many with Likes: A post can have multiple likes.

#### Comments

**Fields:**
- comment_ID (Primary Key): Unique identifier for each comment.
- user_id (Foreign Key): References the user who wrote the comment.
- post_id (Foreign Key): References the post the comment is associated with.
- content: Content of the comment.
- timestamp: Time the comment was created.
**Relationships:**
- Many-to-One with User: Each comment is written by a single user.
- Many-to-One with Post: Each comment is associated with a single post.

#### Likes

**Fields:**
- likes_ID (Primary Key): Unique identifier for each like.
- user_id (Foreign Key): References the user who liked the post.
- post_id (Foreign Key): References the post that was liked.
**Relationships:**
- Many-to-One with User: Each like is made by a single user.
- Many-to-One with Post: Each like is associated with a single post.

#### How Relationships Aid Database Implementation
**Referential Integrity:** Foreign keys ensure that all references between tables are valid. For instance, a comment must be associated with a valid user and post.
**Cascade Operations:** Relationships can enable cascading operations, so deleting a post can automatically remove all associated comments and likes, maintaining database integrity.
**Efficient Data Retrieval:** Relationships allow for efficient data fetching. For example, retrieving a post can include all its comments and likes in one query, reducing the need for multiple database calls.
**Normalization:** By defining relationships, the database avoids redundancy, storing each piece of information only once and referencing it as needed.

---

### 8. Explain how to use this application’s API endpoints. Each endpoint should be explained, including the following data for each endpoint: HTTP verb, Path or route, Any required body or header data, Response.

#### User Endpoints

**Register User**

HTTP Verb: POST
Path: '/auth/register'
Body Data:

``
{
  "name": "Your Name",
  "email": "your.email@example.com",
  "password": "yourpassword"
}
``

Response:

``
{
  "message": "User registered successfully."
}
``

**Login User**
HTTP Verb: POST
Path: '/auth/login'
Body Data:

``
{
  "email": "your.email@example.com",
  "password": "yourpassword"
}
``

Response:

``
{
  "access_token": "your_jwt_token"
}
``

#### Post Endpoints

**Get All Posts**
HTTP Verb: GET
Path: '/posts'
Response:

``
[
  {
    "post_id": 1,
    "title": "Post Title",
    "content": "Post content",
    "date": "2023-07-28",
    "user": {
      "name": "Name"
    },
    "comments": [],
    "likes": []
  }
]
``

**Get Single Post**
HTTP Verb: GET
Path: '/posts/{post_id}'
Response:

``
{
  "post_id": 1,
  "title": "Post Title",
  "content": "Post content",
  "date": "2023-07-28",
  "user": {
    "name": "User Name"
  },
  "comments": [],
  "likes": []
}
``

**Create Post**
HTTP Verb: POST
Path: '/posts'
Header Data: Authorization: Bearer: your_jwt_token
Body Data:

``
{
  "title": "New Post Title",
  "content": "New post content"
}
``

Response:

``
{
  "post_id": 1,
  "title": "New Post Title",
  "content": "New post content",
  "date": "2023-07-28",
  "user": {
    "name": "User Name"
  },
  "comments": [],
  "likes": []
}
``

**Update Post**
HTTP Verb: PUT or PATCH
Path: '/posts/{post_id}'
Header Data: Authorization: Bearer: your_jwt_token
Body Data:

``
{
  "title": "Updated Post Title",
  "content": "Updated post content"
}
``

Response:

``
{
  "post_id": 1,
  "title": "Updated Post Title",
  "content": "Updated post content",
  "date": "2023-07-28",
  "user": {
    "name": "User Name"
  },
  "comments": [],
  "likes": []
}
``

**Delete Post**
HTTP Verb: DELETE
Path: '/posts/{post_id}'
Header Data: Authorization: Bearer: your_jwt_token
Response:

``
{
  "message": "Post deleted successfully."
}
``

#### Comment Endpoints

**Create Comment**
HTTP Verb: POST
Path: '/posts/{post_id}/comments'
Header Data: Authorization: Bearer: your_jwt_token
Body Data:

``
{
  "message": "New comment content"
}
``

Response:

``
{
  "comment_id": 1,
  "message": "New comment content",
  "date": "2023-07-28",
  "user": {
    "name": "User Name"
  },
  "post": {
    "title": "Post Title"
  }
}
``

**Delete Comment**
HTTP Verb: DELETE
Path: '/posts/{post_id}/comments/'{comment_id}
Header Data: Authorization: Bearer: your_jwt_token
Response:

``
{
  "message": "Comment deleted successfully."
}
``

#### Like Endpoints

**Create Like**
HTTP Verb: POST
Path: '/posts/{post_id}/likes'
Header Data: Authorization: Bearer: your_jwt_token
Response:

``
{
  "like_id": 1,
  "user": {
    "name": "User Name"
  },
  "post": {
    "title": "Post Title"
  }
}
``

**Delete Like**
HTTP Verb: DELETE
Path: '/posts/{post_id}/likes/{like_id}'
Header Data: Authorization: Bearer: your_jwt_token
Response:

``
{
  "message": "Like removed successfully."
}
``