from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import Email, DataRequired

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('E-Mail', validators=[Email(), DataRequired()])
    phone = IntegerField('Phone')
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')

class NewsletterSubscribe(FlaskForm):
    email = StringField('E-Mail', validators=[Email(), DataRequired()])
    submit = SubmitField('SUBSCRIBE')