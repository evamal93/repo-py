file_name = "task1.txt"

with open('task1.txt', 'w') as f:
    while True:
        line = input('Введите произвольные данные или оставьте строку пустой для завершения работы: ')
        if not line:
            break

        print(line, file=f)
