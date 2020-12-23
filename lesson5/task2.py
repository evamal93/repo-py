with open('task2.txt', encoding='utf-8') as f:
    my_file = f.readlines()
    for index, value in enumerate(my_file, 1):
        str_len = len(value.split())
        print(f'Количество слов в {index} строке - {str_len}')

with open('task2.txt') as f:
    size=len([0 for _ in f])
    print(f'Всего строк: {size}')