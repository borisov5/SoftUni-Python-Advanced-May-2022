from collections import deque

materials = deque(map(int, input().split()))
magic = deque(map(int, input().split()))
aladdin_succeeded = False

diamonds = 0
gemstones = 0
gold = 0
porcelains = 0

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    present_sum = current_material + current_magic
    if present_sum < 100:
        if present_sum % 2 == 0:
            current_material *= 2
            current_magic *= 3
            present_sum = current_material + current_magic
        elif present_sum % 2 == 1:
            present_sum *= 2
    elif present_sum >= 500:
        present_sum /= 2

    if 100 <= present_sum < 200:
        gemstones += 1
    elif 200 <= present_sum < 300:
        porcelains += 1
    elif 300 <= present_sum < 400:
        gold += 1
    elif 400 <= present_sum < 500:
        diamonds += 1

    if (gemstones and porcelains) or (gold and diamonds):
        aladdin_succeeded = True

if aladdin_succeeded:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

if diamonds != 0:
    print(f"Diamond Jewellery: {diamonds}")
if gemstones != 0:
    print(f"Gemstone: {gemstones}")
if gold != 0:
    print(f"Gold: {gold}")
if porcelains != 0:
    print(f"Porcelain Sculpture: {porcelains}")
