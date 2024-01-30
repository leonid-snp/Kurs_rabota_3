import json


def get_json_file() -> list[dict, ...]:
    """
    Функция считывает файл Json
    :return: Список словарей
    """
    with open("operations.json") as file:
        file = json.load(file)
        return file


def get_list_completed_operations(list_: list[dict, ...]) -> list[dict, ...]:
    """
    Функция принимает список словарей и сортирует его по выполненным операциям
    :param list_: список словарей
    :return: список словарей
    """
    try:
        completed_operations = []
        for state in list_:
            if state["state"] == "EXECUTED":
                completed_operations.append(state)
        return completed_operations

    except KeyError:
        pass

    finally:
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


list_banking_transactions = get_json_file()
list_completed_operations = get_list_completed_operations(list_banking_transactions)
last_five_operations = get_latest_transactions(list_completed_operations)
print(last_five_operations)
