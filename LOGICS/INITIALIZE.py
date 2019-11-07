import random


def start_game():
    mat = []
    for _ in range(4):
        mat.append([0] * 4)
    return mat


def add_new(mat):
    row = random.randint(0, 3)
    column = random.randint(0, 3)
    while mat[row][column] != 0:
        row = random.randint(0, 3)
        column = random.randint(0, 3)
    mat[row][column] = 2
    return


def current_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'

    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'GAME NOT OVER'
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]:
                return 'GAME NOT OVER'

    for j in range(3):
        if mat[3][j] == mat[3][j + 1]:
            return "GAME NOT OVER"

    for i in range(3):
        if mat[i][3] == mat[i + 1][3]:
            return 'GAME NOT OVER'

    return 'LOST'
