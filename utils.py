import re


def strip_newlines_from_edges(string):
    stripped_from_start = re.sub("^\n", "", string)
    stripped_from_both = re.sub("\n$", "", stripped_from_start)
    return stripped_from_both


def get_values_of_identical_keys(list_of_dicts, key):
    values = [dictionary[key] for dictionary in list_of_dicts]
    return tuple(values)


def sort_list_of_dicts(list_of_dicts, key):
    sorted_list = sorted(list_of_dicts, key=lambda k: int(k[key]))
    return sorted_list
