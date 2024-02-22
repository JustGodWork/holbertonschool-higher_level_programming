#!/usr/bin/python3

"""
Module named `Base` that contains the class `Base`.
"""


import json
import turtle


class Base:
    """This is the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []

        new_dictionary = []

        for object in list_objs:
            new_dictionary.append(object.to_dictionary())

        json_string = cls.to_json_string(new_dictionary)

        filename = cls.__name__ + ".json"

        with open(filename, "w", encoding="utf-8") as file:
            return (file.write(json_string))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(4, 2)
        if cls.__name__ == "Square":
            dummy = cls(42)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        objects = []

        try:
            with open(filename, "r", encoding="utf-8") as file:
                list_dicts = Base.from_json_string(file.read())
                for dictionary in list_dicts:
                    objects.append(cls.create(**dictionary))
                return objects

        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        screen = turtle.Screen()
        t = turtle.Turtle()
        t.speed(1)
        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.size)
                t.left(90)

        screen.exitonclick()
