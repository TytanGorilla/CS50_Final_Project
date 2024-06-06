import pytest
from project import greet_obj, specify, target
from unittest.mock import patch

def main():
    test_correct_obj()
    test_incorrect_obj()
    test_correct_specify()
    test_incorrect_specify()
    test_correct_target()
    test_incorrect_target()

def test_correct_obj():
    with patch('builtins.input', return_value='1'):
        result = greet_obj()
        assert result == "Neck"

def test_incorrect_obj():
    with patch('builtins.input', return_value='bicep'):
        with pytest.raises(ValueError, match="Input an INT!"):
            greet_obj()

def test_correct_specify():
    with patch('builtins.input', return_value='1'):
        assert specify("Chest") == ['chest', 'upper']

def test_incorrect_specify():
    with patch('builtins.input', return_value='Rats'):
        with pytest.raises(ValueError, match="Input the appropriate number from the table!"):
            assert specify("Back")

def test_correct_target():
    with patch('builtins.input', return_value='2'):
        assert target(["arms", "upper"]) == "Brachialis"

def test_incorrect_target():
    with patch('builtins.input', return_value='Scaven'):
        with pytest.raises(ValueError, match="Again, input a number in the 'Select No.' column!"):
            assert target(["chest", "upper"])

if __name__ == "__main__":
    main()
