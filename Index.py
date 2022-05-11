#TestIndex = 'Sammy, andrey, Oleg'
#List = TestIndex.split(', ')

#for i in range(len(List)):
    #List[i] = List[i].capitalize()

#result = '___'.join(List)

#print(result)

#country = {'Name': 'Argentina', 'population': '4538032', 'VVP': '1,0%'}
#country = dict(code ='ENG', name = 'Europe')
#print(country['name']);

#country(country.items())

#for key, value in country.items():
  #print (key, "-", value)

#print(country.get('Name'))
#print(country.keys())

# person = {
#     'user_1': {
#         'first_name': 'John',
#         'last_name': 'Marley',
#         'age': 45,
#         'address': ['г. Москва', 'ул. Ужакова', '45'],
#         'gredes': {'math':5, 'physics': 3}
#     },
#     'User_2':{
#
#     }
# }
# print(person['user_1']['gredes'](math))

# data = {3,5,6,2,8}
# data.add(23)
# data.update(['32', True,4, 6])
# data.remove('32')
# data.pop()
#
# nums = [3,3,6,2,6]
# New_nums = set(nums)
# print(New_nums)

#new_data = frozenset([3,4,4,4,8,'32', True,4, 6])
#print(new_data)

#def def_test(a,b):
    #test = a + b
    #print(test, 'hehe')

#ef_test(1,4)

# #file = open('data/text.txt', 'r')
#
# print(file.read())
#
# file.close()

# file = open('data/text.txt', 'r')
# for line in file:
#     print(line, end='')
# file.close()




# x = 0
# while x == 0:
#     try:
#         x = int(input('Enter number: '))
#         x += 5
#         print(x)
#     except ValueError:
#         print('Uncurrect data, enter data type - number')
# try:
#     with open('data/text.txt', 'r', encoding ='utf-8') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('file not found')

import datetime as d, sys, os
print (os.name)