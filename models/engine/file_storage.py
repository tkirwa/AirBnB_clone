import json
import os.path

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(json_dict, file)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                json_dict = json.load(file)
                for key, value in json_dict.items():
                    class_name = key.split(".")[0]
                    instance = eval(class_name)()
                    for attr, val in value.items():
                        if attr != "__class__":
                            setattr(instance, attr, val)
                    self.__objects[key] = instance

    def _deserialize_objects(self):
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value["__class__"]
                    if class_name in classes:
                        obj = classes[class_name](**value)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def _serialize_objects(self):
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }

        serialized_objects = {}
        for key, obj in self.__objects.items():
            class_name = obj.__class__.__name__
            if class_name in classes:
                serialized_objects[key] = obj.to_dict()
                serialized_objects[key].update({"__class__": class_name})
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)
