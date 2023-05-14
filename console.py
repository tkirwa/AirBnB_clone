#!/usr/bin/python3
"""Command interpreter for the AirBnB clone"""
import cmd
import shlex

import models


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it to JSON, and print the id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args[0])()
            models.storage.new(new_instance)
            models.storage.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instances = models.storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in instances:
            print(instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instances = models.storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in instances:
            del instances[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances"""
        args = shlex.split(arg)
        instances = models.storage.all()
        if len(args) == 0:
            print([str(value) for value in instances.values()])
        else:
            try:
                cls = eval(args[0])
            except NameError:
                print("** class doesn't exist **")
                return
            print(
                [
                    str(value)
                    for key, value in instances.items()
                    if key.split(".")[0] == args[0]
                ]
            )

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instances = models.storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in instances:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        attr_name = args[2]
        if hasattr(instances[key], attr_name):
            attr_value = args[3]
        attr_type = type(getattr(instances[key], attr_name))
        setattr(instances[key], attr_name, attr_type(attr_value))
        models.storage.save()

    def emptyline(self):
        """Handles empty lines"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def postloop(self):
        """Prints a new line after each command"""
        print()

    def do_help(self, arg):
        """Help command to display available commands"""
        cmd.Cmd.do_help(self, arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
