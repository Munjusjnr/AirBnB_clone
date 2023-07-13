#!/usr/bin/python3
"""Entry point for the command interpreter and the inclusion of modules"""
import cmd
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.user import User


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

    def do_create(self, arg):
        """This creates instance of a class.

        Arg:
            arg(str): This is a class name.
        """
        if arg == "":
            print("** class name missing **")

        elif arg != "BaseModel":
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

        elif info[0] != "BaseModel":
            print("** class doesn't exist **")

        elif len(info) < 2:
            print("** instance id missing **")

        elif len(info) == 2:
            for key in my_dict.keys():
                mid = key.split(".")
                if info[1] == mid[1]:
                    flag = 1
                    break
            if flag == 1:
                val = mid[0] + '.' + mid[1]
                print(my_dict[val])
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

        elif sep[0] != "BaseModel":
            print("** class doesn't exist **")

        elif len(sep) < 2:
            print("** instance id missing **")

        elif len(sep) == 2:
            for key in sto.keys():
                my_id = key.split(".")
                if sep[1] == my_id[1]:
                    flag = 1
                    break
            if flag == 1:
                val = my_id[0] + '.' + my_id[1]
                del sto[val]
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

        if arg != "BaseModel" and arg != "":
            print("** class doesn't exist **")

        else:
            for key in di.keys():
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

        elif info[0] != "BaseModel":
            print("** class doesn't exist **")

        elif len(info) < 2:
            print("** instance id missing **")

        elif len(info) == 2:
            for key in my_dict.keys():
                mid = key.split(".")
                if info[1] == mid[1]:
                    flag = 1
                    break
            if flag == 0:
                print("** no instance found **")

        elif len(info) < 3:
            print("** attribute name missing **")

        elif len(info) < 4:
            print("** value missing **")

        else:
            va = info[3].split('"')
            my_dict = my_dict[f"{info[0]}.{info[1]}"]
            my_dict.__dict__[info[2]] = va[1]
            my_dict.__dict__['updated_at'] = datetime.now()
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
