#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import os

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')


class User(BaseModel, Base):
    """ User class """
    if (HBNB_TYPE_STORAGE == 'db'):
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship('Place', back_populates='user', cascade='all, delete')
        reviews = relationship('Review', back_populates='user', cascade='all, delete')