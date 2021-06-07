from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, AnyOf, NumberRange

values = [ 'cat', 'dog', 'porcupine', 'Cat', 'Dog', 'Porcupine']

class NewPetForm(FlaskForm):
    name = StringField("Pet Name", validators = [InputRequired()])
    species = StringField('Species', validators = [AnyOf(values)]) 
    photo_url = StringField('Photo URL', validators = [Optional(), URL()])
    age = IntegerField("Pet Age", validators = [NumberRange(min=0, max=30)])
    notes = StringField('Notes')
    available = BooleanField('available')

class EditPetForm(FlaskForm):
    name = StringField("Pet Name", validators = [InputRequired()])
    species = StringField('Species', validators = [AnyOf(values)]) 
    photo_url = StringField('Photo URL', validators = [Optional(), URL()])
    age = IntegerField("Pet Age", validators = [NumberRange(min=0, max=30)])
    notes = StringField('Notes')
    available = BooleanField('available')