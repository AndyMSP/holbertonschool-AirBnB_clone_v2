#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage

# Update these to environmental variables!!!
HBNB_TYPE_STORAGE = 'file'

if HBNB_TYPE_STORAGE == 'db':
    from models.engine.db_storage import DBstorage
    storage = DBstorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
