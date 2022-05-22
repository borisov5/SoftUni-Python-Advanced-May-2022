from lab.fibonacci_sequence.py import create_sequence, locate

print(create_sequence(10))
print(locate(13))

print(create_sequence(3))

try:
    print(create_sequence(3))
    print(locate(10))
except IndexError as err:
    print(err)
