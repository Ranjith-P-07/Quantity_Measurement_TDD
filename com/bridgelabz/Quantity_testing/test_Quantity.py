from com.bridgelabz.QuantityMeasurement.QuantityMeasurement import QuantityMeasurement, Lengths, Volume
import pytest


# Checking If both Values are Zero Then Should Return True
@pytest.mark.parametrize("Length1, Length2, expected",
                         [
                             (QuantityMeasurement(Lengths.Feet, 0.0), QuantityMeasurement(Lengths.Feet, 0.0), True),
                             (QuantityMeasurement(Lengths.Yard, 0.0), QuantityMeasurement(Lengths.Yard, 0.0), True),
                             (QuantityMeasurement(Lengths.Inch, 0.0), QuantityMeasurement(Lengths.Inch, 0.0), True),
                             (QuantityMeasurement(Lengths.Cm, 0.0), QuantityMeasurement(Lengths.Cm, 0.0), True),

                         ])
def test_givenZeroLengthAndZeroLength_whenCompared_returns_true(Length1, Length2, expected):
    assert (Length1 == Length2) == expected


# Comparing If We give only one value to Feet to check whether it is Returning False or not
def test_givenZeroFtAndNone_whenCompared_returns_False():
    first_feet = QuantityMeasurement(Lengths.Feet, 0.0)
    assert first_feet is not None


# Comparing If one value is float and other value is int and Then Should return True
def test_givenZeroFtAndNonFloatType_WhenCompared_ShouldReturn_True():
    first_feet = QuantityMeasurement(Lengths.Feet, 0.0)
    second_feet = QuantityMeasurement(Lengths.Feet, 0)
    assert first_feet == second_feet


@pytest.mark.parametrize("Length1, Length2, expected",
                         [
                             (QuantityMeasurement(Lengths.Feet, "Hello"), QuantityMeasurement(Lengths.Feet, "hi"),
                              False),
                             (QuantityMeasurement(Lengths.Yard, "Hello"), QuantityMeasurement(Lengths.Yard, "hi"),
                              False),
                             (QuantityMeasurement(Lengths.Inch, "Hello"), QuantityMeasurement(Lengths.Inch, "hi"),
                              False),
                             (QuantityMeasurement(Lengths.Cm, "Hello"), QuantityMeasurement(Lengths.Cm, "hi"), False),

                         ])
def test_givenString_And_String_whenCompared_returns_False(Length1, Length2, expected):
    assert (Length1 == Length2) == expected


# Comparing If We Given Two Different Values and Then Should Return False
@pytest.mark.parametrize("Length1, Length2, expected",
                         [
                             (QuantityMeasurement(Lengths.Feet, 1.0), QuantityMeasurement(Lengths.Feet, 2.0), False),
                             (QuantityMeasurement(Lengths.Yard, 1.0), QuantityMeasurement(Lengths.Yard, 2.0), False),
                             (QuantityMeasurement(Lengths.Inch, 1.0), QuantityMeasurement(Lengths.Inch, 2.0), False),
                             (QuantityMeasurement(Lengths.Cm, 1.0), QuantityMeasurement(Lengths.Cm, 2.0), False),

                         ])
def test_given_Different_Values_whenCompared_returns_False(Length1, Length2, expected):
    assert (Length1 == Length2) == expected


# Comparing If We give only one value to Yard to check whether it is Returning False or not
def test_givenZeroYardAndNone_whenCompared_returns_False():
    first_yard = QuantityMeasurement(Lengths.Yard, 0.0)
    assert first_yard is not None


# Comparing If one value is float and other value is int and Then Should return True
def test_givenZeroYardAndNonFloatType_WhenCompared_ShouldReturn_True():
    first_yard = QuantityMeasurement(Lengths.Yard, 0.0)
    second_yard = QuantityMeasurement(Lengths.Yard, 0)
    assert first_yard == second_yard


# Comparing If We give only one value to Inch to check whether it is Returning False or not
def test_givenZeroInchAndNone_whenCompared_returns_False():
    first_inch = QuantityMeasurement(Lengths.Inch, 0.0)
    assert first_inch is not None


# Comparing If one value is float and other value is int and Then Should return True
def test_givenZeroInchAndNonFloatType_WhenCompared_ShouldReturn_True():
    first_inch = QuantityMeasurement(Lengths.Inch, 0.0)
    second_inch = QuantityMeasurement(Lengths.Inch, 0)
    assert first_inch == second_inch


# Checking The Conversion of 3 Feet is equal to 1 Yard, if it True then should return True
def test_given_3Ft_And_1Yard_whenCompared_ShouldReturn_True():
    first_feet = QuantityMeasurement(Lengths.Feet, 3.0)
    second_yard = QuantityMeasurement(Lengths.Yard, 1.0)
    assert first_feet.compare(second_yard)


# Checking The Conversion of 1 Feet is equal to 1 Yard, when checked should return False
def test_given_1Ft_And_1Yard_WhenCompared_ShouldReturn_False():
    first_feet = QuantityMeasurement(Lengths.Feet, 1.0)
    second_yard = QuantityMeasurement(Lengths.Yard, 1.0)
    assert first_feet != second_yard


# Checking The Conversion of 1 Yard is equal to 3 Feet, When checked Should return True
def test_given_1Yard_And_3Ft_WhenCompared_ShouldReturn_True():
    first_yard = QuantityMeasurement(Lengths.Yard, 1.0)
    second_feet = QuantityMeasurement(Lengths.Feet, 3.0)
    assert first_yard.compare(second_feet)


