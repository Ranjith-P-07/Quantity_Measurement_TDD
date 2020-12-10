from enum import Enum


class QuantityMeasurement:
    def __init__(self, unit, value):
        self.unit = unit
        self.value = value

    def __eq__(self, other):
        if isinstance(other, QuantityMeasurement):
            return self.unit == other.unit and self.value == other.value
        return False

    def compare(self, other):
        if isinstance(self.unit, Lengths) and isinstance(other.unit, Lengths):
            if Lengths.convert(self.unit, self.value) == Lengths.convert(other.unit, other.value):
                return True
        return False


class Lengths(Enum):
    """
    Here Inch is taken as a Base Unit
    """
    Feet = 12.0
    Inch = 1.0
    Yard = 36.0
    Cm = 0.4

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        return self.unit * value
