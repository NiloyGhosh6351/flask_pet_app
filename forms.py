from flask_wtf import FlaskForm  # type: ignore
from wtforms import StringField, IntegerField, SubmitField  # type: ignore
from wtforms.validators import DataRequired  # type: ignore

class PetForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    type = StringField('Type', validators=[DataRequired()])
    submit = SubmitField('Add Pet')