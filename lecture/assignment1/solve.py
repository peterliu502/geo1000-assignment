# GEO1000 - Assignment 1
# Authors: Zhenyu Liu, Haoyang Dong
# Studentnumbers: 5386586, 5302501

from math import sqrt


def abc(a, b, c):
    if discriminant(a, b, c) > 0:
        root1 = (-b + sqrt(discriminant(a, b, c))) / (2 * a)
        root2 = (-b - sqrt(discriminant(a, b, c))) / (2 * a)
        print("The roots of {0} x^2 + {1} x + {2} are: \nx1 = {3} , x2 = {4}".format(a, b, c, root1, root2))
    elif discriminant(a, b, c) == 0:
        root0 = -b / (2 * a)
        if root0 == -0.0:
            root0 = 0.0
        print("The roots of {0} x^2 + {1} x + {2} are: \nx = {3}".format(a, b, c, root0))
    else:
        print("The roots of {0} x^2 + {1} x + {2} are: \nnot real".format(a, b, c))


def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


abc(2.0, 0.0, 0.0) 
abc(1.0, 3.0, 2.0)
abc(3.0, 4.5, 9.0)
