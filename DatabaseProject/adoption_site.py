# adoption_site.py
import os
#from forms import AddForm, DelForm
from flask import Flask, render_template, url_for,redirect,session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from adoption_form import AddForm, DelForm, Add_owner

app = Flask(__name__)

#setup a key for forms
app.config['SECRET_KEY'] = 'mykey'


 #########################################
 #####SQL Database Section################
 #########################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#create a data base for our application
db = SQLAlchemy(app)
Migrate(app,db)

##########################################
############ Model #######################
##########################################

class Puppy(db.Model):

    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner',backref='puppy',uselist=False)


    def __init__(self,name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return("Puppy name is: {} and owner is {}".format(self.name,self.owner.name))
        else:
            return("Puppy name is: {} and has no owner assgined yet".format(self.name))


class Owner(db.Model):

    __tablename__ = "owners"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))


    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return ("Owner name {}".format(self.name))


##########################################
############# View functions #############
##########################################

@app.route('/')
def index():
    return render_template('adoption_Home.html')


@app.route('/owner',methods=['GET','POST'])
def owner():

    form = Add_owner()

    if form.validate_on_submit():

        name = form.name.data
        pup_id = form.pup_id.data

        new_owner = Owner(name,pup_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('adoption_Owner.html',form=form)


@app.route('/add',methods=['get','post'])
def add_pup():
    form = AddForm()
    if form.validate_on_submit():

        name = form.name.data

        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('list_pup'))

    return render_template('adoption_Add.html',form=form)


@app.route('/list')
def list_pup():

    puppies = Puppy.query.all()
    return render_template('adoption_list.html',puppies = puppies)

@app.route('/delete',methods=['get','post'])
def del_pup():


    form = DelForm()

    if form.validate_on_submit():

        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('adoption_delete.html',form=form)


if __name__=='__main__':
    app.run(debug=True)
