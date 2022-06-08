#!/usr/bin/env python3

import json
import glob
from pymethods.jsontocsv import jsonlisttocsv


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
                required_attrs = ['first-name', 'last-name',
                                  'company-title', 'company-name', 'website']

                for attr in required_attrs:

                    if attr in attribute_keys:
                        result[attr] = data['attributes'][attr]

                if result:
                    # append only if dict has data
                    final_result.append(result)

    csv_file = "json-to-csv/csvfile.csv"
    jsonlisttocsv(
        csv_file=csv_file,
        field_names=required_attrs,
        json_data=final_result
    )


if __name__ == '__main__':
    main()
