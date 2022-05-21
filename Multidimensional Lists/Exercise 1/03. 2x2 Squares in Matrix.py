def read_matrix():
    n, m = [int(x) for x in input().split()]
    matrix = []
    for _ in range(n):
        row = [x for x in input().split()]
        matrix.append(row)
    return matrix

matrix = read_matrix()
count = 0
for r in range(0, len(matrix) - 1):
    for c in range(0, len(matrix[0]) - 1):
        if matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
            count += 1

print(count)
