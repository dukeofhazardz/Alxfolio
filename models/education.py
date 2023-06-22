#!/usr/bin/python3
"""Defines the Education class"""

from flask_login import UserMixin
from models.basemodel import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey


class Education(Base, BaseModel, UserMixin):
    """This class defines a Education by various attributes"""
    __tablename__ = "education"
    school = Column(String(200), nullable=True)
    degree = Column(String(200), nullable=True)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)