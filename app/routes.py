from flask import render_template, flash, redirect, url_for
from flask import request
from app import app
from app.form import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Idiris'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
    ]
    return render_template('index.html', user=user, posts=posts)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)