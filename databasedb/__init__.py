import os

from databasedb.interface import DatabaseDB

__all__ = ['DatabaseDB', 'connect']

def connect(dbname: str) -> DatabaseDB:
    try:
        file = open(dbname, 'r+b')
    except IOError:
        file_disk = os.open(dbname, os.O_RDWR | os.O_CREAT)
        file = os.fdopen(file_disk, 'r+b')
    return DatabaseDB(file)