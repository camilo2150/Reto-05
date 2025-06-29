from .shape import Shape

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def compute_area(self):
        return self.side ** 2

    def compute_perimeter(self):
        return 4 * self.side
