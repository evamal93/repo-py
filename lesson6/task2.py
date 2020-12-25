class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def outcome(self):
        return f'{self._length} м * {self._width} м * 25 кг * 5 см = {(self._length * self._width * 25 * 5)} тонн'

road = Road(7248, 72)
print(road.outcome())