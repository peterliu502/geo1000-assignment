# GEO1000 - Assignment 3
# Authors: Zhenyu Liu, Haoyang Dong
# Studentnumbers: 5386586, 5302501


def read_grid(filenm):
    table = []
    with open(filenm) as file:
        for index, line in enumerate(file):
            if index % 2 == 1:
                txt = line.split()
                row = []
                for i in txt:
                    if i.isdigit():
                        # tens digit is x (row) , units digit is y (column)
                        row.append(((int(i))//10, (int(i)) % 10))
                table.append(row)
    return table


def visit(table, steps_allowed, path):
    # start at (0, 0)
    if len(path) == 0:
        path.append((0, 0))
    # if it find the treasure, return True
    if table[path[-1][0]][path[-1][1]] == path[-1]:
        return True
    # move on, allowed steps -1, and add the coordinate to path
    elif steps_allowed>1:
        path.append(table[path[-1][0]][path[-1][1]])
        return visit(table, steps_allowed-1, path)
    # failed to find a treasure
    else:
        return False


def hunt(filenm, max_steps):
    path = []
    if visit(read_grid(filenm), max_steps, path):
        return 'The treasure was found at row: {X}, column: {Y}; it took {N} steps to find the treasure.'.format(
            X=path[-1][0], Y=path[-1][1], N=len(path))
    else:
        return 'Could not find a treasure (in {N} steps).'.format(N=max_steps)


if __name__ == "__main__":
    print(hunt('finite.txt', 20))