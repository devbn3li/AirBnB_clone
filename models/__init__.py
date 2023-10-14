#!/usr/bin/python3
"""Initialize the storage system and load data from the JSON file."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
