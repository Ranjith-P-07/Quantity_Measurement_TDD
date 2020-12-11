from com.bridgelabz.QuantityMeasurement.QuantityMeasurement import QuantityMeasurement, Lengths, Volume, Weight
from com.bridgelabz.QuantityMeasurement.QuantityMeasurementError import QuantityMeasurementError
import pytest


# Checking If both Values are Zero Then Should Return True
@pytest.mark.parametrize("unit1, value1, unit2, value2 ",
                         [
                             (Lengths.Feet, 0.0, Lengths.Feet, 0.0),
                             (Lengths.Yard, 0.0, Lengths.Yard, 0.0),
                             (Lengths.Inch, 0.0, Lengths.Inch, 0.0),
                             (Lengths.Cm, 0.0, Lengths.Cm, 0.0),

                         ])
def test_givenZeroLengthAndZeroLength_whenCompared_returns_true(unit1, value1, unit2, value2):
    assert QuantityMeasurement(value1, unit1) == QuantityMeasurement(value2, unit2)


# Comparing If We give only one value to Feet to check whether it is Returning False or not
def test_givenZeroFtAndNone_whenCompared_returns_False():
    assert QuantityMeasurement(0.0, Lengths.Feet) is not None


# Comparing If one value is float and other value is int and Then Should return True
def test_givenZeroFtAndNonFloatType_WhenCompared_ShouldReturn_True():
    assert QuantityMeasurement(0.0, Lengths.Feet) == QuantityMeasurement(0, Lengths.Feet)


# Comparing If We Given Two Different Values and Then Should Return False
@pytest.mark.parametrize("unit1, value1, unit2, value2 ",
                         [
                             (Lengths.Feet, 1.0, Lengths.Feet, 2.0),
                             (Lengths.Yard, 1.0, Lengths.Yard, 2.0),
                             (Lengths.Inch, 1.0, Lengths.Inch, 2.0),
                             (Lengths.Cm, 1.0, Lengths.Cm, 2.0),

                         ])
def test_given_Different_Values_whenCompared_returns_False(unit1, value1, unit2, value2):
    assert QuantityMeasurement(value1, unit1) != QuantityMeasurement(value2, unit2)


# Comparing If We give only one value to Yard to check whether it is Returning False or not
def test_givenZeroYardAndNone_whenCompared_returns_False():
    assert QuantityMeasurement(0.0, Lengths.Yard) is not None


# Comparing If one value is float and other value is int and Then Should return True
def test_givenZeroYardAndNonFloatType_WhenCompared_ShouldReturn_True():
    assert QuantityMeasurement(0.0, Lengths.Yard) == QuantityMeasurement(0, Lengths.Yard)


# Comparing If We give only one value to Inch to check whether it is Returning False or not
def test_givenZeroInchAndNone_whenCompared_returns_False():
    assert QuantityMeasurement(0.0, Lengths.Inch) is not None


# Comparing If one value is float and other value is int and Then Should return True
def test_givenZeroInchAndNonFloatType_WhenCompared_ShouldReturn_True():
    assert QuantityMeasurement(0.0, Lengths.Inch) == QuantityMeasurement(0, Lengths.Inch)


# Checking The Conversion of 3 Feet is equal to 1 Yard, if it True then should return True
def test_given_3Ft_And_1Yard_whenCompared_ShouldReturn_True():
    assert QuantityMeasurement(3.0, Lengths.Feet) == QuantityMeasurement(1.0, Lengths.Yard)


# Checking The Conversion of 1 Feet is equal to 1 Yard, when checked should return False
def test_given_1Ft_And_1Yard_WhenCompared_ShouldReturn_False():
    assert QuantityMeasurement(1.0, Lengths.Feet) != QuantityMeasurement(1.0, Lengths.Yard)


# Checking The Conversion of 1 Yard is equal to 3 Feet, When checked Should return True
def test_given_1Yard_And_3Ft_WhenCompared_ShouldReturn_True():
    assert QuantityMeasurement(1.0, Lengths.Yard, ) == QuantityMeasurement(3.0, Lengths.Feet)


# Checking the Conversion of 1Inch is equal to 1 yard, when checked should return False
def test_given_1Inch_And_1Yard_WhenCompared_ShouldReturn_False():
    assert QuantityMeasurement(1.0, Lengths.Inch) != QuantityMeasurement(1.0, Lengths.Yard)


# Checking the Conversion of 1Yard is equal to 36 Inch, when checked should return True
def test_given_1Yard_And_36Inch_whenCompared_shouldReturn_True():
    assert QuantityMeasurement(1.0, Lengths.Yard) == QuantityMeasurement(36.0, Lengths.Inch)


# Checking the Conversion of 36Inch is equal to 1 Yard, when checked should return True
def test_given_36inch_And_1Yard_whenCompared_ShouldReturn_True():
    assert QuantityMeasurement(36.0, Lengths.Inch) == QuantityMeasurement(1.0, Lengths.Yard)


# Checking the Conversion of 2Inch is equal to 5Cm, when checked should return True
def test_given_2Inch_And_5Cm_WhenCompared_ShouldReturn_True():
    assert QuantityMeasurement(2.0, Lengths.Inch) == QuantityMeasurement(5.0, Lengths.Cm)


