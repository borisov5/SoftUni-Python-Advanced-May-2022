def take_position(mat, r, c):
    all_decorations = 0
    all_gifts = 0
    all_cookies = 0
    for row in range(r):
        for col in range(c):
            if mat[row][col] == "Y":
                r, c = row, col
            elif mat[row][col] == "D":
                all_decorations += 1
            elif mat[row][col] == "G":
                all_gifts += 1
            elif mat[row][col] == "C":
                all_cookies += 1
    return r, c, all_decorations, all_gifts, all_cookies


def change_position(r, c, rows, cols, dest):
    if dest == "right":
        c += 1
        if c > cols - 1:
            c = 0
    elif dest == "left":
        c -= 1
        if c < 0:
            c = cols - 1
    elif dest == "up":
        r -= 1
        if r < 0:
            r = rows - 1
    elif dest == "down":
        r += 1
        if r > rows - 1:
            r = 0
    return r, c


def check(found_d, found_g, found_c, all_d, all_g, all_c):
    if found_d == all_d and found_g == all_g and found_c == all_c:
        return True
    return False


rows, cols = input().split(", ")
rows, cols = int(rows), int(cols)

matrix = []
for _ in range(int(rows)):
    row = input().split()
    matrix.append(row)

command = input()
position_row, position_col, all_decorations, all_gifts, all_cookies = take_position(matrix, rows, cols)
matrix[position_row][position_col] = "x"

number_of_decoration = 0
number_of_gifts = 0
number_of_cookies = 0

while command != "End":
    destination, steps = command.split("-")
    for _ in range(int(steps)):
        position_row, position_col = change_position(position_row, position_col, rows, cols, destination)
        if matrix[position_row][position_col] == "D":
            number_of_decoration += 1
        elif matrix[position_row][position_col] == "G":
            number_of_gifts += 1
        elif matrix[position_row][position_col] == "C":
            number_of_cookies += 1
        if check(number_of_decoration, number_of_gifts, number_of_cookies, all_decorations, all_gifts, all_cookies):
            print("Merry Christmas!")
            break
        matrix[position_row][position_col] = "x"
    if check(number_of_decoration, number_of_gifts, number_of_cookies, all_decorations, all_gifts, all_cookies):
        break
    command = input()

matrix[position_row][position_col] = "Y"
print("You've collected:")
print(f"- {number_of_decoration} Christmas decorations")
print(f"- {number_of_gifts} Gifts")
print(f"- {number_of_cookies} Cookies")

for row in matrix:
    print(" ".join(row))