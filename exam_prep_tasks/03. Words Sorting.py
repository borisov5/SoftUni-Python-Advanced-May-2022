def words_sorting(*args):
    dictionary = {}
    for idx in range(len(args)):
        value = 0
        for letter in args[idx]:
            value += ord(letter)
        dictionary[args[idx]] = value

    total_sum = 0
    for val in dictionary.values():
        total_sum += val
    print(dictionary)
    print(total_sum)
    if total_sum % 2 == 0:
        
        dictionary = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[0])}
    else:
        dictionary = {k: v for k, v in reversed(sorted(dictionary.items(), key=lambda item: item[1]))}

    result = ''
    for key, value in dictionary.items():
        result += f'{key} - {value}\n'

    return result

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