# Checking the Conversion of 2 Inch + 2 Inch is equal to 4 Inch, when checked should return True
def test_given_2Inch_Plus_2Inch_EqualsTo_4Inch_WhenCompared_ShouldReturn_True():
    assert QuantityMeasurement(2.0, Lengths.Inch) + QuantityMeasurement(2.0, Lengths.Inch) == 4


# Checking the Conversion of 1 Ft + 2 Inch is equal to 14 Inch, when checked should return True
def test_given_1Ft_2Inch_EqualsTo_14Inch_WhenCompared_ShouldReturn_True():
    assert QuantityMeasurement(1, Lengths.Feet) + QuantityMeasurement(2.0, Lengths.Inch) == 14


# Checking the Conversion of 1 Ft + 1 Ft is equal to 24 Inch, when checked should return True
def test_given_1Ft_1Ft_EqualsTo_24Inch_WhenCompared_ShouldReturn_True():
    assert QuantityMeasurement(1.0, Lengths.Feet) + QuantityMeasurement(1.0, Lengths.Feet) == 24


# Checking the Conversion of 2 Inch + 2.5 Cm is equal to 3 Inch, when checked should return True
def test_given_2Inch_2_5Cm_EqualsTo_3Inch_WhenCompared_ShouldReturn_True():
    assert QuantityMeasurement(2.0, Lengths.Inch) + QuantityMeasurement(2.5, Lengths.Cm) == 3


# Test Cases For Volume:
@pytest.mark.parametrize("unit1, value1, unit2, value2",
                         [
                             (Volume.Gallon, 0.0, Volume.Gallon, 0.0),
                             (Volume.Litre, 0.0, Volume.Litre, 0.0),
                             (Volume.Ml, 0.0, Volume.Ml, 0.0),
                         ])
def test_given_zeroVolume_And_ZeroVolume_WhenCompared_ShouldReturn_True(unit1, value1, unit2, value2):
    assert QuantityMeasurement(value1, unit1) == QuantityMeasurement(value2, unit2)


@pytest.mark.parametrize("unit1, value1, unit2, value2",
                         [
                             (Volume.Gallon, 1.0, Volume.Gallon, 2.0),
                             (Volume.Litre, 1.0, Volume.Litre, 2.0),
                             (Volume.Ml, 1.0, Volume.Ml, 2.0),

                         ])
def test_given_Different_Values_Volume_whenCompared_returns_False(unit1, value1, unit2, value2):
    assert QuantityMeasurement(value1, unit1) != QuantityMeasurement(value2, unit2)


def test_given_1Gallon_And_3_78Li_WhenCompared_ShouldReturn_True():
    assert QuantityMeasurement(1.0, Volume.Gallon, ) == QuantityMeasurement(3.78, Volume.Litre)


def test_given_1Litre_And_1000ml_WhenCompared_ShouldReturn_True():
    assert QuantityMeasurement(1.0, Volume.Litre) == QuantityMeasurement(1000.0, Volume.Ml)


def test_given_1Gallon_3_78Litre_equalsTo_7_56Litre_WhenCompared_ShouldReturn_True():
    assert QuantityMeasurement(1.0, Volume.Gallon) + QuantityMeasurement(3.78, Volume.Litre) == 7.56


def test_given_1Litre_Plus_1000Ml_EqualsTo_2Litre_WhenCompared_ShouldReturn_True():
    assert QuantityMeasurement(1.0, Volume.Litre) + QuantityMeasurement(1000, Volume.Ml) == 2


# Test Cases For Weight:
@pytest.mark.parametrize("unit1, value1, unit2, value2",
                         [
                             (Weight.KG, 0.0, Weight.KG, 0.0),
                             (Weight.GM, 0.0, Weight.GM, 0.0),
                             (Weight.TONNE, 0.0, Weight.TONNE, 0.0),
                         ])
def test_given_zeroWeight_And_ZeroWeight_WhenCompared_ShouldReturn_True(unit1, value1, unit2, value2):
    assert QuantityMeasurement(value1, unit1) == QuantityMeasurement(value2, unit2)


@pytest.mark.parametrize("unit1, value1, unit2, value2",
                         [
                             (Weight.KG, 1.0, Weight.KG, 2.0),
                             (Weight.GM, 1.0, Weight.GM, 2.0),
                             (Weight.TONNE, 1.0, Weight.TONNE, 2.0),

                         ])
def test_given_Different_Values_Weight_whenCompared_returns_False(unit1, value1, unit2, value2):
    assert QuantityMeasurement(value1, unit1) != QuantityMeasurement(value2, unit2)


def test_given_1Kg_And_1000Grams_WhenCompared_ShouldReturn_True():
    assert QuantityMeasurement(1.0, Weight.KG) == QuantityMeasurement(1000, Weight.GM)


def test_given_1Tonne_And_1000Kgs_WhenCompared_ShouldReturn_True():
    assert QuantityMeasurement(1.0, Weight.TONNE) == QuantityMeasurement(1000, Weight.KG)