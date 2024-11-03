# Assignment 1:
import math


class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = [" " * width for _ in range(height)]

    def print_canvas(self):
        def create_row_headers(length: int):
            return "".join([str(i % 10) for i in range(length)])

        header = " " + create_row_headers(self.width)
        print(header)
        for idx, row in enumerate(self.canvas):
            print(idx % 10, row, idx % 10, sep="")

        print(header)

    def draw_polygon(self, *points: tuple[int, int], closed: bool = True, line_char: str = "*"):
        def draw_line_segment(start: tuple[int, int], end: tuple[int, int], line_char: str = "*"):
            def replace_at_index(s: str, r: str, idx: int) -> str:
                return s[:idx] + r + s[idx + len(r):]

            x1, y1 = start
            x2, y2 = end

            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            sx = 1 if x1 < x2 else -1
            sy = 1 if y1 < y2 else -1
            error = dx - dy

            while x1 != x2 or y1 != y2:
                self.canvas[y1] = replace_at_index(self.canvas[y1], line_char, x1)

                double_error = error * 2
                if double_error > -dy:
                    error -= dy
                    x1 += sx

                if double_error < dx:
                    error += dx
                    y1 += sy

            self.canvas[y2] = replace_at_index(self.canvas[y2], line_char, x2)

        start_points = points[:-1]
        end_points = points[1:]

        if closed:
            start_points += (points[-1],)
            end_points += (points[0],)

        for start_point, end_point in zip(start_points, end_points):
            draw_line_segment(start_point, end_point, line_char)

    def draw_line(self, start: tuple[int, int], end: tuple[int, int], line_char: str = "*"):
        self.draw_polygon(start, end, closed=False, line_char=line_char)

    def draw_rectangle(self, upper_left: tuple[int, int], lower_right: tuple[int, int], line_char: str = "*"):
        x1, y1 = upper_left
        x2, y2 = lower_right

        self.draw_polygon(upper_left, (x2, y1), lower_right, (x1, y2), line_char=line_char)

    def draw_n_gon(self, center: tuple[int, int], radius: int, number_of_points: int, rotation: int = 0,
                   line_char: str = "*"):
        angles = range(rotation, 360 + rotation, 360 // number_of_points)

        points = []
        for angle in angles:
            angle_in_radians = math.radians(angle)
            x = center[0] + radius * math.cos(angle_in_radians)
            y = center[1] + radius * math.sin(angle_in_radians)
            points.append((round(x), round(y)))

        self.draw_polygon(*points, line_char=line_char)


# Example usage:
canvas = Canvas(100, 40)
canvas.draw_polygon((7, 12), (24, 29), (42, 15), (37, 32), (15, 35))
canvas.draw_line((10, 4), (92, 19), "+")
canvas.draw_rectangle((45, 2), (80, 27), '#')
canvas.draw_n_gon((72, 25), 12, 20, 80, "-")
canvas.print_canvas()



# Assignment 2

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x})/({self.y})"

    def __repr__(self):
        return str(self)

    def distance_from_origin(self) -> float:
        return math.sqrt(self.x **2 + self.y **2 )


class Shape(list):
    def __init__(self, *points: Point):
        super().__init__(points)

    def __repr__(self):
        return f"Shape([{', '.join(repr(point) for point in self)}])"

    def centroid(self) -> Point:
        if not self:
            return None

        total_x = sum(point.x for point in self)
        total_y = sum(point.y for point in self)
        n = len(self)
        return Point(total_x / n, total_y / n)

    def __eq__(self, other) -> bool:
        return self.centroid().distance_from_origin() == other.centroid().distance_from_origin()

    def __lt__(self, other) -> bool:
        return self.centroid().distance_from_origin() < other.centroid().distance_from_origin()

