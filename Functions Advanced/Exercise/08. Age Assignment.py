def age_assignment(*args, **kwargs):
    result = {}
    res = ''
    for name in args:
        result[name] = 0
    for k, v in kwargs.items():
        for name in result:
            if k == name[0]:
                result[name] = v

    result = sorted(result.items(), key=lambda n: n[0])
    for name, years in result:
        res += f'{name} is {years} years old.\n'
    return res


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
