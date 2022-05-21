numbers_counts = {}
numbers = [float(x) for x in input().split(" ")]

for number in numbers:
    if number not in numbers_counts:
        numbers_counts[number] = 0
    numbers_counts[number] += 1

for number, count in numbers_counts.items():
    print(f"{number} - {count} times")
