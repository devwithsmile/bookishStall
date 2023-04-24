# auth/routes

from flask import render_template, request, flash, redirect, url_for
from app.auth.forms import RegisterationForm, Login_Form
from app.auth import authentication as at
from app.catlog import main
from app.auth.models import User
from flask_login import login_user, logout_user,login_required,current_user


@at.route('/register', methods=['GET', 'POST'])
def register_user():
    form = RegisterationForm()
    if current_user.is_authenticated:
        flash("already logged-in.")
        return redirect(url_for('main.display_books'))
    
    if form.validate_on_submit():
        User.create_user(
            form.name.data,
            form.email.data,
            form.password.data
        )

        flash('Registeration Successful')
        return redirect(url_for("authentication.login_user"))
    return render_template('register.html', form=form)


@at.route('/login', methods=['GET', 'POST'])
def login_current_user():
    if current_user.is_authenticated:
        flash("already logged-in.")
        return redirect(url_for('main.display_books'))
    form = Login_Form()
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.email.data).first()
        if not user or not user.check_password(form.password.data):
            flash("Invalid Credentials !! Try again")
            return redirect(url_for("authentication.login_current_user",form=form))

        login_user(user, form.stay_loggedin.data)
        return redirect(url_for("main.display_books"))

    return render_template('login.html',form=form)


@at.route('/logout')
@login_required
def log_out_user():
    logout_user()
    return redirect(url_for('authentication.login_current_user'))