matrix = [input().split(' ') for _ in range(6)]

sum_of_points = 0
for _ in range(3):
    row, col = input().split(", ")
    row = int(row[1:])
    col = int(col[:-1])
    if int(row) >= 6 or int(col) >= 6:
        continue
    if matrix[row][col] == 'B':
        for idx in range(6):
            if matrix[idx][col] != 'B':
                sum_of_points += int(matrix[idx][col])
        matrix[idx][col] = '0'

prize = ''

if 100 <= sum_of_points < 200:
    prize = 'Football'
elif 200 <= sum_of_points < 300:
    prize = 'Teddy Bear'
elif sum_of_points >= 300:
    prize = 'Lego Construction Set'


if prize:
    print(f"Good job! You scored {sum_of_points} points, and you've won {prize}.")
else:
    difference = 100 - sum_of_points
    print(f"Sorry! You need {difference} points more to win a prize.")
