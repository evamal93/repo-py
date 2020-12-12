def my_func (x, y):
    try:
        z = x / y
        return float(z)
    except ZeroDivisionError:
        return "На ноль делить нельзя!"

print(my_func(int(input("Введите x = ")), int(input("Введите y = "))))







