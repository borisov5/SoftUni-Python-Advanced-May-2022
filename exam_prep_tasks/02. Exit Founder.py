first_player, second_player = input().split(', ')
one_player = first_player
two_player = second_player
matrix = []
for _ in range(6):
    matrix_row = input().split()
    matrix.append(matrix_row)

first_player_rest = False
second_player_rest = False

while True:
    row, col = input().split(', ')
    if first_player_rest:
        if one_player == first_player:
            first_player_rest = False
            first_player, second_player = second_player, first_player
            continue
    if second_player_rest:
        if two_player == first_player:
            second_player_rest = False
            first_player, second_player = second_player, first_player
            continue

    row = int(row[1:])
    col = int(col[:-1])

    if matrix[row][col] == 'E':
        print(f"{first_player} found the Exit and wins the game!")
        break
    elif matrix[row][col] == 'T':
        winner = second_player
        print(f"{first_player} is out of the game! The winner is {second_player}.")
        break
    elif matrix[row][col] == 'W':
        print(f"{first_player} hits a wall and needs to rest.")
        if one_player == first_player:
            first_player_rest = True
        elif two_player == first_player:
            second_player_rest = True

    first_player, second_player = second_player, first_player
