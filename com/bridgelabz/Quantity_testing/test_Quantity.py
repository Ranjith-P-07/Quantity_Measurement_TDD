from com.bridgelabz.QuantityMeasurement.QuantityMeasurement import Feet


def test_givenZeroFtAndZeroFt_whenCompared_returns_true():
    first_feet = Feet(0.0)
    second_feet = Feet(0.0)
    assert first_feet == second_feet


def test_givenZeroFtAndNone_whenCompared_returns_False():
    first_feet = Feet(0.0)
    assert first_feet is not None
