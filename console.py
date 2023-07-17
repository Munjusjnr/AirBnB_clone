#!/usr/bin/python3
"""Entry point for the command interpreter and the inclusion of modules"""
import cmd
import re
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """This class denotes the command interpreter for a website clone"""
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "Review", "State", "City", "Amenity",
               "Place"]

    def do_quit(self, args):
        """A command to exit the command interpreter"""
        return True

    def do_EOF(self, args):
        """Recognizing end of line when command interpreter is executed"""
        return True

    def do_help(self, args):
        """Help command"""
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """When nothing is entered"""
        pass

    def onecmd(self, line):
        """Every command passes here before getting to their functions"""
        command, args, line = self.parseline(line)

        if not line:
            return self.emptyline()

        if command is None:
            return self.default(line)

        self.lastcommand = line
        if command == '':
            return self.default(line)

        else:
            try:
                line1 = line.replace("()", "")
                my_list = line1.split(".")
                meth = getattr(self, 'do_' + my_list[1])
                return meth(my_list[0])
            except Exception as e:
                pass
            try:
                func = getattr(self, 'do_' + command)
            except AttributeError:
                return self.default(line)
            return func(args)


    def do_create(self, arg):
        """This creates instance of a class.

        Arg:
            arg(str): This is a class name.
        """
        if arg == "":
            print("** class name missing **")

        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")

        else:
            newbase = eval(arg)()
            newbase.save()
            print(f"{newbase.id}")

    def do_show(self, arg):
        """This prints the string representation of an instance
        based on the class name and id.

        Arg:
            arg(str): This is a class name.
        """
        info = arg.split()
        my_dict = storage.all()
        flag = 0

        if arg == "":
            print("** class name missing **")

        elif info[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")

        elif len(info) < 2:
            print("** instance id missing **")

        elif len(info) == 2:
            for key in my_dict.keys():
                given_inst = info[0] + '.' + info[1]
                if given_inst == key:
                    flag = 1
                    break
            if flag == 1:
                print(my_dict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """This deletes an instance based on the class name and id.

        Arg:
            arg(str): This is a class name.
        """
        sep = arg.split()
        sto = storage.all()
        flag = 0

        if arg == "":
            print("** class name missing **")

        elif sep[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")

        elif len(sep) < 2:
            print("** instance id missing **")

        elif len(sep) == 2:
            for key in sto.keys():
                given_inst = sep[0] + '.' + sep[1]
                if given_inst == key:
                    flag = 1
                    break
            if flag == 1:
                del sto[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """This prints all string representation of all
        instances based or not on the class name.

        Arg:
            arg(str): This is a class name.
        """
        my_list = []
        di = storage.all()

        if arg not in HBNBCommand.classes and arg != "":
            print("** class doesn't exist **")

        else:
            for key in di.keys():
                if arg in key:
                    my_list.append(f"{di[key]}")

            print(my_list)

    def do_update(self, arg):
        """This updates an instance based on the class name and
        id by adding or updating attribute.

        Arg:
            arg(str): This is a class name.
        """
        info = arg.split()
        my_dict = storage.all()
        flag = 0

        if arg == "":
            print("** class name missing **")

        elif info[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")

        elif len(info) < 2:
            print("** instance id missing **")

        elif len(info) >= 2:
            for key in my_dict.keys():
                given_inst = info[0] + '.' + info[1]
                if given_inst == key:
                    flag = 1
                    break
            if flag == 0:
                print("** no instance found **")

            elif len(info) < 3:
                print("** attribute name missing **")

            elif len(info) < 4:
                print("** value missing **")

            else:
                va = info[3].replace('"', "")
                my_dict = my_dict[f"{info[0]}.{info[1]}"]
                try:
                    typ = type(my_dict.__class__.__dict__[info[2]])
                    my_dict.__dict__.update({info[2]: typ(va)})
                except KeyError:
                    my_dict.__dict__.update({info[2]: va})
                my_dict.__dict__['updated_at'] = datetime.now()
                storage.save()

    def do_count(self, arg):
        count = 0
        my_dict = storage.all()

        for key, val in my_dict.items():
            classname = key.split(".")
            if arg == classname[0]:
                count += 1

        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
