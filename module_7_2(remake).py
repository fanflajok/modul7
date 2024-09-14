from pprint import pprint

def custom_write(file_name, strings):
    n = 0
    strings_positions = {}
    dz = open(file_name, 'w', encoding = 'utf-8')
    for i in strings:
        strings_positions[(n+1), dz.tell()] = i
        dz.write(i + '\n')
        n = n + 1
    dz.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
file = 'для_дз.txt'
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)



