n = int(input('lenght number:'))
user_list = []
i = 0
while i < n:
    string = 'Enter element number' + str(i) + ':'
    user_list.append(input(string))
    i += 1
print(user_list)