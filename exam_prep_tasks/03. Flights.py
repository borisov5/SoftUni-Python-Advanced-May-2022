def flights(*args):
    dict = {}
    counter = 0
    last_key = ''
    for arg in args:
        counter += 1
        if arg == 'Finish':
            break
        if counter % 2 == 1:
            last_key = arg
            if arg in dict.keys():
                continue
            dict[arg] = 0
            last_key = arg
        elif counter % 2 == 0:
            dict[last_key] += arg

    return dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
