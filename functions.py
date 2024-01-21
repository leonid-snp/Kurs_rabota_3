import json


def get_json_file() -> list[dict, ...]:
    """
    Функция считывает файл Json
    :return: Список словарей
    """
    with open("operations.json") as file:
        file = json.load(file)
        return file


list_of_banking_transactions = get_json_file()
