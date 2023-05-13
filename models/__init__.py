# from models.base_model import BaseModel
# from models.engine import storage
#!/usr/bin/python3
"""__init__ magic method for models dir"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
