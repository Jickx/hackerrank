def diagonal_diff(matrix):
    diag = 0
    i = 0
    j = len(matrix) - 1
    while i < len(matrix):
        diag += matrix[i][i]
        diag -= matrix[i][j]
        i += 1
        j -= 1
    return abs(diag)


matrix = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]
expected = 15

print(diagonal_diff(matrix))
