import pytest

from masks import get_mask_account, get_mask_card_number


def test_mask_card_number_valid():
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"


def test_mask_card_number_with_spaces():
    assert get_mask_card_number("1234 5678 9012 3456") == "1234 56** **** 3456"


def test_mask_card_number_invalid_length():
    with pytest.raises(ValueError):
        get_mask_card_number("1234")


def test_mask_account_valid():
    assert get_mask_account("12345678901234567890") == "**7890"


def test_mask_account_short():
    with pytest.raises(ValueError):
        get_mask_account("123")
