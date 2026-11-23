"""Тесты для модуля masks."""

import pytest

from src.masks import get_mask_account, get_mask_card_number


class TestGetMaskCardNumber:
    """Тесты маскирования номера карты."""

    @pytest.mark.parametrize(
        ("card_number", "expected"),
        [
            ("7000792289606361", "7000 79** **** 6361"),
            ("1234567890123456", "1234 56** **** 3456"),
            ("0000000000000000", "0000 00** **** 0000"),
        ],
    )
    def test_masks_card_correctly(self, card_number: str, expected: str) -> None:
        """Корректное маскирование валидных карт."""
        assert get_mask_card_number(card_number) == expected

    @pytest.mark.parametrize(
        "invalid_number",
        ["", "1234", "abc", "12345678901234567890"],
    )
    def test_invalid_card_returns_none(self, invalid_number: str) -> None:
        """Некорректный номер карты — None."""
        assert get_mask_card_number(invalid_number) is None


class TestGetMaskAccount:
    """Тесты маскирования номера счёта."""

    @pytest.mark.parametrize(
        ("account_number", "expected"),
        [
            ("73654108430135874305", "**4305"),
            ("1234567890", "**7890"),
            ("00000000000000000000", "**0000"),
        ],
    )
    def test_masks_account_correctly(self, account_number: str, expected: str) -> None:
        """Корректное маскирование счёта."""
        assert get_mask_account(account_number) == expected

    @pytest.mark.parametrize("short_number", ["", "12", "123"])
    def test_account_too_short(self, short_number: str) -> None:
        """Слишком короткий номер счёта — None."""
        assert get_mask_account(short_number) is None
