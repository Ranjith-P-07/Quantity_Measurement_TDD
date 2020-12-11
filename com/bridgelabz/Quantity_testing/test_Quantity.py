from com.bridgelabz.QuantityMeasurement.QuantityMeasurement import QuantityMeasurement, Lengths


# Comparing Two same Feet Values and Should return True
def test_givenZeroFtAndZeroFt_whenCompared_returns_true():
    first_feet = QuantityMeasurement(Lengths.Feet, 0.0)
    second_feet = QuantityMeasurement(Lengths.Feet, 0.0)
    assert first_feet == second_feet


# Comparing If We give only one value to Feet to check whether it is Returning False or not
def test_givenZeroFtAndNone_whenCompared_returns_False():
    first_feet = QuantityMeasurement(Lengths.Feet, 0.0)
    assert first_feet is not None


# Comparing If one value is float and other value is int and Then Should return True
def test_givenZeroFtAndNonFloatType_WhenCompared_ShouldReturn_True():
    first_feet = QuantityMeasurement(Lengths.Feet, 0.0)
    second_feet = QuantityMeasurement(Lengths.Feet, 0)
    assert first_feet == second_feet


# Comparing If We Given Two Different Values and Then Should Return False
def test_givenDifferentFtValues_WhenCompared_ShouldReturn_False():
    first_feet = QuantityMeasurement(Lengths.Feet, 1.0)
    second_feet = QuantityMeasurement(Lengths.Feet, 2.0)
    assert (first_feet == second_feet) == False


# Comparing Two same Yard Values and Should return True
def test_givenZeroYardAndZeroYard_whenCompared_returns_true():
    first_yard = QuantityMeasurement(Lengths.Yard, 0.0)
    second_yard = QuantityMeasurement(Lengths.Yard, 0.0)
    assert first_yard == second_yard


# Comparing If We give only one value to Yard to check whether it is Returning False or not
def test_givenZeroYardAndNone_whenCompared_returns_False():
    first_yard = QuantityMeasurement(Lengths.Yard, 0.0)
    assert first_yard is not None


# Comparing If one value is float and other value is int and Then Should return True
def test_givenZeroYardAndNonFloatType_WhenCompared_ShouldReturn_True():
    first_yard = QuantityMeasurement(Lengths.Yard, 0.0)
    second_yard = QuantityMeasurement(Lengths.Yard, 0)
    assert first_yard == second_yard


# Comparing If We Given Two Different Values and Then Should Return False
def test_givenDifferentYardValues_WhenCompared_ShouldReturn_False():
    first_yard = QuantityMeasurement(Lengths.Yard, 1.0)
    second_yard = QuantityMeasurement(Lengths.Yard, 2.0)
    assert (first_yard == second_yard) == False


# Comparing Two same Inch Values and Should return True
def test_givenZeroInchAndZeroInch_whenCompared_returns_true():
    first_inch = QuantityMeasurement(Lengths.Inch, 0.0)
    second_inch = QuantityMeasurement(Lengths.Inch, 0.0)
    assert first_inch == second_inch


# Comparing If We give only one value to Inch to check whether it is Returning False or not
def test_givenZeroInchAndNone_whenCompared_returns_False():
    first_inch = QuantityMeasurement(Lengths.Inch, 0.0)
    assert first_inch is not None


# Comparing If one value is float and other value is int and Then Should return True
def test_givenZeroInchAndNonFloatType_WhenCompared_ShouldReturn_True():
    first_inch = QuantityMeasurement(Lengths.Inch, 0.0)
    second_inch = QuantityMeasurement(Lengths.Inch, 0)
    assert first_inch == second_inch


# Comparing If We Given Two Different Values and Then Should Return False
def test_givenDifferentInchValues_WhenCompared_ShouldReturn_False():
    first_inch = QuantityMeasurement(Lengths.Inch, 1.0)
    second_inch = QuantityMeasurement(Lengths.Inch, 2.0)
    assert (first_inch == second_inch) == False


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


def test_given_2Inch_And_5Cm_WhenCompared_ShouldReturn_True():
    inch = QuantityMeasurement(Lengths.Inch, 2.0)
    cm = QuantityMeasurement(Lengths.Cm, 5.0)
    assert inch.compare(cm)


def test_given_2Inch_Plus_2Inch_EqualsTo_4Inch_WhenCompared_ShouldReturn_True():
    inch = QuantityMeasurement(Lengths.Inch, 2.0) + QuantityMeasurement(Lengths.Inch, 2.0)
    inch3 = QuantityMeasurement(Lengths.Inch, 4.0)
    assert inch == inch3


def test_given_1Ft_2Inch_EqualsTo_14Inch_WhenCompared_ShouldReturn_True():
    feet_inch = QuantityMeasurement(Lengths.Feet, 1) + QuantityMeasurement(Lengths.Inch, 2.0)
    inch = QuantityMeasurement(Lengths.Inch, 14)
    assert feet_inch == inch
