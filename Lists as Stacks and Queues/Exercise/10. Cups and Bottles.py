from collections import deque


cups = deque(input().split())
bottles = deque(input().split())

wasted_litters_of_water = 0
while cups and bottles:
    current_cup = int(cups[0])
    current_bottle = int(bottles[-1])
    difference = current_bottle - current_cup
    if difference >= 0:
        wasted_litters_of_water += difference
        cups.popleft()
        bottles.pop()
    else:
        cups[0] = str(abs(difference))
        bottles.pop()

if bottles:
    print(f'Bottles: {" ".join(bottles)}')
if cups:
    print(f'Cups: {" ".join(cups)}')
print(f'Wasted litters of water: {wasted_litters_of_water}')
