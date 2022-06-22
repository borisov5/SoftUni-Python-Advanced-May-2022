from collections import deque

pizza_orders = deque(map(int, input().split(", ")))
employees = deque(map(int, input().split(", ")))
total_count = 0

while pizza_orders and employees:
    number_of_pizzas = pizza_orders.popleft()
    employer_capacity = employees.pop()
    if number_of_pizzas > 10:
        employees.append(employer_capacity)
    elif number_of_pizzas <= 0:
        employees.append(employer_capacity)
        continue
    elif number_of_pizzas > employer_capacity:
        number_of_pizzas -= employer_capacity
        total_count += employer_capacity
        pizza_orders.appendleft(number_of_pizzas)
    else:
        total_count += number_of_pizzas

if pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, pizza_orders))}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_count}")
    print(f"Employees: {', '.join(map(str, employees))}")
