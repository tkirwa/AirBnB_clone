#!/usr/bin/python3
"""
Import modules and packages.
Console module for the AirBnB clone project.
"""


import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Implementation of the command interpreter.
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """
        Called when an empty line + ENTER is entered.
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def help_quit(self):
        """
        Help message for quit command.
        """
        print("Quit command to exit the program.")

    def help_EOF(self):
        """
        Help message for EOF command.
        """
        print("EOF command to exit the program.")

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all instances or instances of a specific class.
        Usage: all [class name]
        """
        args = arg.split()
        objects = storage.all()

        if not args:
            print([str(obj) for obj in objects.values()])
            return

        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        print(
            [
                str(obj)
                for obj in objects.values()
                if type(obj).__name__ == args[0]
            ]
        )

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in storage.classes:
            print("** class doesn't exist **")
