from random import randint
first_list = [randint(2, 13) for _ in range(10)]
print(first_list)
second_list = [el for el in first_list if first_list.count(el)==1]
print(second_list)