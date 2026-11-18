"""Функции маскирования номеров карт и счетов."""

from typing import Optional


def get_mask_card_number(card_number: str) -> Optional[str]:
    """Замаскировать номер карты: 'XXXX XX** **** XXXX'.

    Args:
        card_number: Номер карты (16 цифр без пробелов).

    Returns:
        Строка с маской или None, если номер некорректный.
    """
    if not card_number or not card_number.isdigit() or len(card_number) != 16:
        return None
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> Optional[str]:
    """Замаскировать номер счёта: '**XXXX'.

    Args:
        account_number: Номер счёта (минимум 4 цифры).

    Returns:
        Строка с маской или None, если номер некорректный.
    """
    if not account_number or not account_number.isdigit() or len(account_number) < 4:
        return None
    return f"**{account_number[-4:]}"
