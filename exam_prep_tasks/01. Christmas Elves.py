from collections import deque


elves_energy = deque(map(int, input().split()))
boxes = deque(map(int, input().split()))

total_used_energy = 0
total_number_of_toys = 0
counter = 0
while boxes and elves_energy:
    counter += 1
    current_elves_energy = elves_energy.popleft()
    number_of_materials = boxes.pop()
    if current_elves_energy < 5:
        boxes.append(number_of_materials)
        continue
    if counter % 3 == 0:
        number_of_materials *= 2
        if current_elves_energy < number_of_materials:

            total_number_of_toys += 2
            current_elves_energy -= number_of_materials
            total_used_energy += number_of_materials
            current_elves_energy += 1
            elves_energy.append(current_elves_energy)
        elif current_elves_energy >= number_of_materials:
            elves_energy.append(current_elves_energy)
            boxes.append(number_of_materials)
    elif counter % 5 == 0:
        current_elves_energy -= number_of_materials
        total_used_energy += number_of_materials
        boxes.append(current_elves_energy)
    elif current_elves_energy >= number_of_materials:
        total_number_of_toys += 1
        current_elves_energy -= number_of_materials
        current_elves_energy += 1
        total_used_energy += number_of_materials
        elves_energy.append(current_elves_energy)
    elif current_elves_energy < number_of_materials:
        boxes.append(number_of_materials)
        current_elves_energy *= 2
        elves_energy.append(current_elves_energy)


print(f"Toys: {total_number_of_toys}")
print(f"Energy: {total_used_energy}")

if elves_energy:
    print(f"Elves left: {', '.join(map(str, elves_energy))}")

if boxes:
    print(f"Boxes left: {', '.join(map(str, boxes))}")
