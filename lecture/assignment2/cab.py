# GEO1000 - Assignment 2
# Authors: Zhenyu Liu, Haoyang Dong
# Studentnumbers: 5386586, 5302501


def wiggle(start, end, moves):
    if moves == 0:
        if start == end:
            return 1
        else:
            return 0
    else:
        move_right = wiggle(start + 1, end, moves - 1)
        move_left = wiggle(start - 1, end, moves - 1)
        paths = move_right + move_left
        return paths


if __name__ == "__main__":
    print("running cab.py directly")
    print(wiggle(1, 4, 5))

