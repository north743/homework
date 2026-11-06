from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    if not info or not info.strip():
        raise ValueError("Пустая строка")

    parts = info.strip().split()
    # Ищем, где заканчивается текст и начинается номер
    number = parts[-1]
    prefix = " ".join(parts[:-1])

    if not prefix:
        raise ValueError("Неизвестный тип")

    if "Счет" in prefix:
        return f"{prefix} {get_mask_account(number)}"
    else:
        return f"{prefix} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    if not date_string:
        raise ValueError("Нет даты")
    try:
        dt = datetime.fromisoformat(date_string)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Неверный формат даты")
