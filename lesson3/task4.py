# первый вариант
def my_func(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res

print(my_func(int(input("Введите положительное число ")), int(input("Введите отрицательное число "))))


# второй вариант
def another_func(x, y):
    result = pow(x,y)
    return result

result = another_func(int(input("Введите положительное число ")), int(input("Введите отрицательное число ")))
print(result)