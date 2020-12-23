import sys

min_wage = 20000
file_name = "task3.txt"

try:
    with open(file_name, 'r', encoding='utf-8') as fh:
        employees = fh.readlines()
except IOError as e:
    print(e)
    sys.exit(1)

average_salary = 0

for employee in employees:
    name, salary = employee.split()

    try:
        salary = int(salary)
    except ValueError:
        continue

    average_salary += salary
    if salary < min_wage:
        print('Минимальный оклад у: ', (name))

print('Средний оклад: ', round(average_salary / len(employees), 2))





my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('task4.txt', 'w', encoding='utf-8') as new_block:
    with open('task4.txt', encoding='utf-8') as orig_block:
        new_block.writelines([line.replace(line.split()[0], my_dict.get(line.split()[0])) for line in orig_block])