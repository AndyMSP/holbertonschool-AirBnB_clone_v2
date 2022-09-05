#!/usr/bin/python3
"""Module handling database storage"""
# import os
# from typing_extensions import Self
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, scoped_session
# from models.base_model import Base
# from models.base_model import BaseModel
# from models.user import User
# from models.place import Place
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.review import Review

from curses import echo
import os
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.review import Review




# Set these internally for testing and development
# HBNB_ENV = 'dev'
# HBNB_MYSQL_USER = 'hbnb_dev'
# HBNB_MYSQL_PWD = 'hbnb_dev_pwd'
# HBNB_MYSQL_HOST = 'localhost'
# HBNB_MYSQL_DB = 'hbnb_dev_db'

# Set these with environmental variables for project requirements
# HBNB_ENV = os.getenv('HBNB_ENV')
# HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
# HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
# HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
# HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')

os.environ['HBNB_MYSQL_USER'] = 'hbnb_dev'
os.environ['HBNB_MYSQL_PWD'] = 'hbnb_dev_pwd'
os.environ['HBNB_MYSQL_HOST'] = 'localhost'
os.environ['HBNB_MYSQL_DB'] = 'hbnb_dev_db'


# classes = {
#             'State': State, 'City': City
#           }


class DBStorage:
    """Class defining database storage object"""

    __engine = None
    __session = None

    # def __init__(self):
    #     """function to run during DBstorage instance creation"""
    #     conn = f"mysql+mysqldb://{HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@\{HBNB_MYSQL_HOST}/{HBNB_MYSQL_DB}"
    #     self.__engine = create_engine(conn, pool_pre_ping=True, echo=False)
    #     if HBNB_ENV == 'test':
    #         Base.metadata.drop_all(self.__engine)


    def __init__(self):
        """Engine"""
        self.__engine = db.create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)


    # def reload(self):
    #     """Bring database into application as objects"""
    #     Base.metadata.create_all(self.__engine)
    #     session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
    #     session = scoped_session(session_factory)
    #     self.__session = session()


    def reload(self):
        """Loads information from Database and starts Session"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(sess_factory)
        self.__session = session()


    def new(self, obj):
        """Add object to current session"""
        self.__session.add(obj)


    def save(self):
        """Save to database"""
        self.__session.commit()

    # def delete(self, obj):
    #     """delete object from current session"""
    #     self.__session.delete(obj)


    def delete(self, obj=None):
        """Deletes from table"""
        if obj is not None:
            self.__session.delete(obj)

    # def all(self, cls=None):
    #     """Returns a dictionary of models currently in storage"""
    #     results = {}
    #     if cls is None:
    #         for k, v in classes.items():
    #             objs = self.__session.query(v).all()
    #             for obj in objs:
    #                 results[f"{k}.{obj.id}"] = obj
    #     else:
    #         objs = self.__session.query(cls).all()
    #         for obj in objs:
    #             results[f"{k}.{obj.id}"] = obj
    #     return results


    def all(self, cls=None):
        """Returns dictionary"""
        table_dict = {}
        classes = {
            'State': State,
            'City': City}
        if cls is None:
            for c in classes:
                result = self.__session.query(classes[c]).all()
                for obj in result:
                    table_dict[f"{type(obj).__name__}.{obj.id}"] = obj
        else:
            result = self.__session.query(classes[cls]).all()
        for obj in result:
            table_dict[f"{type(obj).__name__}.{obj.id}"] = obj
        return table_dict

