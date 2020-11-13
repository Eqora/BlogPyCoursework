from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ilya Keduk'}
    posts = [
        {
            'author': {'username': 'Maxim'},
            'body': 'I am IOS Programmer!'
        },
        {
            'author': {'username': 'Sergey'},
            'body': 'I am crazy about Photoshop!'
        },
        {
            'author': {'username': 'Vadim'},
            'body': 'I am 10th level of faceit!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)
