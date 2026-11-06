def get_mask_card_number(card_number: str) -> str:
    # Убираем пробелы и дефисы
    clean_number = str(card_number).replace(" ", "").replace("-", "")
    if len(clean_number) != 16:
        raise ValueError("Неверная длина номера карты")
    return f"{clean_number[:4]} {clean_number[4:6]}** **** {clean_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    clean_number = str(account_number).replace(" ", "")
    if len(clean_number) < 4:
        raise ValueError("Неверная длина номера счета")
    return f"**{clean_number[-4:]}"
