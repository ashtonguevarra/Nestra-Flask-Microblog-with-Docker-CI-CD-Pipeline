from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from sqlalchemy as sa 
from app import db
from app.models import User 
from flask_login import login_required
from flask import requestfrom urllib.parse import urlsplit

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Ashton'}
    posts = [
        {
            'author': {'username': 'Dom'},
            'body': 'I pissed my pants today.'
        },
        {
            'author': {'username': 'Tonee'},
            'body': 'I think I have a crush on Ashton.'
        },
        {
            'author': {'username': 'Pau'},
            'body': 'so uhh we broke up...'
        },
        {
            'author': {'username': 'Drei'},
            'body': 'best night ever with robie!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)