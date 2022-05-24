def even_odd_filter(**kwargs):
    res = {}
    for key, values in kwargs.items():
        l = []
        if key == 'odd':
            for idx in values:
                if idx % 2 == 1:
                    l.append(idx)
        elif key == 'even':
            for idx in values:
                if idx % 2 == 0:
                    l.append(idx)
        res[key] = l
    res = {k: v for k, v in sorted(res.items(), key=lambda item: len(item[1]), reverse=True)}
    return res


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
