# 1.
def matrix_max_index(M, m, n):
    max_elem = 0

    row = 0
    column = 0
    for i in range(0, m):
        for j in range(0, n):
            if M[i][j] > max_elem:
                max_elem = M[i][j]
                row = i
                column = j
    return (row, column)


M = [[0, 3, 2, 4], [2, 3, 5, 5],  [5, 1, 2, 3]]
print(matrix_max_index(M, 3, 4))

# 2.


def swap_columns(M, m, n, i, j):
    for x in range(0, m):
        M[x][i], M[x][j] = M[x][j], M[x][i]


M = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]
swap_columns(M, 3, 4, 0, 1)
print(M)

# 3.


def scale_matrix(M, m, n, c):
    import copy
    N = copy.deepcopy(M)
    for i in range(0, m):
        for j in range(0, n):
            N[i][j] = N[i][j] * c
    return N


M = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]
N = scale_matrix(M, 3, 4, 2)
print(M)
print(N)
