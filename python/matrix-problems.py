def set_zeros(matrix):
    rows = set()
    cols = set()
    for col_i in range(len(matrix)):
        for row_i in range(len(matrix[0])):
            if matrix[col_i][row_i] == 0:
                rows.add(row_i)
                cols.add(col_i)

    for col in cols:
        matrix[col] = [0 for i in matrix[col]]

    for row in rows:
        for col_i in range(len(matrix[0])):
            matrix[col_i][row] = 0

    return matrix

print set_zeros([
    [2, 3, 0, 4],
    [0, 6, 3, 9],
    [3, 6, 8, 2],
    [3, 8, 2, 1]
])
