from com.bridgelabz.QuantityMeasurement.QuantityMeasurement import Feet, Yard
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


def test_givenZeroYardAndZeroYard_whenCompared_returns_true():
    first_yard = Yard(0.0)
    second_yard = Yard(0.0)
    assert first_yard == second_yard


def test_givenZeroYardAndNone_whenCompared_returns_False():
    first_yard = Yard(0.0)
    assert first_yard is not None


def test_givenZeroYardAndNonFloatType_WhenCompared_raise_Error():
    with pytest.raises(QuantityMeasurementError):
        first_yard = Yard(0.0)
        second_yard = Yard(0)
        assert first_yard == second_yard


def test_givenDifferentYardValues_WhenCompared_ShouldReturn_False():
    first_yard = Yard(1.0)
    second_yard = Yard(2.0)
    assert (first_yard == second_yard) == False
