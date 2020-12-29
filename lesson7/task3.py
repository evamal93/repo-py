class Cell:
    def __init__(self, numbs):
        self.numbs = numbs

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.numbs // rows)]) + '\n' + '*' * (self.numbs % rows)

    def __str__(self):
        return self.numbs

    def __add__(self, other):
        return f'Сумма равна {self.numbs + other.numbs}'

    def __sub__(self, other):
        return f'Вычитание равно {self.numbs - other.numbs}' if (self.numbs - other.numbs) > 0 else print('Некорректное значение')

    def __mul__(self, other):
        return f'Произведение равно {self.numbs * other.numbs}'

    def __truediv__(self, other):
        return f'Разница равна {self.numbs // other.numbs}'

cell_1 = Cell(30)
cell_2 = Cell(10)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2.make_order(20))
print(cell_1.make_order(10))