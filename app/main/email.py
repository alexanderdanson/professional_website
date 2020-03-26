from flask_mail import Message
from app import mail
from app import app
from flask import render_template

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

def contact_me_email(from_name, sender, message_body, phone):
    send_email('[AlexanderDanson.com] New Message From {}'.format(from_name),
               sender=sender,
               recipients=[app.config['ADMINS'][0]],
               text_body=render_template('email/contact.txt', message_body=message_body, phone=phone,
                                         sender=sender, from_name=from_name),
               html_body=render_template('email/contact.html', message_body=message_body, phone=phone,
                                         sender=sender, from_name=from_name))
