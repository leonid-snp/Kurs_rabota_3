from functions.functions import get_json_file, get_list_completed_operations, get_latest_transactions, \
    get_date_from_string, get_card_number, get_account_number, get_amount_transactions


def main():
    list_banking_transactions = get_json_file()
    list_completed_operations = get_list_completed_operations(list_banking_transactions)
    last_five_operations = get_latest_transactions(list_completed_operations)
    date_from_string = get_date_from_string(last_five_operations)
    card_number = get_card_number(last_five_operations)
    account_number = get_account_number(last_five_operations)
    amount_transactions = get_amount_transactions(last_five_operations)

    for date in range(len(date_from_string)):
        if "Открытие вклада" in date_from_string[date]:
            print(f"{date_from_string[date]}\n{account_number[date]}\n{amount_transactions[date]}\n")
        elif "Перевод организации" in date_from_string[date]:
            print(f"{date_from_string[date]}\n{card_number[date]} -> {account_number[date]}\n{amount_transactions[date]}\n")
        elif "Перевод со счета на счет" in date_from_string[date]:
            print(f"{date_from_string[date]}\n{card_number[date]} -> {account_number[date]}\n{amount_transactions[date]}\n")
        else:
            print("Что то пошло не так")


if __name__ == "__main__":
    main()
