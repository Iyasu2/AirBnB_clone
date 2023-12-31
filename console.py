#!/usr/bin/python3
'''
this module contains a class
where the command interpreter will
be built
'''
import cmd
import shlex
import models
import sys
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''
    this is the class HBNBCommand
    which inherits from cmd.Cmd
    that is a command line creating tool
    '''
    prompt = '(hbnb) '

    classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review}

    def do_quit(self, arg):
        '''
        Quit command to exit the program
        '''
        return True

    def do_EOF(self, arg):
        '''
        EOF command to exit the program
        '''
        print()
        return True

    def emptyline(self):
        '''
        doesn't execute when nothing is entered
        '''
        pass

    def do_create(self, argument):
        '''
        create a new instance, saves it and prints the id
        '''
        if argument:
            if argument in self.classes:
                get_class = getattr(sys.modules[__name__], argument)
                instance = get_class()
                models.storage.save()
                print(instance.id)
            else:
                print("** class doesn't exist **")
                return
        else:
            print("** class name missing **")
        return

    def do_show(self, argument):
        '''
        show string representation of an instance
        '''
        tokens = shlex.split(argument)
        if len(tokens) == 0:
            print("** class name missing **")
            return
        elif len(tokens) == 1:
            print("** instance id missing **")
            return
        elif tokens[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            obj_dict = models.storage.all()
            key_dict = tokens[0] + '.' + str(tokens[1])
            if key_dict in obj_dict:
                print(obj_dict[key_dict])
            else:
                print("** no instance found **")
        return

    def do_destroy(self, argument):
        '''
        deletes an instance
        '''
        tokens = shlex.split(argument)
        if len(tokens) == 0:
            print("** class name missing **")
            return
        elif len(tokens) == 1:
            print("** instance id missing **")
            return
        elif tokens[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            obj_dict = models.storage.all()
            key_dict = tokens[0] + '.' + str(tokens[1])
            if key_dict in obj_dict:
                del obj_dict[key_dict]
                models.storage.save()
            else:
                print("** no instance found **")
        return

    def do_all(self, argument):
        '''
        prints all the instances' string representation
        '''
        list_all = []
        tokens = shlex.split(argument)
        obj_dict = models.storage.all()

        if len(tokens) == 0:
            for key_dict in obj_dict:
                list_all.append(str(obj_dict[key_dict]))
            print(list_all)
            return

        if tokens[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            for key_dict in obj_dict:
                classname = key_dict.split('.')
                if classname[0] == tokens[0]:
                    list_all.append(str(obj_dict[key_dict]))
            print(list_all)
            return

    def do_update(self, argument):
        '''
        updates an instance
        '''
        tokens = shlex.split(argument)
        if len(tokens) == 0:
            print("** class name missing **")
            return
        elif len(tokens) == 1:
            print("** instance id missing **")
            return
        elif len(tokens) == 2:
            print("** attribute name missing **")
            return
        elif len(tokens) == 3:
            print("** value missing **")
            return
        elif tokens[0] not in self.classes:
            print("** class doesn't exist **")
            return
        obj_dict = models.storage.all()
        key_dict = tokens[0] + '.' + tokens[1]
        try:
            attr = type(getattr(obj_dict[key_dict], tokens[2]))
            tokens[3] = attr(tokens[3])
        except AttributeError:
            pass
        setattr(obj_dict[key_dict], tokens[2], tokens[3])
        models.storage.save()


if __name__ == '__main__':
    '''
    starts the loop if not imported
    '''
    HBNBCommand().cmdloop()
