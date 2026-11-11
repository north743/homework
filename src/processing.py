from typing import Any


def filter_by_state(
    data: list[dict[str, Any]], state: str = "EXECUTED"
) -> list[dict[str, Any]]:
    """Фильтрует список словарей по значению ключа 'state'.

    Args:
        data: Список словарей с данными о банковских операциях.
        state: Значение ключа 'state' для фильтрации.
            По умолчанию 'EXECUTED'.

    Returns:
        Новый список словарей, у которых ключ 'state' равен
        заданному значению.
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(
    data: list[dict[str, Any]], reverse: bool = True
) -> list[dict[str, Any]]:
    """Сортирует список словарей по дате (ключ 'date').

    Args:
        data: Список словарей с данными о банковских операциях.
        reverse: Порядок сортировки. True — по убыванию (по умолчанию),
            False — по возрастанию.

    Returns:
        Новый список словарей, отсортированный по дате.
    """
    return sorted(data, key=lambda item: item.get("date", ""), reverse=reverse)
