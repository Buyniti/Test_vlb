TestIndex = 'Sammy, andrey, Oleg'
List = TestIndex.split(', ')

for i in range(len(List)):
    List[i] = List[i].capitalize()

result = '___'.join(List)

print(result)