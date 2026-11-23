"""Виджет для отображения карт, счетов и дат."""

from datetime import datetime
from typing import Optional

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(raw: str) -> Optional[str]:
    """Замаскировать карту или счёт по строке вида 'Visa ... 1234'.

    Args:
        raw: Строка с типом и номером ('Visa Platinum 7000...', 'Счет 7365...').

    Returns:
        Строка с замаскированным номером или None при ошибке.
    """
    if not raw or not raw.strip():
        return None

    parts = raw.rsplit(maxsplit=1)
    if len(parts) != 2:
        return None

    title, number = parts
    if not number.isdigit():
        return None

    if title.strip().lower().startswith(("счет", "счёт")):
        masked = get_mask_account(number)
        return f"{title} {masked}" if masked else None

    masked = get_mask_card_number(number)
    return f"{title} {masked}" if masked else None


def get_date(iso_date: str) -> Optional[str]:
    """Преобразовать ISO-дату в формат 'DD.MM.YYYY'.

    Args:
        iso_date: Дата в ISO-формате ('2024-03-15T10:20:30').

    Returns:
        Дата 'DD.MM.YYYY' или None, если формат некорректный.
    """
    if not iso_date:
        return None
    try:
        parsed = datetime.fromisoformat(iso_date)
    except ValueError:
        return None
    return parsed.strftime("%d.%m.%Y")
