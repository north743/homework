"""Общие фикстуры для тестов проекта."""

from typing import Any

import pytest


@pytest.fixture
def sample_operations() -> list[dict[str, Any]]:
    """Список операций с разными статусами и датами."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-15T10:20:30"},
        {"id": 2, "state": "CANCELED", "date": "2023-12-01T08:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
        {"id": 4, "state": "PENDING", "date": "2024-06-20T18:45:10"},
        {"id": 5, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
    ]


@pytest.fixture
def empty_operations() -> list[dict[str, Any]]:
    """Пустой список операций."""
    return []
