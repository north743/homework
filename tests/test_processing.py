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

    @pytest.mark.parametrize("reverse", [True, False])
    def test_sort_direction(
        self,
        sample_operations: list[dict[str, Any]],
        reverse: bool,
    ) -> None:
        """Сортировка по убыванию и возрастанию."""
        result = sort_by_date(sample_operations, reverse=reverse)
        dates = [item["date"] for item in result]
        assert dates == sorted(dates, reverse=reverse)

    def test_default_is_descending(
        self, sample_operations: list[dict[str, Any]]
    ) -> None:
        """По умолчанию сортировка по убыванию."""
        result = sort_by_date(sample_operations)
        dates = [item["date"] for item in result]
        assert dates == sorted(dates, reverse=True)

    def test_same_dates_stable(
        self, operations_with_same_date: list[dict[str, Any]]
    ) -> None:
        """Одинаковые даты не ломают сортировку."""
        result = sort_by_date(operations_with_same_date)
        assert len(result) == len(operations_with_same_date)
        assert {item["id"] for item in result} == {1, 2, 3}

    @pytest.mark.parametrize("reverse", [True, False])
    def test_empty(
        self,
        empty_operations: list[dict[str, Any]],
        reverse: bool,
    ) -> None:
        """Пустой список — пустой результат при любом направлении."""
        assert sort_by_date(empty_operations, reverse=reverse) == []
