class Textil:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def total_for_coat(self):
        return self.width / 6.5 + 0.5

    def total_for_suit(self):
        return self.height * 2 + 0.3

    @property
    def total(self):
        return str(f'Общая площадь ткани: {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.coat_area = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани на пальто: {self.coat_area}'


class Suit(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.suit_area = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани на костюм: {self.suit_area}'

coat = Coat(5, 18)
suit = Suit(9, 11)
print(coat)
print(suit)
print(coat.total)
print(suit.total)
