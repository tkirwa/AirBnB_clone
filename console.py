#!/usr/bin/env python3
"""
Console module for the AirBnB clone
"""

import cmd
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models import storage
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Command line interpreter for the AirBnB clone
    """
    valid_classes = ["BaseModel"]

    prompt = '(hbnb) '

    def emptyline(self):
        """Override the emptyline method"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file),
        and prints the id.
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        else:
            dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'City': City, 'Amenity': Amenity, 'State': State,
                   'Review': Review}
            my_model = dct[arg]()
            print(my_model.id)
            my_model.save()

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_instances = storage.all()
        instance = all_instances.get(key)
        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_instances = storage.all()
        instance = all_instances.get(key)
        if instance:
            del all_instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        all_instances = storage.all()
        objects = []
        if arg:
            if arg not in globals():
                print("** class doesn't exist **")
                return
            for key, obj in all_instances.items():
                if arg == key.split(".")[0]:
                    objects.append(str(obj))
        else:
            for obj in all_instances.values():
                objects.append(str(obj))
        print(objects)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_instances = storage.all()
        instance = all_instances.get(key)
        if instance is None:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute = args[2]
        value = args[3]
        if hasattr(instance, attribute):
            try:
                value = eval(value)
            except (NameError, SyntaxError):
                pass
            setattr(instance, attribute, value)
            storage.save()
        else:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
