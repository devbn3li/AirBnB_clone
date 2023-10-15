#!/usr/bin/python3
"""
command interpreter using cmd module
"""


import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """class cmd"""

    prompt = '(hbnb) '
    classes = ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity',
               'Review']

    def do_quit(self, line):
        """Quit to exit the program"""

        return True

    def do_EOF(self, line):
        """EOF to exit the program"""

        print()
        return True

    def emptyline(self):
        """
        empty line command to execute anything
        """

        pass

    def do_create(self, line):
        """Creates new instance"""

        if line:
            if line not in HBNBCommand.list_of_classes:
                print("** class doesn't exist **")
            else:
                instance = eval(f"{line}()")
                instance.save()
                print(instance.id)
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Prints the string representation of \
            an instance based on the class name and id"""

        if line:
            ls_line = line.split(" ")
            if ls_line[0] not in HBNBCommand.list_of_classes:
                print("** class doesn't exist **")
            elif len(ls_line) == 1:
                print("** instance id missing **")
            elif ls_line[1]:
                dic = storage.all()
                flagg = 0
                for key, value in dic.items():
                    if f"{ls_line[0]}.{ls_line[1]}" == key:
                        print(value)
                        flagg = 1
                        break
                if flagg == 0:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        kwargs = HBNBCommand.__parse(line)

        if not kwargs:
            return

        if not kwargs['cls_name']:
            print("** class name missing **")
            return

        if kwargs['cls_name'] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not kwargs['id']:
            print("** instance id missing **")
            return

        try:
            del storage.all()[f"{kwargs['cls_name']}.{kwargs['id']}"]
            storage.save()
        except KeyError:
            print("** no instance found **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
