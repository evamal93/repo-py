a = int(input("Сколько км вы пробежали в первый день?"))
b = int(input("Сколько км вы хотели бы в итоге пробежать?"))
result_days = 1
goal = a
while goal < b:
        a = a + 0.1 * a
        result_days += 1
        goal = goal + a
print(f"Вы достигнете своей цели на {result_days} день тренировок")