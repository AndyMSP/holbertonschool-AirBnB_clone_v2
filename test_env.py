#!/usr/bin/python3
# Setup python environment for testing HBNB functions

import os

# Environment variables that can be changed
os.environ['HBNB_ENV'] = 'real'
os.environ['HBNB_TYPE_STORAGE'] = 'db'
os.environ['HBNB_MYSQL_USER'] = 'hbnb_dev'
os.environ['HBNB_MYSQL_PWD'] = 'hbnb_dev_pwd'
os.environ['HBNB_MYSQL_HOST'] = 'localhost'
os.environ['HBNB_MYSQL_DB'] = 'hbnb_dev_db'

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
