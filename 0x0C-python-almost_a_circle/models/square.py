#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square."""
        return self.height
    @size.setter
    def size(self, value):
        """set the size of the Square."""
        self.width = value
        self.height = value
    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.height)

    def update(self, *args, **kwargs):
        """Update the Square
        Args:
            *args (int): New attribute value
                arg 0 is id
                arg 1 is size
                arg 2 is x
                arg 3 is y
            **kwargs (dict): New key/value pairs of attributes.
        """
        x = len(args)
        if x > 0 and x <= 4:
            if x >= 1:
                self.id = args[0]
            if x >= 2:
                self.size = args[1]
            if x >= 3:
                self.x = args[2]
            if x == 4:
                self.y = args[3]
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representaion of a square"""
        return {"id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y}
