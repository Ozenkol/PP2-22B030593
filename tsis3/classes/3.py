class Shape:

    def area(self):
        return 0

    class Square:

        def __init__(self, length):
            self.length = length

        def area(self):
            return self.length**2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


shape = Rectangle(5,6)
print(shape.area())
