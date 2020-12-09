from com.bridgelabz.QuantityMeasurement.QuantityMeasurementError import QuantityMeasurementError


class Feet:
    def __init__(self, feet):
        self.feet = feet

    def __eq__(self, other):
        if isinstance(other, Yard):
            return self.feet == other.yard * 3
        if isinstance(other, Inch):
            return other.inch == self.feet * 12
        return self.feet == other


class Yard:
    def __init__(self, yard):
        self.yard = yard

    def __eq__(self, other):
        if isinstance(other, Feet):
            return other.feet == self.yard * 3
        if isinstance(other, Inch):
            return other.inch == self.yard * 36
        return self.yard == other


class Inch:
    def __init__(self, inch):
        self.inch = inch

    def __eq__(self, other):
        if isinstance(other, Feet):
            return self.inch == other.feet * 12
        if isinstance(other, Yard):
            return self.inch == other.yard * 36
        return self.inch == other
