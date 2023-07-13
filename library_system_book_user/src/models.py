from src.extensions import db


class BaseMixin(object):
    id = db.Column(db.Integer, primary_key=True, index=True)
    created_on = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())
    updated_on = db.Column(db.TIMESTAMP, onupdate=db.func.current_timestamp())


class ReprMixin(object):
    __repr_fields__ = ["id", "username", "books"]

    def __repr__(self):
        fields = {f: getattr(self, f, "<BLANK>") for f in self.__repr_fields__}
        pattern = ["{0}={{{0}}}".format(f) for f in self.__repr_fields__]
        pattern = " ".join(pattern)
        pattern = pattern.format(**fields)
        return "<{} {}>".format(self.__class__.__name__, pattern)


class User(BaseMixin, ReprMixin, db.Model):
    __tablename__ = "user"

    username = db.Column(db.String(50))
    books = db.relationship("Book", backref="author", lazy=True)


class Book(BaseMixin, ReprMixin, db.Model):
    title = db.Column(db.String(100))
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
