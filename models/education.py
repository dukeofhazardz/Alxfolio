#!/usr/bin/python3
"""Defines the Education class"""

from flask_login import UserMixin
from models.basemodel import Base, BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey


class Education(Base, BaseModel, UserMixin):
    """This class defines a Education by various attributes"""
    __tablename__ = "education"
    school = Column(String(100), nullable=True)
    year = Column(Integer, nullable=True)
    degree = Column(String(100), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)