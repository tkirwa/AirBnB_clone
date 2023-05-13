import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB command line interpreter."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_help(self, arg):
        """Help command to display available commands."""
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    # Add more command methods as needed

if __name__ == '__main__':
    HBNBCommand().cmdloop()
