from flask import Blueprint, request
from flask_restful import Api, Resource

from src.app import app
from src.extensions import db
from src.models import Book, User
from src.schema import book_schema, books_schema, user_schema, users_schema

api_blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(api_blueprint)


class BookResource(Resource):
    def get(self, book_id):
        book = db.session.get(Book, book_id)
        if book:
            return book_schema.dump(book)
        else:
            return {"message": "Book not found"}, 404

    def put(self, book_id):
        book = db.session.get(Book, book_id)
        if not book:
            return {"message": "Book not found"}, 404

        data = request.get_json()
        book.title = data["title"]
        book.author_id = data["author_id"]
        db.session.commit()
        return book_schema.dump(book)

    def delete(self, book_id):
        book = db.session.get(Book, book_id)
        if not book:
            return {"message": "Book not found"}, 404

        db.session.delete(book)
        db.session.commit()
        return {"message": "Book deleted"}, 200


class BookListResource(Resource):
    def get(self):
        books = Book.query.all()
        return books_schema.dump(books)

    def post(self):
        data = request.get_json()
        book = Book(title=data["title"], author_id=data["author_id"])
        db.session.add(book)
        db.session.commit()
        return book_schema.dump(book), 201


class UserResource(Resource):
    def get(self, user_id):
        user = db.session.get(User, user_id)
        if user:
            return user_schema.dump(user)
        else:
            return {"message": "User not found"}, 404

    def put(self, user_id):
        user = db.session.get(User, user_id)
        if not user:
            return {"message": "User not found"}, 404

        data = request.get_json()
        user.username = data["username"]
        db.session.commit()
        return user_schema.dump(user)

    def delete(self, user_id):
        user = db.session.get(User, user_id)
        if not user:
            return {"message": "User not found"}, 404

        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}, 200


class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return users_schema.dump(users)

    def post(self):
        data = request.get_json()
        user = User(username=data["username"])
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user), 201


api.add_resource(UserResource, "/users/<int:user_id>")
api.add_resource(UserListResource, "/users")
api.add_resource(BookResource, "/books/<int:book_id>")
api.add_resource(BookListResource, "/books")

app.register_blueprint(api_blueprint)
