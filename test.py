#!/usr/bin/python3

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBstorage
from models.state import State
from models.city import City

fs = FileStorage()
ds = DBstorage()