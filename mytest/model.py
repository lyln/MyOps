from app.db import db

__author__ = 'ljd'


class test_db(db.Model):
    __tablename__ = "test_db"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(45))

    def __repr__(self):
        return '<name %r>' %self.name