import os
from os import path

if path.exists('my_first_file.txt'):
    os.remove('my_first_file.txt')
else:
    print("File already deleted!")

# print(os.listdir('.')) # pokazva kakvo ima v direktoriqta