from db import db

class Image_Url(db.Model):
    __tablename__ = "image_urls"
    image_id = db.Column(db.Integer,primary_key=True)
    image_url = db.Column(db.String(255))

    # def __repr__(self):
    #     return '<image_urls %r>' %self.image_url


class Test_user(db.Model):
    __tablename__ = "test_user"
    user_id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(20))


class Project_List(db.Model):
    __tablename__ = "project_list"
    project_id = db.Column(db.Integer,primary_key=True)
    project_name = db.Column(db.String(45))
    host_name = db.Column(db.String(45))