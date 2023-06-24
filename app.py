#!/usr/bin/python3

"""A module that starts the Flask App"""

from models import storage
from models.user import User
from models.education import Education
from models.socials import Socials
from flask import Flask, render_template, url_for, redirect, flash
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from wtforms.validators import ValidationError
from flask_bcrypt import Bcrypt
from functions import *
from forms import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return storage.get_user_by_id(int(user_id))

@app.route("/", strict_slashes=False)
def home():
    return render_template("home.html", title="Home")

@app.route("/signup", strict_slashes=False,
           methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        existing_user_email = storage.get_user(form.email.data)
        if existing_user_email:
            raise ValidationError("That email already exists Please choose a different one.")
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        storage.reload()
        new_user = User(first_name=form.first_name.data,
                        last_name=form.last_name.data,
                        github_username=form.github_username.data,
                        email=form.email.data,
                        password=hashed_password,
                        phone_no=form.phone_no.data)
        storage.new(new_user)
        storage.save()
        return redirect(url_for('login'))
    return render_template("signup.html", form=form, title="signup")

@app.route("/login", strict_slashes=False,
           methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = storage.get_user(form.email.data)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard', user=user.github_username))
    return render_template("login.html", form=form, title="login")

@app.route('/logout', strict_slashes=False,
           methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/dashboard/<user>", strict_slashes=False,
           methods=['GET', 'POST'])
@login_required
def dashboard(user):
    username = user
    user = g.get_user(username)
    alx = validate_alx(username)
    all_repos = get_all_repos(username)
    return render_template("dashboard.html", alx=alx, user=user, all_repos=all_repos)

@app.route("/dashboard/<user>/education", strict_slashes=False,
           methods=['GET', 'POST'])
@login_required
def addEducation(user):
    form = EducationForm()

    if form.validate_on_submit():
        storage.reload()
        user = storage.get_user_git(user)
        user_education = Education(school=form.school.data,
                                   year=form.year.data,
                                   degree=form.degree.data,
                                   user=user)
        storage.new(user_education)
        storage.save()
        return redirect(url_for('dashboard', user=user.github_username))
    return render_template("education.html", form=form, title="education")

@app.route("/dashboard/<user>/socials", strict_slashes=False,
           methods=['GET', 'POST'])
@login_required
def addSocials(user):
    form = SocialsForm()

    if form.validate_on_submit():
        storage.reload()
        user = storage.get_user_git(user)
        user_socials = Socials(bio=form.bio.data,
                                   twitter=form.twitter.data,
                                   linkedin=form.linkedin.data,
                                   instagram=form.instagram.data,
                                   user=user)
        storage.new(user_socials)
        storage.save()
        return redirect(url_for('dashboard', user=user.github_username))
    return render_template("socials.html", form=form, title="socials")


if __name__ == "__main__":
    app.run(debug=True, port=6060)