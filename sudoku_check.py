"""In this module I check sudoku squares"""

def check_value(val, sqaure_size):
    if not isinstance(val, int):
        return False
    if not (0 < val <= sqaure_size):
        return False
    return True


def check_sudoku(square_list):
    flag = False
    n = len(square_list)
    # checking rows
    for row in square_list:
        flag = all(check_value(val, n) for val in row)
        if not flag:
            return flag
        if len(set(row)) != n:
            return False

    # checking columns
    for i in range(n):
        column_values = [row[i] for row in square_list]
        flag = all(check_value(val, n) for val in column_values)
        if not flag:
            return flag
        if len(set(column_values)) != n:
            return False

    return flag



if __name__ == "__main__":
    test1 = check_sudoku([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    test2 = check_sudoku([[1, 1, 4, 4], [1, 1, 4, 4], [4, 4, 1, 1], [4, 4, 1, 1]])

    print("end")