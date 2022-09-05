#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


place_amenity = Table('association', Base.metadata,
    Column('place_id', ForeignKey('places.id'), primary_key=True),
    Column('amenity_id', ForeignKey('amenities.id'), primary_key=True)
)



class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    cities = relationship('City', back_populates='places')
    user = relationship('User', back_populates='places')
    reviews = relationship('Review', back_populates='place', cascade='all, delete')
    place_amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        back_populates="place_amenities")
    