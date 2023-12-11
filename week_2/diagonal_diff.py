def diagonal_diff(matrix):
        diag = [matrix[i][i] - matrix[i][len(matrix) - i - 1] for i in range(len(matrix))]
        return abs(sum(diag))


matrix = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]
expected = 15

print(diagonal_diff(matrix))
