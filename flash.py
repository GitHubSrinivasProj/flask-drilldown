from flask import Flask,render_template,request,session,redirect,flash,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__)

app.config['SECRET_KEY']='mykey'

class SimpleForm(FlaskForm):

    breed = StringField('What breed are you?')
    submit = SubmitField('Click Me!')

@app.route('/',methods=['get','post'])
def index():

    #create a instance of the form
    form = SimpleForm()

    if form.validate_on_submit():
        session['breed']=form.breed.data
        flash("You just changed your breed to: {}".format(session['breed']))

        return redirect(url_for('index'))

    return render_template('flash.html',form = form)



if __name__=='__main__':
    app.run(debug=True)
