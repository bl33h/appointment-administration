from app import app
from flask import render_template, flash, request, redirect
from app.forms import LoginForm, EnteringStudentData

@app.route('/index', methods=['POST', 'GET'])
def index():
    form = EnteringStudentData()
    return render_template('index.html', title='Inicio', form =form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
    