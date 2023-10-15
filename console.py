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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
