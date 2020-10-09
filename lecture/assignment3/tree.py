# GEO1000 - Assignment 3
# Authors: Zhenyu Liu, Haoyang Dong
# Studentnumbers: 5386586, 5302501
import math


def distance(p1, p2):
    """Returns Cartesian distance (as float) between two 2D points"""
    return math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)


def point_angle_distance(pt, beta, distance):
    """Compute new point that is distance away from pt in direction beta"""
    return pt[0]+math.cos(beta)*distance, pt[1]+math.sin(beta)*distance


def absolute_angle(p1, p2):
    """Returns the angle (in radians) between the positive x-axis 
    and the line through two given points, p1 and p2"""
    return math.atan2(p2[1]-p1[1], p2[0]-p1[0])


def opposite_edge(p1, p2):
    """Compute edge parallel to the edge defined by the two given points 
    p1 and p2 (i.e. the opposite edge in the square).
    """
    p4 = point_angle_distance(p1, absolute_angle(p1, p2)+math.radians(90), distance(p1, p2))
    p3 = point_angle_distance(p4, absolute_angle(p1, p2), distance(p1, p2))
    return p3, p4


def split_point(p1, p2, alpha):
    """Returns the point above this top edge that defines 
    the two new boxes (together with points p1 and p2 of the top edge).
    """
    return point_angle_distance(p1, alpha+absolute_angle(p1, p2), distance(p1, p2)*math.cos(alpha))


def as_wkt(p1, p2, p3, p4):
    """Returns Well Known Text string (POLYGON) for 4 points 
    defining the square
    """
    return 'POLYGON (({} {}, {} {}, {} {}, {} {}, {} {}))'.format(
        p1[0], p1[1], p2[0], p2[1], p3[0], p3[1], p4[0], p4[1], p1[0], p1[1])


def draw_pythagoras_tree(p1, p2, alpha, currentorder, totalorder, filename):
    p3, p4 = opposite_edge(p1, p2)
    p5 = split_point(p4, p3, alpha)
    area = distance(p1, p2) ** 2
    with open(filename, 'a') as file:
        file.write(as_wkt(p1, p2, p3, p4)+';{};{}'.format(currentorder, area)+'\n')
    if totalorder > 0:
        draw_pythagoras_tree(p4, p5, alpha, currentorder+1, totalorder-1, filename)
        draw_pythagoras_tree(p5, p3, alpha, currentorder+1, totalorder-1, filename)


if __name__ == "__main__":
    with open('out.wkt', 'w') as fh:  # 'with' statement closes 
                                      # file automatically
        fh.write("geometry;currentorder;area\n")
    draw_pythagoras_tree(p1=(5,0), 
        p2=(6,0), 
        alpha=math.radians(45),
        currentorder=0,
        totalorder=6,
        filename='out.wkt')


