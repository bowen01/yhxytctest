import numpy as np

def Check_wholeGrid(grid):
    '''
    :param grid:
    :return: true if the grid is valid, else return false
    '''
    rows = len(grid)
    cols = len(grid[0])
    for i in range(1,rows):
        # print(i)
        for k in range(0,cols):
            if grid[i][k]==0 and grid[i-1][k]!=0:
                return False
    return True
grid = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 4, 0, 0, 0, 0, 0],
                 [0, 0, 2, 0, 0, 0, 0, 0],
                 [3, 3, 3, 0, 0, 2, 2, 1],
                 [2, 1, 3, 1, 3, 2, 2, 1]])

print(Check_wholeGrid(grid))