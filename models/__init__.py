#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

# Comment out for final project
# os.environ['HBNB_ENV'] = 'real'
# os.environ['HBNB_TYPE_STORAGE'] = 'file'
# os.environ['HBNB_MYSQL_USER'] = 'hbnb_dev'
# os.environ['HBNB_MYSQL_PWD'] = 'hbnb_dev_pwd'
# os.environ['HBNB_MYSQL_HOST'] = 'localhost'
# os.environ['HBNB_MYSQL_DB'] = 'hbnb_dev_db'

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')

if HBNB_TYPE_STORAGE == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
