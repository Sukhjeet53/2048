def compress(mat):
    new_mat = [[0] * 4 for _ in range(4)]
    changed = False
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1
    return new_mat, changed
