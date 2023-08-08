#!/usr/bin/python3
'''
this module contains a class
where the command interpreter will
be built
'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''
    this is the class HBNBCommand
    which inherits from cmd.Cmd
    that is a command line creating tool
    '''
    prompt = '(hbnb) '

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


if __name__ == '__main__':
    '''
    starts the loop if not imported
    '''
    HBNBCommand().cmdloop()
