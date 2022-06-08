#!/usr/bin/env python3

import json
from pprint import pprint as print


json_file = "data/file-28.json"

with open(json_file, 'r') as jf:
    json_data = json.load(fp=jf)

for data in json_data['included']:
    data_keys = data.keys()
    if 'attributes' in data_keys:
        print(data['attributes'])
