#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Sets the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Gets the width of the Rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x coordinate of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x coordinate of the Rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y coordinate of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y coordinate of the Rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Gets the area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """prints the rectangle using #"""
        for i in range(self.y):
            print("")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """Return the print and str representation of rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the Rectangle
        Args:
            *args (int): New attribute value
                arg 0 is id
                arg 1 is width
                arg 2 is height
                arg 3 is x
                arg 4 is y
            **kwargs (dict): New key/value pairs of attributes.
        """
        x = len(args)
        if x > 0 and x <= 5:
            if x >= 1:
                self.id = args[0]
            if x >= 2:
                self.width = args[1]
            if x >= 3:
                self.height = args[2]
            if x >= 4:
                self.x = args[3]
            if x == 5:
                self.y = args[4]
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of a rectangle"""
        return {"x": self.x,
                "y": self.y,
                "id": self.id,
                "height": self.height,
                "width": self.width}
