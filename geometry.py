class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def is_Left(a : Point,b : Point,c : Point):
     return ((a.x - b.x)*(c.y - b.y) - (a.y - b.y)*(c.x - b.x)) > 0;


class Polygon:
    def __init__(self, p0, p1, p2, p3):
        self.points = [p0, p1, p2, p3]
        self.vertices = [[p0.x, p0.y], [p1.x, p1.y], [p2.x, p2.y], [p3.x, p3.y]]
        self.centroid = [(self.vertices[0][0] + self.vertices[2][0]) // 2,
                         (self.vertices[0][1] + self.vertices[3][1]) // 2]

    def encloses_point(self, point: Point):
        return is_Left(self.points[0], self.points[1], point) and is_Left(self.points[1], self.points[2], point) and \
        is_Left(self.points[2], self.points[3], point) and is_Left(self.points[3], self.points[0], point)
