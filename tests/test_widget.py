"""Тесты для модуля widget."""

import pytest

from src.widget import get_date, mask_account_card


class TestMaskAccountCard:
    """Тесты функции mask_account_card."""

    @pytest.mark.parametrize(
        ("raw", "expected"),
        [
            ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
            ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
            ("Счет 73654108430135874305", "Счет **4305"),
            ("Счёт 1234567890", "Счёт **7890"),
        ],
    )
    def test_recognizes_card_and_account(self, raw: str, expected: str) -> None:
        """Функция распознаёт тип и применяет маску."""
        assert mask_account_card(raw) == expected

    @pytest.mark.parametrize(
        "bad_input",
        ["", "   ", "Visa", "Visa Platinum", "Visa Platinum notdigits"],
    )
    def test_handles_bad_input(self, bad_input: str) -> None:
        """Некорректный ввод — None."""
        assert mask_account_card(bad_input) is None


class TestGetDate:
    """Тесты функции get_date."""

    @pytest.mark.parametrize(
        ("iso_date", "expected"),
        [
            ("2024-03-15T10:20:30", "15.03.2024"),
            ("2023-12-01T08:00:00", "01.12.2023"),
            ("2024-01-01T00:00:00", "01.01.2024"),
            ("2024-06-20T18:45:10.123456", "20.06.2024"),
        ],
    )
    def test_date_conversion(self, iso_date: str, expected: str) -> None:
        """Корректное преобразование ISO-даты."""
        assert get_date(iso_date) == expected

    @pytest.mark.parametrize("bad_date", ["", "not-a-date", "2024/03/15"])
    def test_invalid_date(self, bad_date: str) -> None:
        """Некорректная дата — None."""
        assert get_date(bad_date) is None
