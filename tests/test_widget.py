import pytest

from widget import get_date, mask_account_card


def test_mask_account_card_visa():
    result = mask_account_card("Visa Platinum 1234567890123456")
    assert result == "Visa Platinum 1234 56** **** 3456"


def test_mask_account_card_account():
    result = mask_account_card("Счет 12345678901234567890")
    assert result == "Счет **7890"


def test_mask_account_card_empty():
    with pytest.raises(ValueError):
        mask_account_card("")


def test_get_date_valid():
    assert get_date("2024-03-15T10:30:00") == "15.03.2024"


def test_get_date_invalid():
    with pytest.raises(ValueError):
        get_date("not-a-date")
