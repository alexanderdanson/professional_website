from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import Email, Length, ValidationError, DataRequired

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('E-Mail', validators=[Email, DataRequired()])
    phone = IntegerField('Phone', validators=[Length(min=0, max=12)])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')