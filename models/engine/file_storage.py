import json
import os.path


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
