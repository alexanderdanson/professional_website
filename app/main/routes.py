from app.main import bp
from flask import render_template

@bp.route('/')
@bp.route('/index', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@bp.route('/test')
def test():
    return render_template('test.html')