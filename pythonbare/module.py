#!/usr/bin/env python3
"""
This is my barebone python package.
It just prints a string when called
It can be installed with pip install . or pip install -e .
Tests can be done with python3 setup.py test
And code formatting checking with python3 setup.py flake8
"""

def print_string():
    print("min python program")

if __name__ == "__main__":
    print_string()