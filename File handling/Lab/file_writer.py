# def write_to_file(file_path, mode, text):
#     # file = open(file_path, mode)
#     # file.write(text)
#     # file.close()
#     with open(file_path, mode) as file:
#         file.write(text)
#
#
# write_to_file('files/numbers.txt', 'a', 'tuk pi6a text')

file_path = 'my_first_file.txt'
content = 'I just created my first file'

with open(file_path, 'w') as file:
    file.write(content)


# variant 2
# file = open(file_path, 'w')
# file.write(content)
# file.close()
