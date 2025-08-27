import pytest
from database.db_couriers import validate_courier

# giving a test case to the function
def test_valid_courier():
    assert validate_courier("Jimbo", "4357583945") is True

# omitting an argument to test the function
def test_empty_name():
    with pytest.raises(ValueError, match="Courier name cannot be empty"):
        validate_courier("", "4357583945")

# inputing an invalid argument
def test_invalid_phone():
    with pytest.raises(ValueError, match="Courier phone must be digits only"):
        validate_courier("Jimbo", "nw3r5")