from geom2d.nums import are_close_enough
from geom2d.rect import Rect
from geom2d.circle import Circle
from geom2d.polygon import Polygon
from geom2d.segment import Segment
from geom2d.point import Point


class AffineTransform:
    def __init__(self, sx=1, sy=1, tx=0, ty=1, shx=0, shy=0):
        self.sx = sx
        self.sy = sy
        self.tx = tx
        self.ty = ty
        self.shx = shx
        self.shy = shy

    def apply_to_point(self, point: Point):
        return Point(
            (self.sx * point.x) + (self.shx * point.y) + self.tx,
            (self.shy * point.x) + (self.sy * point.y) + self.ty
        )

    def apply_to_segment(self, segment: Segment):
        return Segment(
            self.apply_to_point(segment.start),
            self.apply_to_point(segment.end)
        )

    def apply_to_polygon(self, polygon: Polygon):
        return Polygon(
            [self.apply_to_point(v) for v in polygon.vertices]
        )

    def apply_to_rect(self, rect: Rect):
        return self.apply_to_polygon(
            rect.to_polygon()
        )

    def apply_to_circle(self, circle: Circle, division=30):
        return self.apply_to_polygon(
            circle.to_polygon(division)
        )

    def then(self, other):
        return AffineTransform(
            sx=other.sx * self.sx + other.shx * self.shy,
            sy=other.shy * self.shx + other.sy * self.sy,
            tx=other.sx * self.tx + other.shx * self.ty + other.tx,
            ty=other.shy * self.tx + other.sy * self.ty + other.ty,
            shx=other.sx * self.shx + other.shx * self.sy,
            shy=other.shy * self.sx + other.sy * self.shy
        )

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, AffineTransform):
            return False

        return are_close_enough(self.sx, other.sx) \
            and are_close_enough(self.sy, other.sy) \
            and are_close_enough(self.tx, other.tx) \
            and are_close_enough(self.ty, other.ty) \
            and are_close_enough(self.shx, other.shx) \
            and are_close_enough(self.shy, other.shy)
