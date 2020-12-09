from com.bridgelabz.QuantityMeasurement.QuantityMeasurement import Feet, Yard
from com.bridgelabz.QuantityMeasurement.QuantityMeasurementError import QuantityMeasurementError
import pytest


# Comparing Two same Feet Values and Should return True
def test_givenZeroFtAndZeroFt_whenCompared_returns_true():
    first_feet = Feet(0.0)
    second_feet = Feet(0.0)
    assert first_feet == second_feet


# Comparing If We give only one value to Feet to check whether it is Returning False or not
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


def test_given_3Ft_And_1Yard_whenCompared_ShouldReturn_True():
    first_feet = Feet(3.0)
    second_yard = Yard(1.0)
    assert first_feet == second_yard


def test_given_1Ft_And_1Yard_WhenCompared_ShoulReturn_False():
    first_feet = Feet(1.0)
    second_yard = Yard(1.0)
    assert first_feet != second_yard


def test_given_1Yard_And_3Ft_WhenCompared_ShouldReturn_True():
    first_yard = Yard(1.0)
    second_feet = Feet(3.0)
    assert first_yard == second_feet
