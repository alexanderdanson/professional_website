from app.main import bp
from app.main.forms import ContactForm
from flask import render_template

@bp.route('/')
@bp.route('/index', methods = ['GET', 'POST'])
def index():
    form = ContactForm()
    return render_template('index.html', form=form)

@bp.route('/test')
def test():
    return render_template('test.html')