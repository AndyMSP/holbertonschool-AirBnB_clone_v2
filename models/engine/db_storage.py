#!/usr/bin/python3
"""Module handling database storage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

# Update these to environmental variables!!!
HBNB_ENV = 'dev'
HBNB_MYSQL_USER = 'hbnb_dev'
HBNB_MYSQL_PWD = 'hbnb_dev_pwd'
HBNB_MYSQL_HOST = 'localhost'
HBNB_MYSQL_DB = 'hbnb_dev_db'


classes = {
            'State': State, 'City': City
          }


class DBstorage:
    """Class defining database storage object"""

    __engine = None
    __session = None

    def __init__(self):
        """function to run during DBstorage instance creation"""
        conn = f"mysql+mysqldb://{HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@\{HBNB_MYSQL_HOST}/{HBNB_MYSQL_DB}"
        self.__engine = create_engine(conn, pool_pre_ping=True, echo=False)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)


    def reload(self):
        """Bring database into application as objects"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()


    def new(self, obj):
        """Add object to current session"""
        self.__session.add(obj)


    def save(self):
        self.__session.commit()


    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        results = {}
        if cls is None:
            for k, v in classes.items():
                objs = self.__session.query(v).all()
                for obj in objs:
                    results[f"{k}.{obj.id}"] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                results[f"{k}.{obj.id}"] = obj
        return results

        # else:
        #     class_dict = {}
        #     for k, v in FileStorage.__objects.items():
        #         if v.__class__ == cls:
        #             class_dict.update({k:v})
        #     return class_dict