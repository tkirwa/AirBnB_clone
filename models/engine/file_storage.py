#!/usr/bin/python3

import json


class FileStorage:
    """
    FileStorage class is responsible for serializing instances to a JSON file and deserializing JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary that stores all objects by <class name>.id.

    Methods:
        all(self): Returns the dictionary of all objects.
        new(self, obj): Adds a new object to the dictionary.
        save(self): Serializes the objects to the JSON file.
        reload(self): Deserializes the JSON file to objects.

    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all objects.

        Returns:
            dict: Dictionary of all objects.

        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary.

        Args:
            obj: Object to be added.

        The object is stored in the dictionary with the key "<class name>.<id>".

        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes the objects to the JSON file.

        The objects dictionary is converted to a dictionary of JSON-serializable representations.
        The resulting dictionary is then written to the JSON file.

        """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to objects.

        If the JSON file exists, it is read and parsed into a dictionary.
        Each key-value pair in the dictionary is processed to recreate the objects and store them in the objects dictionary.

        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    module_name = class_name.lower()
                    module = __import__("models." + module_name, fromlist=[class_name])
                    cls = getattr(module, class_name)
                    FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
