import re


def strip_newlines_from_edges(string):
    stripped_from_start = re.sub("^\n", "", string)
    stripped_from_both = re.sub("\n$", "", stripped_from_start)
    return stripped_from_both
