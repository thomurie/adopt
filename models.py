from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

default_img = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5TyD_D5zFsu6L3TFMxTq2VHgwzqka4qw8Pg&usqp=CAU'

def connect_db(app):

    db.app = app
    db.init_app(app)

class Pet(db.Model):

    __tablename__ = "pet"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name= db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text, default= default_img)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable = False, default = True)
