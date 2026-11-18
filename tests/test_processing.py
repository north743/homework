"""Тесты для модуля processing."""

from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date


class TestFilterByState:
    """Тесты функции filter_by_state."""

    @pytest.mark.parametrize(
        ("state", "expected_ids"),
        [
            ("EXECUTED", [1, 3, 5]),
            ("CANCELED", [2]),
            ("PENDING", [4]),
            ("UNKNOWN", []),
        ],
    )
    def test_filters_by_state(
        self,
        sample_operations: list[dict[str, Any]],
        state: str,
        expected_ids: list[int],
    ) -> None:
        """Фильтрация по различным статусам."""
        result = filter_by_state(sample_operations, state)
        assert [item["id"] for item in result] == expected_ids

    def test_empty_list(self, empty_operations: list[dict[str, Any]]) -> None:
        """Пустой список — пустой результат."""
        assert filter_by_state(empty_operations, "EXECUTED") == []

    def test_default_state(self, sample_operations: list[dict[str, Any]]) -> None:
        """Значение по умолчанию — EXECUTED."""
        result = filter_by_state(sample_operations)
        assert all(item["state"] == "EXECUTED" for item in result)


class TestSortByDate:
    """Тесты функции sort_by_date."""

    def test_sort_descending(self, sample_operations: list[dict[str, Any]]) -> None:
        """По умолчанию сортировка по убыванию."""
        result = sort_by_date(sample_operations)
        dates = [item["date"] for item in result]
        assert dates == sorted(dates, reverse=True)

    def test_sort_ascending(self, sample_operations: list[dict[str, Any]]) -> None:
        """Сортировка по возрастанию при reverse=False."""
        result = sort_by_date(sample_operations, reverse=False)
        dates = [item["date"] for item in result]
        assert dates == sorted(dates)

    def test_same_dates_stable(self) -> None:
        """Одинаковые даты не ломают сортировку."""
        data = [
            {"id": 1, "date": "2024-01-01T00:00:00"},
            {"id": 2, "date": "2024-01-01T00:00:00"},
        ]
        result = sort_by_date(data)
        assert {item["id"] for item in result} == {1, 2}
        assert len(result) == 2

    def test_empty(self, empty_operations: list[dict[str, Any]]) -> None:
        """Пустой список — пустой результат."""
        assert sort_by_date(empty_operations) == []
