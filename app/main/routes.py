from app.main import bp
from app.main.forms import ContactForm
from app.main.email import contact_me_email
from flask import render_template, redirect, flash

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        from_name = form.name.data
        sender = form.email.data
        message_body = form.message.data
        phone = form.phone.data
        contact_me_email(from_name=from_name, sender=sender, message_body=message_body, phone=phone)
        flash("Thanks for your email, I'll get back to you as soon as I can!")
    return render_template('index.html', form=form)

@bp.route('/music', methods=['GET', 'POST'])
def music():
    form = ContactForm()
    if form.validate_on_submit():
        from_name = form.name.data
        sender = form.email.data
        message_body = form.message.data
        phone = form.phone.data
        contact_me_email(from_name=from_name, sender=sender, message_body=message_body, phone=phone)
        flash("Thanks for your email, I'll get back to you as soon as I can!")
    return render_template('music_index.html', form=form)

@bp.route('/test')
def test():
    return render_template('test.html')