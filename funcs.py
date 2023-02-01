import json
from datetime import datetime

with open('operations.json', 'r', encoding='utf-8') as json_file:
    input_json = json.load(json_file)

data = []
for item in input_json:
    try:
        if item['date']:
            data.append(item)
    except KeyError:
        pass

data_sorted_by_time = sorted(data,
                             key=lambda x: (x['date']),
                             reverse=True)

number_of_executed_operations = 5
last_executed_operations = []

for item in data_sorted_by_time:
    if item['state'] == 'EXECUTED':
        last_executed_operations.append(item)
        number_of_executed_operations -= 1
    if number_of_executed_operations == 0:
        break


def hide_digits(account):
    account_number = account.split(' ')[-1]
    if len(account_number) == 20:
        return f'Счет **{account_number[16:]}'
    else:
        return f'{" ".join(account.split(" ")[:-1])} ' \
               f'{account_number[0:4]} {account_number[4:6]}' \
               f'** **** {account_number[12:]}'


for operation in last_executed_operations:
    date = datetime.strptime(operation['date'][0:10], '%Y-%m-%d')
    print(f'{date.strftime("%d.%m.%Y")} {operation["description"]}')
    try:
        print(f'{hide_digits(operation["from"])} -> ', end='')
    except KeyError:
        pass
    print(f'{hide_digits(operation["to"])}')
    print(f'{operation["operationAmount"]["amount"]} '
          f'{operation["operationAmount"]["currency"]["name"]}')
    print()