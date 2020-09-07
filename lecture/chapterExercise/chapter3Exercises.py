# Exercise 3.1
def right_justify(s):
    output_str = (70 - len(s)) * " " + s
    print(output_str)


right_justify("monty")
right_justify("peterson")


# Exercise 3.2
def do_twice(f, *my_arg):
    f(*my_arg)
    f(*my_arg)
    print("")


def print_twice(bruce):
    print(bruce)
    print(bruce)
    print("")


def do_four(f, my_arg):
    do_twice(do_twice, f, my_arg)
    print("")


do_four(print_twice, "four")
do_twice(print_twice, "two")


# Exercise
def add_line(num):
    second_line = "|" + num * "     |"
    third_line = "+" + num * "  -  +"
    print(second_line)
    print(third_line)


def grid(num):
    # form the first line
    first_line = "+" + num * "  -  +"
    print(first_line)
    for i in range(num):
        add_line(num)
    print("")

grid(1)
grid(2)
grid(4)
grid(8)
grid(16)


