from com.bridgelabz.QuantityMeasurement.QuantityMeasurementError import QuantityMeasurementError


class Feet:
    def __init__(self, feet):
        if type(feet) != float:
            raise QuantityMeasurementError("Entered Value is not Float type")
        self.feet = feet

    def __eq__(self, other):
        if isinstance(other, Yard):
            return self.feet == other.yard * 3
        return self.feet == other


class Yard:
    def __init__(self, yard):
        if type(yard) != float:
            raise QuantityMeasurementError("Entered Value is not float type")
        self.yard = yard

    def __eq__(self, other):
        if isinstance(other, Feet):
            return other.feet == self.yard * 3
        return self.yard == other
