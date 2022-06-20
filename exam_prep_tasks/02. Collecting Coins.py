def get_starting_position(m, size):
    for row in range(size):
        for col in range(size):
            if m[row][col] == 'P':
                coords = [row, col]
                return coords


def move(destination, coords, size):
    def out_of_the_field(value, num):
        if value < 0:
            value = num - 1
        elif value == num:
            value = 0
        return value

    row = coords[0]
    col = coords[1]
    if destination == 'up':
        row -= 1
        row = out_of_the_field(row, size)
    elif destination == 'down':
        row += 1
        row = out_of_the_field(row, size)
    elif destination == 'right':
        col += 1
        col = out_of_the_field(col, size)
    elif destination == 'left':
        col -= 1
        col = out_of_the_field(col, size)

    coords = [row, col]
    return coords


def win_a_game(points):
    if points >= 100:
        return True
    return False


def hit_a_wall(board, coords):
    row = coords[0]
    col = coords[1]
    if board[row][col] == 'X':
        return True
    return False


def colect_coins(board, coords):
    row = coords[0]
    col = coords[1]
    additional_coins = 0
    if board[row][col] != 'P' and board[row][col] != 'X':
        additional_coins = int(board[row][col])
        board[row][col] = 0
    return additional_coins, board


size_of_the_field = int(input())
matrix = [input().split(' ') for _ in range(size_of_the_field)]
your_path = []
total_coins = 0

coordinates = get_starting_position(matrix, size_of_the_field)
your_path.append(coordinates)


while True:
    command = input()
    coordinates = move(command, coordinates, size_of_the_field)
    your_path.append(coordinates)

    current_coins, matrix = colect_coins(matrix, coordinates)
    total_coins += current_coins

    if hit_a_wall(matrix, coordinates):
        total_coins /= 2
        win_a_game = False
        break

    if win_a_game(total_coins):
        break

if win_a_game:
    print(f"You won! You've collected {int(total_coins)} coins.")
else:
    print(f"Game over! You've collected {int(total_coins)} coins.")

print('Your path:')
print("\n".join(str(x) for x in your_path))