def my_func(a, b, c):
    result = max([a+b, b+c, c+a])
    return result

result = my_func(int(input("Введите первое число ")), int(input("Введите второе число ")), int(input("Введите третье число ")))
print(result)
