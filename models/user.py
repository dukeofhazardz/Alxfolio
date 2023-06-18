#!/usr/bin/python3
"""Defines the User class"""

from flask_login import UserMixin
from models.basemodel import Base, BaseModel
from sqlalchemy import Column, String


class User(Base, BaseModel, UserMixin):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    github_username = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    phone_no = Column(String(15))