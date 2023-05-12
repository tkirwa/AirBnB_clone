import uuid
from datetime import datetime
from models import storage


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)

<<<<<<< HEAD
    def __str__(self,):
        """Returns class name, id and dictionary attribute
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )
=======
    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
>>>>>>> 8a385a36cc34f3b9c8b3dc73802b4339e9ad1b4d

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        data = self.__dict__.copy()
        data["__class__"] = self.__class__.__name__
        data["created_at"] = self.created_at.isoformat()
        data["updated_at"] = self.updated_at.isoformat()
        return data
