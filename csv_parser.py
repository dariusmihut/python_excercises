import csv
import json

TELEGRAM_SIZE = 30
TELEGRAM_TEMPLATE = "{0}{1}{2}"

path = 'files/t_data.csv'
json_path = 'files/t_data.json'

csv_file = open(path, 'r+', encoding='utf-8-sig')
json_file = open(json_path, 'w+')

read_csv = csv.DictReader(csv_file,delimiter=';')

csv_file = open(path, 'r+', encoding='utf-8-sig')

json_data = {}
telegrams = []

for row in read_csv:
    telegrams.append(row)

json_data["transfer_id"] = 1
json_data["telegrams"] = telegrams

json_file.write(json.dumps(json_data))
json_file.close()
csv_file.close()

