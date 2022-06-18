def naughty_or_nice_list(santa_list, *args, **kwargs):
    naughty = []
    nice = []
    not_found = []

    for arg in args:
        kid_number, command = arg.split("-")
        counter = 0
        current_kid = ''
        for number, kid in santa_list:
            if int(kid_number) == number:
                counter += 1
                current_kid = kid
                if counter > 1:
                    break
        if counter == 1:
            if command == "Nice":
                nice.append(current_kid)
                santa_list.remove((int(kid_number), current_kid))
            elif command == "Naughty":
                naughty.append(current_kid)
                santa_list.remove((int(kid_number), current_kid))
    for name, command in kwargs.items():
        counter = 0
        kid_number = None
        for number, kid in santa_list:
            kid_number = number
            if name == kid:
                counter += 1
                if counter > 1:
                    break
        if counter == 1:
            if command == "Nice":
                nice.append(name)
                santa_list.remove((int(kid_number), name))
            elif command == "Naughty":
                naughty.append(name)
                santa_list.remove((int(kid_number), name))

    for number, kid in santa_list:
            not_found.append(kid)

    result = ''
    if nice:
        result += f"Nice: {', '.join(nice)}\n"
    if naughty:
        result += f"Naughty: {', '.join(naughty)}\n"
    if not_found:
        result += f"Not found: {', '.join(not_found)}"
    return result



print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
