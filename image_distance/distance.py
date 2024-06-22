import math

def calculate_distances(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    x_distance = abs(x2 - x1)
    y_distance = abs(y2 - y1)
    return distance, x_distance, y_distance

def calculate_real_distances(distance, x_distance, y_distance, mm_per_pixel):
    real_distance = distance * mm_per_pixel
    real_x_distance = x_distance * mm_per_pixel
    real_y_distance = y_distance * mm_per_pixel
    return real_distance, real_x_distance, real_y_distance
