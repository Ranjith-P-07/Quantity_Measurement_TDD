from com.bridgelabz.QuantityMeasurement.QuantityMeasurement import Feet
from com.bridgelabz.QuantityMeasurement.QuantityMeasurementError import QuantityMeasurementError
import pytest


def test_givenZeroFtAndZeroFt_whenCompared_returns_true():
    first_feet = Feet(0.0)
    second_feet = Feet(0.0)
    assert first_feet == second_feet


def test_givenZeroFtAndNone_whenCompared_returns_False():
    first_feet = Feet(0.0)
    assert first_feet is not None


def test_givenZeroFtAndNonFloatType_WhenCompared_raise_Error():
    with pytest.raises(QuantityMeasurementError):
        first_feet = Feet(0.0)
        second_feet = Feet(0)
        assert first_feet == second_feet


def test_givenDifferentFtValues_WhenCompared_ShouldReturn_False():
    first_feet = Feet(1.0)
    second_feet = Feet(2.0)
    assert (first_feet == second_feet) == False


