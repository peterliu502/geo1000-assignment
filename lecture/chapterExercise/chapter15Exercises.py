import copy

class Point:
    """
    represent a point in 2-D space
    attributions: x, y
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Exercise 15.0.1
    def distance(self, p2):
        return ((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2) ** (1/2)


print(Point(1, 1).distance(Point(0, 0)))


class Rectangle:
    """
    represent a rectangle with a corner point, height and width.
    attributions: corner point, height, width
    """
    def __init__(self, corner, height, width):
        self.corner = corner
        self.height = height
        self.width = width
        self.center = Point(self.corner.x + width / 2, self.corner.x + height / 2)

    # Exercise 15.0.2
    def move_rectangle(self, delta_x, delta_y):
        self.corner.x += delta_x
        self.corner.y += delta_y

    # Exercise 15.0.3
    def move_rectangle_copy(self, delta_x, delta_y):
        return Rectangle(Point(self.corner.x + delta_x, self.corner.y + delta_y), self.width, self.height)


# Exercise 15.1
class Circle:
    """
    Use a center point and a radius to represent a circle
    attributions: center point, radius
    """
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def point_in_circle(self, point):
        if ((self.center.x - point.x) ** 2 + (self.center.y - point.y) ** 2) ** (1/2) <= self.radius:
            return True
        else:
            return False

    def rect_in_circle(self, rectangle):
        p1 = Point(rectangle.corner.x, rectangle.corner.y)
        p2 = Point(rectangle.corner.x + rectangle.width, rectangle.corner.y)
        p3 = Point(rectangle.corner.x, rectangle.corner.y + rectangle.height)
        p4 = Point(rectangle.corner.x + rectangle.height, rectangle.corner.y + rectangle.width)
        for point in [p1, p2, p3, p4]:
            if not self.point_in_circle(point):
                return False
        return True

    def rect_circle_overlap(self, rectangle):
        vector_v = (abs(rectangle.center.x - self.center.x),
                    abs(rectangle.center.y - self.center.y))
        vector_h = (rectangle.center.x, rectangle.center.y)
        diff_v_h = (vector_v[0] - vector_h[0], vector_v[1] - vector_h[1])
        if diff_v_h[0] < 0:
            diff_v_h = (0, diff_v_h[1])
        if diff_v_h[1] < 0:
            diff_v_h = (diff_v_h[0], 0)
        if (diff_v_h[0] ** 2 + diff_v_h[1] ** 2) < (self.radius ** 2):
            return True
        else:
            return False


if __name__ == "__main__":
    shape1 = Rectangle(Point(0, 0), 1, 1)
    shape1.move_rectangle(1, 2)
    shape2 = shape1.move_rectangle_copy(-1, -1)
    shape3 = Circle(Point(150, 100), 75)
    print(str(shape1.corner.x) + ", " + str(shape1.corner.y) + " " + str(shape2.corner.x) + ", " + str(shape2.corner.y))
    print(shape3.point_in_circle(Point(0, 0)),
          shape3.point_in_circle(Point(100, 100)),
          shape3.rect_in_circle(shape1),
          shape3.rect_in_circle(shape1.move_rectangle_copy(150, 100)))
    print(shape3.rect_circle_overlap(shape1),
          shape3.rect_circle_overlap(shape1.move_rectangle_copy(150, 100)),
          shape3.rect_circle_overlap(Rectangle(Point(0, 0), 10000, 10000)))
