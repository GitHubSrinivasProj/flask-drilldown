import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#setting up a sqlite database
# choose a directory

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# connect the flask to database

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#pass in the application to the Database
db = SQLAlchemy(app)

# connects the app with the database inorder to add on migration capabilities
Migrate(app,db)

########################################################


#setting up a model
#model is just a setting up a table in our database
# Puppy here is a tablename but it can be overridden to another
#tablename using __tablename__ = 'Provide a table name'
#by default the class name and adds 's' to it and  is considered as table name
class Puppy(db.Model):

    #manual table name
    __tablename__ = "Puppies"

    #create columns to the table

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        return("Puppy {} is {} years old and is of the {} breed".format((self.name),(self.age),(self.breed)))
