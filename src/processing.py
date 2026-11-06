"""Модуль обработки данных о банковских операциях."""

from typing import Any

Transaction = dict[str, Any]


def filter_by_state(
    transactions: list[Transaction],
    state: str = "EXECUTED",
) -> list[Transaction]:
    """Фильтрует список операций по значению ключа ``state``.

    :param transactions: список словарей с данными об операциях
    :param state: значение статуса для фильтрации (по умолчанию ``'EXECUTED'``)
    :return: новый список словарей, у которых ``state`` равен ``state``
    """
    return [tx for tx in transactions if tx.get("state") == state]


def sort_by_date(
    transactions: list[Transaction],
    reverse: bool = True,
) -> list[Transaction]:
    """Сортирует список операций по дате.

    :param transactions: список словарей с данными об операциях
    :param reverse: порядок сортировки; ``True`` — по убыванию (по умолчанию),
        ``False`` — по возрастанию
    :return: новый список словарей, отсортированный по ключу ``date``
    """
    return sorted(transactions, key=lambda tx: tx["date"], reverse=reverse)