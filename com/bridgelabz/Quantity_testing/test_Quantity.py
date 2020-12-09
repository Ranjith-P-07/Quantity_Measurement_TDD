from com.bridgelabz.QuantityMeasurement.QuantityMeasurement import Feet, Yard, Inch
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


# Comparing If one value is float and other value is int and Then Should return True
def test_givenZeroFtAndNonFloatType_WhenCompared_ShouldReturn_True():
    first_feet = Feet(0.0)
    second_feet = Feet(0)
    assert first_feet == second_feet


# Comparing If We Given Two Different Values and Then Should Return False
def test_givenDifferentFtValues_WhenCompared_ShouldReturn_False():
    first_feet = Feet(1.0)
    second_feet = Feet(2.0)
    assert (first_feet == second_feet) == False


# Comparing Two same Yard Values and Should return True
def test_givenZeroYardAndZeroYard_whenCompared_returns_true():
    first_yard = Yard(0.0)
    second_yard = Yard(0.0)
    assert first_yard == second_yard


# Comparing If We give only one value to Yard to check whether it is Returning False or not
def test_givenZeroYardAndNone_whenCompared_returns_False():
    first_yard = Yard(0.0)
    assert first_yard is not None


# Comparing If one value is float and other value is int and Then Should return True
def test_givenZeroYardAndNonFloatType_WhenCompared_ShouldReturn_True():
    first_yard = Yard(0.0)
    second_yard = Yard(0)
    assert first_yard == second_yard


# Comparing If We Given Two Different Values and Then Should Return False
def test_givenDifferentYardValues_WhenCompared_ShouldReturn_False():
    first_yard = Yard(1.0)
    second_yard = Yard(2.0)
    assert (first_yard == second_yard) == False


# Checking The Conversion of 3 Feet is equal to 1 Yard, if it True then should return True
def test_given_3Ft_And_1Yard_whenCompared_ShouldReturn_True():
    first_feet = Feet(3.0)
    second_yard = Yard(1.0)
    assert first_feet == second_yard


# Checking The Conversion of 1 Feet is equal to 1 Yard, when checked should return False
def test_given_1Ft_And_1Yard_WhenCompared_ShouldReturn_False():
    first_feet = Feet(1.0)
    second_yard = Yard(1.0)
    assert first_feet != second_yard


# Checking The Conversion of 1 Yard is equal to 3 Feet, Whwn checked Should return True
def test_given_1Yard_And_3Ft_WhenCompared_ShouldReturn_True():
    first_yard = Yard(1.0)
    second_feet = Feet(3.0)
    assert first_yard == second_feet


# Comparing Two same Feet Values and Should return True
def test_givenZeroInchAndZeroInch_whenCompared_returns_true():
    first_feet = Inch(0.0)
    second_feet = Inch(0.0)
    assert first_feet == second_feet
