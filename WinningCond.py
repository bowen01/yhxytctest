import numpy as np

def check_continuous_element(row, value):
    count = 0
    for x in row:
        if x == value:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    return False


def check_winning(grid):
    '''
    :param grid: a 2d numpy array
    :return: (flag, [0,0,0,0])
    flag:
    the flag means whether some role wins, ture = someone wins, false means no one wins.
    eg: check_winning(grid)[0] return ture or false for some if-else statement in the future

    array[]:the array indicates the details you need.
    includes 0 0r 1 means lose or win.
    array[0]-array[3] represent, Red_Color,White_Color,Black_Dot,White_Dot, respectively.
    eg:check_winning(grid)[1] might return [1, 0, 1, 0] means someone wins, and Red_Color,Black_Dot win.

    eg:(True, [1, 0, 1, 0]) means someone wins, and Red_Color,Black_Dot win.
    )
    '''
    winning_flag = False
    #the third value is to check and record whether each item wins. 1 = win 0 = not win
    winning_conditions = {'Red_Color':   [1, 2, 0],
                          'White_Color': [3, 4, 0],
                          'Black_Dot':   [1, 3, 0],
                          'White_Dot':   [2, 4, 0]}
    # TODO: Optimization, multi-threading
    # check each winning condition
    for key, item in winning_conditions.items():
        # change winning pair to -1
        replace_value = -1
        grid1 = np.where(grid == item[0], replace_value, grid)
        grid1 = np.where(grid1 == item[1], replace_value, grid1)

        # check horizontal and vertical
        for matrix in [grid1, np.transpose(grid1)]:
            for row in matrix:
                if check_continuous_element(row, value=replace_value):
                    # you can delete the print
                    # print("{} Won!".format(key))
                    winning_conditions[key][2] = 1
                    winning_flag = True
                # check diagonal and reverse diagonal
        for matrix in [grid1, np.fliplr(grid1)]:
            for k in range(-8, 5):
                if check_continuous_element(np.diag(matrix, k=k), value=replace_value):
                    # you can delete the print
                    # print("{} Won!".format(key))
                    winning_conditions[key][2] = 1
                    winning_flag = True

    results = [winning_conditions[key][2] for key in winning_conditions]
    return winning_flag, results


def __main__():
    # grid = np.random.randint(5, size=(12, 8))
    grid = np.array([[0, 2, 0, 3, 0, 1, 0, 0],
                     [0, 2, 1, 0, 3, 4, 0, 0],
                     [0, 0, 3, 0, 0, 0, 0, 0],
                     [0, 0, 3, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 0, 1, 0, 0, 0, 4],
                     [4, 0, 0, 0, 2, 0, 0, 0],
                     [2, 3, 0, 0, 0, 2, 0, 0],
                     [3, 0, 0, 0, 0, 0, 2, 0],
                     [0, 0, 0, 1, 0, 2, 0, 0],
                     [0, 3, 0, 0, 0, 0, 0, 1],
                     [0, 1, 3, 1, 3, 0, 0, 0]])
    print(grid)
    results1 = check_winning(grid)

    print("just results[0]")
    print(check_winning(grid)[0])
    print("just results[1]")
    print(check_winning(grid)[1])
    print("whole result")
    print(check_winning(grid))


if __name__ == "__main__":
    __main__()


