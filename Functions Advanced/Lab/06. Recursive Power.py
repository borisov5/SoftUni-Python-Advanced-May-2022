def recursive_power(num, rate):
    if rate <= 1:
        return num
    return num * recursive_power(num, rate - 1)

print(recursive_power(2, 10))
print(recursive_power(10, 100))
