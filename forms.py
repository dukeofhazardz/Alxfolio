#!/usr/bin/python3

"""A module containing all forms used in the app"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Length


class SignupForm(FlaskForm):
    first_name = StringField(validators=[InputRequired(), Length(
        min=2, max=100)], render_kw={"placeholder": "First Name"})
    
    last_name = StringField(validators=[InputRequired(), Length(
        min=2, max=100)], render_kw={"placeholder": "Last Name"})
    
    github_username = StringField(validators=[InputRequired(), Length(
        min=4, max=100)], render_kw={"placeholder": "Github Username"})
    
    email = StringField(validators=[InputRequired(), Length(
        min=10, max=100)], render_kw={"placeholder": "Email"})
    
    password = PasswordField(validators=[InputRequired(), Length(
        min=8, max=100)], render_kw={"placeholder": "Password"})
    
    phone_no = StringField(validators=[InputRequired(), Length(
        min=8, max=100)], render_kw={"placeholder": "Phone Number"})    

    submit = SubmitField("Signup")


class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Length(
        min=10, max=100)], render_kw={"placeholder": "Email"})
    
    password = PasswordField(validators=[InputRequired(), Length(
        min=8, max=100)], render_kw={"placeholder": "Password"})  

    submit = SubmitField("Login")


class EducationForm(FlaskForm):
    school = StringField(validators=[InputRequired(), Length(
        min=10, max=100)], render_kw={"placeholder": "School"})
    
    year = StringField(validators=[InputRequired(), Length(
        min=4, max=10)], render_kw={"placeholder": "Year"})
    
    degree = StringField(validators=[InputRequired(), Length(
        min=10, max=100)], render_kw={"placeholder": "Degree"})
    
    submit = SubmitField("Save")


class SocialsForm(FlaskForm):
    bio = twitter = StringField(validators=[InputRequired(), Length(
        min=10, max=1000)], render_kw={"placeholder": "Bio"})

    twitter = StringField(validators=[InputRequired(), Length(
        min=10, max=100)], render_kw={"placeholder": "Twitter Url"})
    
    linkedin = StringField(validators=[InputRequired(), Length(
        min=10, max=100)], render_kw={"placeholder": "Linkedin Url"})
    
    instagram = StringField(validators=[InputRequired(), Length(
        min=10, max=100)], render_kw={"placeholder": "Instagram Url"})
    
    submit = SubmitField("Save")