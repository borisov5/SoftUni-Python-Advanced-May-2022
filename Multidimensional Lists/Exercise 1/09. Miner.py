def make_move(position, turn, size):
    if turn == "up":
        if position[0] > 0:
            position[0] -= 1
    elif turn == "down":
        if position[0] < size - 1:
            position[0] += 1
    elif turn == "right":
        if position[1] < size - 1:
            position[1] += 1
    elif turn == "left":
        if position[1] > 0:
            position[1] -= 1
    return position


def get_starting_position(size):
    miner_coord = []
    coal = 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == "s":
                miner_coord = [r, c]
            if matrix[r][c] == "c":
                coal += 1
    return miner_coord, coal


square_field_size = int(input())
commands = input().split()
matrix = []
for row in range(square_field_size):
    matrix.append(input().split())

collected_coals = 0
end_of_route_found = False
position = get_starting_position(square_field_size)[0]
coals = get_starting_position(square_field_size)[1]
matrix[position[0]][position[1]] = "*"
coord = (0, 0)

for move in commands:
    coord = make_move(position, move, square_field_size)

    if matrix[coord[0]][coord[1]] == "*":
        continue
    elif matrix[coord[0]][coord[1]] == "c":
        collected_coals += 1
        matrix[coord[0]][coord[1]] = "*"
        if collected_coals == coals:
            print(f'You collected all coal! {(coord[0], coord[1])}')
            end_of_route_found = True
            break
    elif matrix[coord[0]][coord[1]] == "e":
        print(f'Game over! {(coord[0], coord[1])}')
        end_of_route_found = True
        break

coals_left = coals - collected_coals
if not end_of_route_found:
    print(f'{coals_left} pieces of coal left. {(coord[0], coord[1])}')
