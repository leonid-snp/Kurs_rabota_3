import json


def get_json_file(name_file) -> list[dict, ...]:
    """
    Функция считывает файл Json
    :return: Список словарей
    """
    with open(name_file) as file:
        file = json.load(file)
        return file


def get_list_completed_operations(list_: list[dict, ...]) -> list[dict, ...]:
    """
    Функция принимает список словарей и сортирует его по выполненным операциям
    :param list_: список словарей
    :return: список словарей
    """
    completed_operations = [operation for operation in list_ if operation.get("state") == "EXECUTED"]
    return completed_operations


def get_latest_transactions(list_: list[dict, ...]) -> list[dict, ...]:
    """
    Функция принимает список словарей и отсортировывает их по дате возвращая
    только пять последних операций по дате
    :param list_: список словарей
    :return: пять первых элементов в списке
    """
    latest_transactions = sorted(list_, key=lambda date: date["date"], reverse=True)
    return latest_transactions[:5]


def get_date_from_string(list_: list[dict, ...]) -> tuple[str, ...]:
    """
    Функция принимает список словарей и возвращает кортеж из дат и типов операций
    :param list_: список словарей
    :return: кортеж строк
    """
    date = [data["date"][:10].replace("-", ".") for data in list_]
    list_operations = [description["description"] for description in list_]
    revers_data = [".".join(data.split(".")[::-1]) for data in date]
    type_transaction = (f"{revers_data[0] + " " + list_operations[0]}",
                        f"{revers_data[1] + " " + list_operations[1]}",
                        f"{revers_data[2] + " " + list_operations[2]}",
                        f"{revers_data[3] + " " + list_operations[3]}",
                        f"{revers_data[4] + " " + list_operations[4]}")

    return type_transaction


def get_card_number(list_: list[dict, ...]) -> tuple[str, ...]:
    """
    Функция принимает список словарей и возвращает зашифрованное значение по ключу "from"
    :param list_: список словарей
    :return: кортеж строк
    """
    list_cards = [card.get("from") for card in list_]
    list_number = [number.split()[-1] for number in list_cards if number is not None]
    cards_number = [number[:6] + "*" * 6 + number[-4:] for number in list_number if len(number) < 20]
    hidden_numbers = ("".join([f"{cards_number[0][:4]} {cards_number[0][4:8]} {cards_number[0][8:12]} {cards_number[0][12:16]},"
                      f"{cards_number[1][:4]} {cards_number[1][4:8]} {cards_number[1][8:12]} {cards_number[1][12:16]}"])
                      .split(","))
    hidden_numbers.append("**" + list_number[2][len(list_number[2]) - 4:])

    empty_list = []
    for card in list_cards:
        if card is not None:
            for el in card:
                if el.isalpha():
                    empty_list.append(el)

    card_names = f"{"".join(empty_list)[:11]} {"".join(empty_list)[11:18]} {"".join(empty_list)[18:]}".split()
    hidden_information = (f"{None}",
                          f"{card_names[0][:4]} {card_names[0][4:11]} {hidden_numbers[0]}",
                          f"{card_names[1]} {hidden_numbers[1]}",
                          f"{card_names[2]} {hidden_numbers[2]}",
                          f"{None}")

    return hidden_information


def get_account_number(list_: list[dict, ...]) -> list[str, ...]:
    """
    Функция получает список из 5 последних операций и выводит замаскированный счет куда были отправлены деньги
    :param list_: список словарей
    :return: список строк
    """
    account = [to.get("to").split()[0] + " " for to in list_]
    hidden_account = [account[0] + "**" + to.get("to").split()[-1][len(to.get("to").split()[-1]) - 4:] for to in list_]

    return hidden_account


def get_amount_transactions(list_: list[dict, ...]) -> list[str, ...]:
    """
    Функция получает список из 5 последних операций и возвращает список из сумм и валюты
    выполненных операций
    :param list_: список словарей
    :return: список строк
    """
    summ = [summ.get("operationAmount")["amount"] + " " + summ.get("operationAmount")["currency"]["name"] for summ in list_]
    return summ
