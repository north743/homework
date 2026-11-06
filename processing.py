from datetime import datetime


def filter_by_state(transactions: list, state: str = "EXECUTED") -> list:
    return [t for t in transactions if t.get("state") == state]


def sort_by_date(transactions: list, reverse: bool = True) -> list:
    def parse_date(t):
        try:
            return datetime.fromisoformat(t["date"])
        except (ValueError, KeyError):
            raise ValueError("Неверный формат даты")

    return sorted(transactions, key=parse_date, reverse=reverse)
