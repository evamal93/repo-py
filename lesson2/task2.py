make_list = input('Введите несколько чисел').split()
for i in range (1, len(make_list), 2):
    make_list.insert(i - 1, make_list.pop(i))
print(make_list)