from pprint import pprint

def custom_write(file_name, strings):
    name = open(file_name, 'w')
    name.write(str(strings))
    name.close()
    name = open(file_name, 'r', encoding = 'utf-8')
    tup1 = (1, name.seek(0))
    tup2 = (2, name.seek(10))
    tup3 = (3, name.seek(20))
    tup4 = (4, name.seek(29))
    name.close()
    strings_positions = {tup1: 'Shla Sasha', tup2: 'Po Shosse', tup3: 'I sosala', tup4: 'Sushki'}
    return strings_positions



info = 'Shla Sasha\nPo Shosse\nI sosala\nSushki!'
file = 'для_дз.txt'
custom_write('для_дз.txt', info)

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

