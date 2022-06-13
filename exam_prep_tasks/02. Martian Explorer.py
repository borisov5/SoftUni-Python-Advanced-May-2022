from collections import deque

water_found = False
metal_found = False
concrete_found = False


def position(command, position):
    if command == 'up':
        if position[0] == 0:
            position[0] = 5
        else:
            position[0] -= 1
    elif command == 'down':
        if position[0] == 5:
            position[0] = 0
        else:
            position[0] += 1
    elif command == 'right':
        if position[1] == 5:
            position[1] = 0
        else:
            position[1] += 1
    elif command == 'left':
        if position[1] == 0:
            position[1] = 5
        else:
            position[1] -= 1


matrix = []
for _ in range(6):
    row = input().split(' ')
    matrix.append(row)

commands = deque(map(str, input().split(", ")))

current_position = []
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if matrix[row][column] == 'E':
            current_position = [row, column]

while commands:
    current_command = commands.popleft()

    current_row = current_position[0]
    current_column = current_position[1]

    position(current_command, current_position)

    if matrix[current_row][current_column] == 'W':
        print(f'Water deposit found at ({current_row}, {current_column})')
        water_found = True
    elif matrix[current_row][current_column] == 'M':
        print(f'Metal deposit found at ({current_row}, {current_column})')
        metal_found = True
    elif matrix[current_row][current_column] == 'C':
        print(f'Concrete deposit found at ({current_row}, {current_column})')
        concrete_found = True
    elif matrix[current_row][current_column] == 'R':
        print(f'Rover got broken at ({current_row}, {current_column})')
        break

if water_found and metal_found and concrete_found:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
