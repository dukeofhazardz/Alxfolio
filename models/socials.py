#!/usr/bin/python3
"""Defines the Socials class"""

from flask_login import UserMixin
from models.basemodel import Base, BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey


class Socials(Base, BaseModel, UserMixin):
    """This class defines a user by various attributes"""
    __tablename__ = "socials"
    bio = Column(String(1000), nullable=True)
    title = Column(String(1000), nullable=True)
    whatido = Column(String(1000), nullable=True)
    twitter = Column(String(100), nullable=True)
    linkedin = Column(String(100), nullable=True)
    instagram = Column(String(100), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)