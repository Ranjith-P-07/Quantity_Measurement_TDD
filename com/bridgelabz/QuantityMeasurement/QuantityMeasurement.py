from enum import Enum


class QuantityMeasurement:
    """
    This class is for Measurement Purpose like Comparing, adding..
    """
    def __init__(self, unit, value):
        self.unit = unit
        self.value = value

    def __eq__(self, other):
        if isinstance(other, QuantityMeasurement):
            return self.unit == other.unit and self.value == other.value
        if self.unit == other.unit and self.value == other.value:
            return True
        return False

    def compare(self, other):
        if isinstance(self.unit, Lengths) and isinstance(other.unit, Lengths):
            if Lengths.convert(self.unit, self.value) == Lengths.convert(other.unit, other.value):
                return True
        if isinstance(self.unit, Volume) and isinstance(other.unit, Volume):
            if Volume.convert(self.unit, self.value) == Volume.convert(other.unit, other.value):
                return True
        return False

    def __add__(self, other):
        if isinstance(self.unit, Lengths) and isinstance(other.unit, Lengths):
            other.value = Lengths.convert(self.unit, self.value) + Lengths.convert(other.unit, other.value)
            other.unit = Lengths.Inch
            return other
        if isinstance(self.unit, Volume) and isinstance(other.unit, Volume):
            other.value = Volume.convert(self.unit, self.value) + Volume.convert(other.unit, other.value)
            other.unit = Volume.Litre
            return other


class Lengths(Enum):
    """
    Here Inch is taken as a Base Unit.
    """
    Feet = 12.0
    Inch = 1.0
    Yard = 36.0
    Cm = 0.4

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        return self.unit * value


class Volume(Enum):
    """
    Here Litre is taken as a Base unit
    """
    Litre = 1.0
    Gallon = 3.78
    Ml = 0.001

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        return self.unit * value
