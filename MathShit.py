import math

LAYSER_DISTANCE = 0.23


def distance_from_wall(left_x, left_y, right_x, right_y, screen_width=640, fov=0.5477):
    distance_between_dots = math.sqrt((left_x - right_x) ** 2 + (left_y - right_y) ** 2)
    angle_untill_dots = (distance_between_dots / screen_width) * fov
    distance_until_wall = (LAYSER_DISTANCE / (2 * math.tan(angle_untill_dots / 2)))
    return distance_until_wall
