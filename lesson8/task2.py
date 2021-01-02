class UnforgivableCurse(Exception):
    text = "Магия вне Хогвартса! На ноль делить нельзя!"

    def __str__(self):
        return self.text

class Number(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise UnforgivableCurse

        return Number(float(self) / float(other))

if __name__ == '__main__':
    while True:
        try:
            dividend, divider = map(Number, input("Введите значения через пробел: ").split())
            print(dividend / divider)
        except UnforgivableCurse as e:
            print(e)
        except ValueError as e:
            print(e)
            break