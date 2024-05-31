#!/usr/bin/python3
"""Module to defines a student by class Student"""


class Student:
    """Class that defines properties of student

    Attributes:
        first_name (str): first name of student
        last_name (int): last name of student
        age (int): age of student
    """

    def __init__(self, first_name, last_name, age):
        """Initialization  instances of student

        Args:
            first_name (str): first name of student
            last_name (int): last name of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of a Student"""
        return self.__dict__
