from com.bridgelabz.QuantityMeasurement.QuantityMeasurementError import QuantityMeasurementError


class Feet:
    def __init__(self, feet):
        if type(feet) != float:
            raise QuantityMeasurementError("Entered Value is not Float type")
        self.feet = feet

    def __eq__(self, other):
        return self.feet == other
