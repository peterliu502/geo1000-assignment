# GEO1000 - Assignment 1
# Authors: Zhenyu Liu, Haoyang Dong
# Studentnumbers: 5386586, 5302501

import math


# To calculate the distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# To calculate the area of a triangle using Heron's formula
def heron(a, b, c):
    half_sides_lengths = (a + b + c) / 2
    return math.sqrt(half_sides_lengths * (half_sides_lengths - a) * (half_sides_lengths - b) * (half_sides_lengths - c))


# To caclulate the angle which is opposite of side c
def angle(a, b, c):
    return math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))


def segment_point_dist(s1x, s1y, s2x, s2y, px, py):
    distance_s1s2 = distance(s1x, s1y, s2x, s2y)
    distance_s1p = distance(s1x, s1y, px, py)
    distance_s2p = distance(s2x, s2y, px, py)
    list_sides_lengths = [distance_s1s2, distance_s1p, distance_s2p]
    list_sides_lengths.sort()
    # Test whether these three points can form a triangle
    if list_sides_lengths[0] + list_sides_lengths[1] == list_sides_lengths[2]:  
        # Judge if the point is on the finite line or equal to s1 or s2
        if max([distance_s1p, distance_s2p]) <= distance_s1s2:    
            return 0    # if true, the distance will be 0
        else:
            return min([distance_s1p, distance_s2p])    # Otherwise, the distance is equal to the shorter one in s1p and s2p
    # Test whether Arc_s1 is obtuse.
    elif angle(distance_s1s2, distance_s1p, distance_s2p) > math.pi / 2:  
        return distance_s1p 
    # Test whether Arc_s2 is obtuse.
    elif angle(distance_s1s2, distance_s2p, distance_s1p) > math.pi / 2:  
        return distance_s2p
    # A right or acute triangle
    else:  
        return 2 * heron(distance_s1s2, distance_s1p, distance_s2p) / distance_s1s2    # The height of the triangle


if __name__ == "__main__":
    print(segment_point_dist(0, 0, 10, 0, 5, 10))
    print(segment_point_dist(0, 0, 10, 0, 20, 0))
    print(segment_point_dist(0, 0, 10, 0, -10, -10))
    print(segment_point_dist(0, 0, 10, 10, 0, 10))
