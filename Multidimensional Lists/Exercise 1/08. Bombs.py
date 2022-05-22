def explode_bomb(r, c, mat, turns):
    bomb_size = mat[r][c]
    if bomb_size > 0:
        mat[r][c] = 0
        if c < turns - 1:
            if mat[r][c + 1] > 0:
                mat[r][c + 1] -= bomb_size
        if c > 0:
            if mat[r][c - 1] > 0:
                mat[r][c - 1] -= bomb_size
        if r < turns - 1:
            if mat[r + 1][c] > 0:
                mat[r + 1][c] -= bomb_size
        if r > 0:
            if mat[r - 1][c] > 0:
                mat[r - 1][c] -= bomb_size
        if c < turns - 1 and r > 0:
            if mat[r - 1][c + 1] > 0:
                mat[r - 1][c + 1] -= bomb_size
        if c < turns - 1 and r < turns - 1:
            if mat[r + 1][c + 1] > 0:
                mat[r + 1][c + 1] -= bomb_size
        if c > 0 and r < turns - 1:
            if mat[r + 1][c - 1] > 0:
                mat[r + 1][c - 1] -= bomb_size
        if c > 0 and r > 0:
            if mat[r - 1][c - 1] > 0:
                mat[r - 1][c - 1] -= bomb_size
    return mat


rows = int(input())
matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
coordinates = input().split()

alive_cells = 0
sum_of_cells = 0
for coord in coordinates:
    row, col = coord.split(',')
    matrix = explode_bomb(int(row), int(col), matrix, rows)

for row in matrix:
    for arg in row:
        arg = int(arg)
        if arg > 0:
            alive_cells += 1
            sum_of_cells += arg

print(f'Alive cells: {alive_cells}')
print(f'Sum: {sum_of_cells}')
for row_elements in matrix:
    print(' '.join([str(x) for x in row_elements]))
