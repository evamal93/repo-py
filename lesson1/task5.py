earnings = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if earnings > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {earnings / costs}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"Прибыль в расчете на одного сторудника - {earnings / workers}")
else:
    print("Фирма работает в убыток")
