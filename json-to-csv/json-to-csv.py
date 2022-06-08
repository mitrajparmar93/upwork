#!/usr/bin/env python3

import json
from pprint import pprint as print
import csv
import glob


def main():
    file_list = glob.glob("json-to-csv/data/*")
    final_result = []

    for json_file in file_list:

        with open(json_file, 'r', encoding='utf-8') as jf:
            json_data = json.load(fp=jf)                

        for data in json_data['included']:
            result = {}
            data_keys = data.keys()

            if 'attributes' in data_keys:
                attribute_keys = data['attributes'].keys()
                required_attrs = ['first-name', 'last-name', 'company-title', 'company-name', 'website']

                for attr in required_attrs:

                    if attr in attribute_keys:
                        result[attr] = data['attributes'][attr]
                    # else:
                    #     result[attr] = 'NONE'

                if result:
                    final_result.append(result)

    print(final_result)

    csv_file = "json-to-csv/csvfile.csv"
    try:
        with open(csv_file, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['first-name', 'last-name', 'company-title', 'company-name', 'website'])
            writer.writeheader()
            for data in final_result:
                writer.writerow(data)
    except IOError:
        print("I/O error")

if __name__ == '__main__':
    main()