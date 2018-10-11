import csv


def read_csv(file_path):
    with open(file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        list_of_rows = [dict(line) for line in reader]
    return list_of_rows
