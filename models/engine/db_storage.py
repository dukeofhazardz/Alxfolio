#!/usr/bin/python3
"""The module for Database Storage"""

from models.basemodel import Base
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """ This class defines the DBstorage """

    # Private attributes
    __engine = None
    __session = None

    def __init__(self):
        """This method initializes a new DBStorage instance"""
        self.__engine = create_engine("mysql+mysqldb://gitfolio_dev:gitfolio_pwd@localhost/gitfolio_db",
                                      pool_pre_ping=True)

    def all(self):
        """ A method that retrieves all the data in a class
            and returns it as a dict """
        objs = self.__session.query(User).all()
        return {"{}.{}".format(type(obj).__name__, obj.id) for obj in objs}

    def get_user(self, email):
        """A method that get the data from storage for validation"""
        user = self.__session.query(User).filter(User.email==email).first()
        return user

    def get_user_by_id(self, user_id):
        """A method that get the data from storage for validation"""
        user = self.__session.query(User).filter(User.id==user_id).first()
        return user

    def new(self, obj):
        """ Adds the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes from the current database session obj if not None """
        if (obj):
            self.__session.delete(obj)

    def reload(self):
        """this method creates all the tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Calls the close() method on session attribute(self.__session) """
        self.__session.close()