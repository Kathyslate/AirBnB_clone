import json
from datetime import datetime
from models.base_model import BaseModel

storage = {}

class Storage:
    def new(self, obj):
        """Adds the object to storage"""
        key = obj.__class__.__name__ + "." + obj.id
        self.storage[key] = obj

    def save(self):
        """Saves the storage to a file"""
        with open("file.json", "w") as f:
            json.dump([obj.to_dict() for obj in self.storage.values()], f)

    def reload(self):
        """Reloads the storage from a file"""
        try:
            with open("file.json", "r") as f:
                data = json.load(f)
            for obj_data in data:
                obj = BaseModel(**obj_data)
                self.new(obj)
        except FileNotFoundError:
            pass
