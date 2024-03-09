#!/usr/bin/python3
""" Console Module """
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """class for console py"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Exit method for quit typing """
        exit()

    def do_EOF(self, arg):
        """ Exit method for EOF """
        print('')
        exit()
if __name__ == "__main__":
    HBNBCommand().cmdloop()
