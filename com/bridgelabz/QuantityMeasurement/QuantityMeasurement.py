from enum import Enum

from com.bridgelabz.QuantityMeasurement.QuantityMeasurementError import QuantityMeasurementError


class QuantityMeasurement:
    """
    This class is for Measurement Purpose like Comparing, adding..
    """

    def __init__(self, value, choice):
        self.value = value
        self.choice = choice

    def __eq__(self, other):
        if isinstance(other, QuantityMeasurement):
            if type(self.choice) == type(other.choice):
                return self.choice.convert(self.value) == other.choice.convert(other.value)
            raise QuantityMeasurementError("Invalid Comparison")

    def __add__(self, other):
        if isinstance(other, QuantityMeasurement):
            if type(self.choice) == type(other.choice):
                return self.choice.convert(self.value) + other.choice.convert(other.value)
            raise QuantityMeasurementError("Invalid addition")


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


class Weight(Enum):
    """
    Here Kg is taken as base unit
    """
    KG = 1
    GM = 1000
    TONNE = 0.001

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        """
        converts the value into the base unit value
        :param value: takes value from user
        :return: converted value in base unit
        """
        return self.unit * value
