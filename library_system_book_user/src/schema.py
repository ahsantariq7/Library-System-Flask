from marshmallow import Schema, fields


class BookSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    author = fields.Nested(
        lambda: UserSchema(exclude=("books",)), dump_only=True, only=("id", "username")
    )
    author_id = fields.Integer()


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String()
    books = fields.Nested(BookSchema, many=True, exclude=("author",))


book_schema = BookSchema()
books_schema = BookSchema(many=True)
user_schema = UserSchema()
users_schema = UserSchema(many=True)
