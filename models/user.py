#!/usr/bin/python3
"""Defines the User class"""

from flask_login import UserMixin
from models.basemodel import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(Base, BaseModel, UserMixin):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    github_username = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    phone_no = Column(String(20), nullable=False)
    address = Column(String(200), nullable=False)
    education = relationship('Education', backref='user')
    socials = relationship('Socials', backref='user')