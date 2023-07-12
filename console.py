#!/usr/bin/python3
"""Entry point for the command interpreter and the inclusion of modules"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class denotes the command interpreter for a website clone"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """A command to exit the command interpreter"""
        raise SystemExit

    def do_EOF(self, args):
        """Recognizing end of line when command interpreter is executed"""
        return True

    def do_help(self, args):
        """Help command"""
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """When nothing is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
