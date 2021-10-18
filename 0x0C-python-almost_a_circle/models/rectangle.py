#!/usr/bin/python3
"""
Create inherents class of Base
"""

from .base import Base


class Rectangle(Base):
    """New rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initiallize attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width property"""
        return (self.__width)

    @width.setter
    def width(self, width):
        """Width Setter"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Height property"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """Height Setter"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """x property"""
        return (self.__x)

    @x.setter
    def x(self, x):
        """x Setter"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """y property"""
        return (self.__y)

    @y.setter
    def y(self, y):
        """y setter"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """Area of rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Display rectangle"""
        for i in range(self.__y):
            print("")
        for column in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for row in range(self.__width - 1):
                print('#', end="")
            print('#')

    def __str__(self):
        """String representation"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Updating data"""
        if len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Create a dictionary"""
        dictionary = {}
        dictionary['x'] = self.x
        dictionary['y'] = self.y
        dictionary['id'] = self.id
        dictionary['height'] = self.height
        dictionary['width'] = self.width
        return dictionary
