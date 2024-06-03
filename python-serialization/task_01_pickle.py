#!/usr/bin/python3


import pickle


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (OSError, pickle.PicklingError) as e:
            print(f"An error occurred while serializing: {e}")

    @classmethod
    def deserialize(cls, filename: str):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (OSError, pickle.UnpicklingError, EOFError) as e:
            print(f"An error occurred while deserializing: {e}")
            return None
