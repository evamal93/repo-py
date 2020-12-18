from sys import argv

name, hour, rate, benefit = argv

calculation = (int(hour) * int(rate)) + int(benefit)
print(f"Общая сумма выплат равна {calculation}")