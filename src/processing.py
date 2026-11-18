"""Фильтрация и сортировка банковских операций."""

from typing import Any


def filter_by_state(
    operations: list[dict[str, Any]],
    state: str = "EXECUTED",
) -> list[dict[str, Any]]:
    """Отфильтровать операции по статусу.

    Args:
        operations: Список словарей с операциями.
        state: Статус для фильтрации (по умолчанию 'EXECUTED').

    Returns:
        Отфильтрованный список операций.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(
    operations: list[dict[str, Any]],
    reverse: bool = True,
) -> list[dict[str, Any]]:
    """Отсортировать операции по полю 'date'.

    Args:
        operations: Список словарей с операциями.
        reverse: True — по убыванию (по умолчанию), False — по возрастанию.

    Returns:
        Отсортированный список операций.
    """
    return sorted(operations, key=lambda op: op.get("date", ""), reverse=reverse)
