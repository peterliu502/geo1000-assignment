# GEO1000 - Assignment 2
# Authors: Zhenyu Liu, Haoyang Dong
# Studentnumbers: 5386586, 5302501


def parse(sudoku):
    if len(sudoku) != 16:
        return None
    elif not sudoku.isdigit():
        return None
    else:
        sudoku_structure = []
        sudoku_list = []
        for ch in sudoku:
            sudoku_list.append(int(ch))
        for row in range(4):
            sudoku_structure.append((sudoku_list[(row%4)*4], sudoku_list[(row%4)*4+1], sudoku_list[(row%4)*4+2], sudoku_list[(row%4)*4+3]))
        for col in range(4):
            sudoku_structure.append((sudoku_list[0*4+col], sudoku_list[1*4+col], sudoku_list[2*4+col], sudoku_list[3*4+col]))
        for box in range(4):
            sudoku_structure.append((sudoku_list[box//2*4+box*2], sudoku_list[box//2*4+box*2+1], sudoku_list[box//2*4+box*2+4], sudoku_list[box//2*4+box*2+5]))
        return sudoku_structure


def is_valid(sudoku_structure):
    for elm in sudoku_structure:
        # define a dictionary to record the times that numbers in the turple show
        valid_dict = {} 
        for j in elm:
            # if the number is new for the dictionary, give the value of the key 0, then +1; else the key value will +1
            valid_dict[j] = valid_dict.get(j, 0)+1
            # check if there are more than 1 of one number in the turple
            if valid_dict[j] > 1:
                return False
    return True


def main():
    print('Your sudoku for validation, or "quit" to exit.')
    words = input(">")
    while words != "quit":
        if parse(words) is None:
            print("Input not understood")
        else:
            if is_valid(parse(words)):
                print("This sudoku is *VALID*")
            else:
                print("This sudoku is *INVALID*")
        words = input(">")
    return


if __name__ == "__main__":
    main()
