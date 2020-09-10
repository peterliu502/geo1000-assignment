import math


# Exercise 7.1
def mysqrt(a):
    x = 1
    while True:
        y = (x + a / x) / 2
        if y == x:
            return x
        x = y


def test_square_root(a):
    print("{0:<13} {1:<13.11} {2:<13.11} {3:<13.11}".format(
        float(a), float(mysqrt(a)), float(math.sqrt(a)),
        float(abs(mysqrt(a) - math.sqrt(a)))
    ))


print("{0:<13} {1:<13} {2:<13} {3:<13}".format(
    "a", "mysqrt(a)", "math.sqrt(a)", "diff"
))
print("{0:<13} {1:<13} {2:<13} {3:<13}".format(
    "-------------", "-------------", "-------------", "-------------"
))
for i in range(9):
    test_square_root(i + 1)


# Exercise 7.2
def eval_loop():
    output = ""
    temp = ""
    while temp != "done":
        output += temp
        temp = input(">")
    return eval(output)


# print(eval_loop())


# Exercise 7.3
def factorial(num):
    if num > 1:
        num = num * factorial(num - 1)
    elif num == 0:
        num += 1
    return num


def estimate_pi():
    summation = 0
    k = 0
    while abs((2 * math.sqrt(2) * factorial(4 * k) * (1103 + 26390 * k))
              / (9801 * (factorial(k) ** 4) * (396 ** (4 * k)))) >= 1e-15:
        summation += \
            (2 * math.sqrt(2) * factorial(4 * k) * (1103 + 26390 * k)) \
            / (9801 * (factorial(k) ** 4) * (396 ** (4 * k)))
        k += 1
    return 1 / summation


print("estimate_pi() is ", estimate_pi(),
      "\ndiff between estimate_pi() and math.pi is ", abs(math.pi - estimate_pi()))
