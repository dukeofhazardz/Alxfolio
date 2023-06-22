#!/usr/bin/python3
"""Defines the Socials class"""

from flask_login import UserMixin
from models.basemodel import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey


class Socials(Base, BaseModel, UserMixin):
    """This class defines a user by various attributes"""
    __tablename__ = "socials"
    twitter = Column(String(200), nullable=True)
    linkedin = Column(String(200), nullable=True)
    instagram = Column(String(200), nullable=True)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)