def even_odd(*args):
    command = args[-1]
    result = []
    parity = 0 if command == "even" else 1
    for num in args[0:len(args) - 1]:
        if num % 2 == parity:
            result.append(num)
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
