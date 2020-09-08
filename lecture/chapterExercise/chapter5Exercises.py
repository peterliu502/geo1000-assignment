# Exercise 5.1
import time
now = int(time.time())
now_day = int(now // 86400)
now_hour = int((now % 86400) // 3600)
now_min = int((now % 86400 % 3600) // 60)
now_sec = int(now % 86400 % 3600 % 60)
print("It has been passed {0}days {1}hours {2}minutes {3}seconds since the epoch.".format(
    now_day, now_hour, now_min, now_sec
))


# Exercise 5.2.1
def check_fermat(a, b, c, n):
    if n > 2 and (a ** n + b ** n) == c ** n:
        print("Holy smokes, Fermat is wrong!")
    else:
        print("No, that doesn't work.")


# Exercise 5.2.2
def input_fermat_arg():
    arg_a = int(input("please input arg a:"))
    arg_b = int(input("please input arg b:"))
    arg_c = int(input("please input arg c:"))
    arg_n = int(input("please input arg n:"))
    return arg_a, arg_b, arg_c, arg_n


# check_fermat(*input_fermat_arg())

# Exercise 5.3.1
def is_triangle(a, b, c):
    if a + b <= c:
        print("No")
    elif b + c <= a:
        print("No")
    elif a + c <= b:
        print("No")
    else:
        print("Yes")


# Exercise 5.3.2
def input_stick_length():
    stick_a = int(input("please input stick a:"))
    stick_b = int(input("please input stick b:"))
    stick_c = int(input("please input stick c:"))
    return stick_a, stick_b, stick_c


is_triangle(*input_stick_length())
