import re


def strip_newlines_from_edges(string):
    stripped_from_start = re.sub("^\n", "", string)
    stripped_from_both = re.sub("\n$", "", stripped_from_start)
    return stripped_from_both


def flatten_list(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list
