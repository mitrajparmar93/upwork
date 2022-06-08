import csv


def jsonlisttocsv(csv_file, field_names: list, json_data: list):
    """
    jsontocsv: Convert list of dicts into CSV

    Args:
        csv_file (_type_): Output CSV file
        field_names (list): Column headers
        json_data (list): List of dicts
    """

    try:
        with open(csv_file, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writeheader()
            for data in json_data:
                writer.writerow(data)

    except IOError:
        print("I/O Error")
