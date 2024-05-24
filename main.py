import json
import os.path
import sys
from json import JSONDecodeError


def printJson(file_path, key):
    if not os.path.isfile(file_path):
        print('The path "{}" does not point to a file or does not exist'.format(file_path))
        return

    try:

        json_file = open(file_path)

        json_raw_data = json.loads(json_file.read())
    except JSONDecodeError as err:
        print("Error decoding json: {}".format(str(err)))

    else:
        keys = key.split(',')

        json_data_multi = json_raw_data.get('data')
        for json_data in json_data_multi:
            for given_key in keys:
                property_structure = given_key.split('.')

                index = 0
                temp_value = json_data
                for property in property_structure:
                    temp_value = temp_value.get(property)
                    if index + 1 == len(property_structure):
                        value = temp_value

                    index = index+1

                if value:
                    print("{0}: {1}".format(given_key, value))
                else:
                    print('The key "{}" could not been found'.format(given_key))


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if len(arguments) != 2:
        print("Please provide one json file path and one key to print")
    else:
        printJson(arguments[0], arguments[1])
