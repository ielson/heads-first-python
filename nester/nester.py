#!/usr/bin/env python3
"""
This is my barebone python package.
It just prints a string when called
It can be installed with pip install . or pip install -e .
Tests can be done with python3 setup.py test
And code formatting checking with python3 setup.py flake8
"""


def print_lol(the_list, level):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, level+1)
        else:
            for tab_stop in range(level):
                print("\t", end="")
            print(each_item)


if __name__ == "__main__":
    movies = ['The Holy Grail', 1975, 'Terry Johnes & Terry Gilliam', 91,
                ['Graham Chapman', ['John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]
    print_lol(movies, 0)
