#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state', cascade='all, delete')

    @property
    def cities_att(self):
        """Defines cities attribute for FileStorage"""
        from models import storage
        cities_dict = storage.all('City')
        cities_list = []
        for key, value in cities_dict.items():
            if value.state_id == self.id:
                cities_list.append(value)
        return cities_list