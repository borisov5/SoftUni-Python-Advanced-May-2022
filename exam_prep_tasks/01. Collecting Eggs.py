from collections import deque

eggs_sizes = deque(map(int, input().split(', ')))
pieces_of_paper = deque(map(int, input().split(', ')))

boxes = 0
while eggs_sizes and pieces_of_paper:
    current_egg = eggs_sizes.popleft()
    current_paper = pieces_of_paper.pop()
    if current_egg == 13:
        switched_paper = pieces_of_paper.popleft()
        pieces_of_paper.appendleft(current_paper)
        pieces_of_paper.append(switched_paper)
    elif current_egg <= 0:
        pieces_of_paper.append(current_paper)
    elif (current_egg + current_paper) <= 50:
        boxes += 1


if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_sizes:
    print(f"Eggs left: {', '.join(map(str, eggs_sizes))}")
if pieces_of_paper:
    print(f"Pieces of paper left: {', '.join(map(str, pieces_of_paper))}")
