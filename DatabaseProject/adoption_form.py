## create forms here
## created this two forms to get the data from the user
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):

    name = StringField('Name of the puppy: ')
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):

    id = IntegerField("Id number of Puppy to remove: ")
    submit = SubmitField('Remove Puppy')

class Add_owner(FlaskForm):

    name = StringField("Name of the Owner:")
    pup_id = IntegerField("Id of Puppy:")
    submit = SubmitField('Add Owner')
