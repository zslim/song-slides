import csv


def read_csv(file_path):
    with open(file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        list_of_rows = [dict(line) for line in reader]
    data = set_numeric_fields(list_of_rows)
    return data


def set_numeric_fields(list_of_dicts):
    list_of_fields = list_of_dicts[0].keys()
    for row in list_of_dicts:
        for field in list_of_fields:
            try:
                row[field] = int(row[field])
            except ValueError:
                continue
    return list_of_dicts