# Checking the Conversion of 1Inch is equal to 1 yard, when checked should return False
def test_given_1Inch_And_1Yard_WhenCompared_ShouldReturn_False():
    first_inch = QuantityMeasurement(Lengths.Inch, 1.0)
    second_yard = QuantityMeasurement(Lengths.Yard, 1.0)
    assert first_inch != second_yard


# Checking the Conversion of 1Yard is equal to 36 Inch, when checked should return True
def test_given_1Yard_And_36Inch_whenCompared_shouldReturn_True():
    first_yard = QuantityMeasurement(Lengths.Yard, 1.0)
    second_inch = QuantityMeasurement(Lengths.Inch, 36.0)
    assert first_yard.compare(second_inch)


# Checking the Conversion of 36Inch is equal to 1 Yard, when checked should return True
def test_given_36inch_And_1Yard_whenCompared_ShouldReturn_True():
    first_inch = QuantityMeasurement(Lengths.Inch, 36.0)
    second_yard = QuantityMeasurement(Lengths.Yard, 1.0)
    assert first_inch.compare(second_yard)


# Checking the Conversion of 2Inch is equal to 5Cm, when checked should return True
def test_given_2Inch_And_5Cm_WhenCompared_ShouldReturn_True():
    inch = QuantityMeasurement(Lengths.Inch, 2.0)
    cm = QuantityMeasurement(Lengths.Cm, 5.0)
    assert inch.compare(cm)


# Checking the Conversion of 2 Inch + 2 Inch is equal to 4 Inch, when checked should return True
def test_given_2Inch_Plus_2Inch_EqualsTo_4Inch_WhenCompared_ShouldReturn_True():
    inch = QuantityMeasurement(Lengths.Inch, 2.0) + QuantityMeasurement(Lengths.Inch, 2.0)
    inch3 = QuantityMeasurement(Lengths.Inch, 4.0)
    assert inch == inch3


# Checking the Conversion of 1 Ft + 2 Inch is equal to 14 Inch, when checked should return True
def test_given_1Ft_2Inch_EqualsTo_14Inch_WhenCompared_ShouldReturn_True():
    feet_inch = QuantityMeasurement(Lengths.Feet, 1) + QuantityMeasurement(Lengths.Inch, 2.0)
    inch = QuantityMeasurement(Lengths.Inch, 14)
    assert feet_inch == inch


# Checking the Conversion of 1 Ft + 1 Ft is equal to 24 Inch, when checked should return True
def test_given_1Ft_1Ft_EqualsTo_24Inch_WhenCompared_ShouldReturn_True():
    feet = QuantityMeasurement(Lengths.Feet, 1.0) + QuantityMeasurement(Lengths.Feet, 1.0)
    inch = QuantityMeasurement(Lengths.Inch, 24.0)
    assert feet == inch


# Checking the Conversion of 2 Inch + 2.5 Cm is equal to 3 Inch, when checked should return True
def test_given_2Inch_2_5Cm_EqualsTo_3Inch_WhenCompared_ShouldReturn_True():
    inch_cm = QuantityMeasurement(Lengths.Inch, 2.0) + QuantityMeasurement(Lengths.Cm, 2.5)
    inch = QuantityMeasurement(Lengths.Inch, 3.0)
    assert inch_cm == inch


# Test Cases For Volume:
@pytest.mark.parametrize("Volume1, Volume2, expected",
                         [
                             (QuantityMeasurement(Volume.Gallon, 0.0), QuantityMeasurement(Volume.Gallon, 0.0), True),
                             (QuantityMeasurement(Volume.Litre, 0.0), QuantityMeasurement(Volume.Litre, 0.0), True),
                             (QuantityMeasurement(Volume.Ml, 0.0), QuantityMeasurement(Volume.Ml, 0.0), True),
                         ])
def test_given_zeroVolume_And_ZeroVolume_WhenCompared_ShouldReturn_True(Volume1, Volume2, expected):
    assert (Volume1 == Volume2) == expected


@pytest.mark.parametrize("Volume1, Volume2, expected",
                         [
                             (QuantityMeasurement(Volume.Gallon, 1.0), QuantityMeasurement(Volume.Gallon, 2.0), False),
                             (QuantityMeasurement(Volume.Litre, 1.0), QuantityMeasurement(Volume.Litre, 2.0), False),
                             (QuantityMeasurement(Volume.Ml, 1.0), QuantityMeasurement(Volume.Ml, 2.0), False),

                         ])
def test_given_Different_Values_whenCompared_returns_False(Volume1, Volume2, expected):
    assert (Volume1 == Volume2) == expected


def test_given_1Gallon_And_3_78Li_WhenCompared_ShouldReturn_True():
    gallon = QuantityMeasurement(Volume.Gallon, 1.0)
    gallon1 = QuantityMeasurement(Volume.Litre, 3.78)
    assert gallon.compare(gallon1)


def test_given_1Litre_And_1000ml_WhenCompared_ShouldReturn_True():
    gallon = QuantityMeasurement(Volume.Litre, 1.0)
    gallon1 = QuantityMeasurement(Volume.Ml, 1000.0)
    assert gallon.compare(gallon1)


def test_given_1Gallon_3_78Litre_equalsTo_7_56Litre_WhenCompared_ShouldReturn_True():
    gallon_litre = QuantityMeasurement(Volume.Gallon, 1.0) + QuantityMeasurement(Volume.Litre, 3.78)
    litre = QuantityMeasurement(Volume.Litre, 7.56)
    assert gallon_litre == litre


def test_given_1Litre_Plus_1000Ml_EqualsTo_2Litre_WhenCompared_ShouldReturn_True():
    litre_ml = QuantityMeasurement(Volume.Litre, 1.0) + QuantityMeasurement(Volume.Ml, 1000)
    litre = QuantityMeasurement(Volume.Litre, 2.0)
    assert litre_ml == litre
