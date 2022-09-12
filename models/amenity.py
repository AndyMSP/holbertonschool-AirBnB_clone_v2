#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import os

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    if (HBNB_TYPE_STORAGE == 'db'):
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            'Place',
            secondary='place_amenity',
            back_populates='amenities')
