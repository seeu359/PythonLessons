class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def points(self):
        return self.x, self.y


class Rectangle:
    def __init__(self, *obj):
        if len(obj) == 2:
            self.sp = obj[0]
            self.ep = obj[1]
        else:
            self.sp = Point(obj[0], obj[1])
            self.ep = Point(obj[2], obj[3])



rect2 = Rectangle(1, 2, 3, 4)
print(rect2.sp.points, rect2.ep.points)