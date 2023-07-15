#!/usr/bin/python3
"""A module that starts the Flask App"""

from models import storage
from models.user import User
from models.education import Education
from models.socials import Socials
from flask import Flask, render_template, url_for, redirect, flash, request
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
    """A function that loads the user from storage by id"""
    return storage.get_user_by_id(int(user_id))

@app.route("/", strict_slashes=False)
def home():
    """A function that renders the home page"""
    all_users = get_all_user(User)
    return render_template("home.html", title="Home", all_users=all_users,
                           current_user=current_user)

@app.route("/signup", strict_slashes=False,
           methods=['GET', 'POST'])
def signup():
    """A function that renders the signup page"""
    form = SignupForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            existing_user_email = storage.get_user(form.email.data)
            if existing_user_email:
                flash("That email already exists Please choose a different one.")
            hashed_password = bcrypt.generate_password_hash(form.password.data)
            storage.reload()
            new_user = User(first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            github_username=form.github_username.data,
                            email=form.email.data,
                            password=hashed_password,
                            phone_no=form.phone_no.data,
                            address=form.address.data)
            storage.new(new_user)
            storage.save()
            return redirect(url_for('login'))
    return render_template("signup.html", form=form, title="Signup")

@app.route("/login", strict_slashes=False,
           methods=['GET', 'POST'])
def login():
    """A function that renders the login page"""
    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = storage.get_user(form.email.data)
            if user:
                if bcrypt.check_password_hash(user.password, form.password.data):
                    login_user(user)
                    return redirect(url_for('dashboard', user=user.github_username))
            flash('Invalid email or password', 'error')
    return render_template("login.html", form=form, title="Login")

@app.route('/logout', strict_slashes=False,
           methods=['GET', 'POST'])
@login_required
def logout():
    """A function that renders the logout page"""
    logout_user()
    flash("You have been loggged out!", "info")
    return redirect(url_for('login'))

@app.route("/dashboard/<user>", strict_slashes=False,
           methods=['GET', 'POST'])
@login_required
def dashboard(user):
    """A function that renders the dashboard page"""
    username = user
    user_id = storage.get_user_git(user).id
    address = storage.get_user_git(user).address
    user = get_user(username)
    alx = validate_alx(username) 
    all_repos = get_all_repos(username)
    bio = get_bio(user_id)
    whatido = get_whatido(user_id)  
    title = get_title(user_id)
    socials = get_socials(user_id)
    education = get_education(user_id)
    return render_template("dashboard.html", alx=alx, whatido=whatido,
                           user=user, all_repos=all_repos, user_title=title,
                           bio=bio, socials=socials, address=address,
                           education=education, user_id=user_id, title="Dashboard")

@app.route("/dashboard/<user>/education", strict_slashes=False,
           methods=['GET', 'POST'])
@login_required
def addEducation(user):
    """A function that renders the add education page"""
    form = EducationForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            storage.reload()
            user = storage.get_user_git(user)
            education = storage.get_education_git(user.id)
            if education:
                if form.school.data:
                    education.school = form.school.data
                if form.year.data:
                    education.year = form.year.data
                if form.degree.data:
                    education.degree = form.degree.data
                storage.save()
            else:
                user_education = Education(school=form.school.data,
                                        year=form.year.data,
                                        degree=form.degree.data,
                                        user=user)
                storage.new(user_education)
                storage.save()
            return redirect(url_for('dashboard', user=user.github_username))
    return render_template("education.html", form=form, title="Education")

@app.route("/dashboard/<user>/socials", strict_slashes=False,
           methods=['GET', 'POST'])
@login_required
def addSocials(user):
    """A function that renders the add socials and bio page"""
    form = SocialsForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            storage.reload()
            user = storage.get_user_git(user)
            socials = storage.get_socials_git(user.id)
            if socials:
                if form.bio.data:
                    socials.bio = form.bio.data
                if form.title.data:
                    socials.title = form.title.data
                if form.whatido.data:
                    socials.whatido = form.whatido.data
                if form.twitter.data:
                    socials.twitter = form.twitter.data
                if form.linkedin.data:
                    socials.linkedin = form.linkedin.data
                if form.instagram.data:
                    socials.instagram = form.instagram.data
                storage.save()
            else:
                user_socials = Socials(bio=form.bio.data,
                                       title=form.title.data,
                                       whatido=form.title.data,
                                       twitter=form.twitter.data,
                                       linkedin=form.linkedin.data,
                                       instagram=form.instagram.data,
                                       user=user)
                storage.new(user_socials)
                storage.save()
            return redirect(url_for('dashboard', user=user.github_username))
    return render_template("socials.html", form=form, title="Socials")

@app.route("/<user>", strict_slashes=False,
           methods=['GET', 'POST'])
def userPortfolio(user):
    """A function that renders the user portfolio page"""
    if user:
        username = user 
        user_obj = storage.get_user_git(user)
        user_id = None
        address = None
        try:
            user_id = user_obj.id 
            address = user_obj.address 
        except Exception as e:
            print(e)
        user = get_user(username)  
        alx = validate_alx(username)
        all_repos = get_all_repos(username)
        bio = get_bio(user_id)
        whatido = get_whatido(user_id)
        title = get_title(user_id)
        socials = get_socials(user_id)
        education = get_education(user_id)
        return render_template("userPort.html", alx=alx, whatido=whatido,
                            user=user, all_repos=all_repos, user_title=title,
                            bio=bio, socials=socials, address=address,
                            education=education, user_id=user_id, title="Portfolio")
    else:
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)