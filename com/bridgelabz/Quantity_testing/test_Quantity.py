from com.bridgelabz.QuantityMeasurement.QuantityMeasurement import QuantityMeasurement, Lengths


# Comparing Two same Feet Values and Should return True
def test_givenZeroFtAndZeroFt_whenCompared_returns_true():
    first_feet = QuantityMeasurement(Lengths.Feet, 0.0)
    second_feet = QuantityMeasurement(Lengths.Feet, 0.0)
    assert first_feet == second_feet

