#!/usr/bin/python3
"""
Return new txt
"""


def append_after(filename="", search_string="", new_string=""):
    """Overwrite an specific text if find the string python"""
    new_txt = ""
    with open(filename, "r") as f:
        for line in f:
            new_txt += line
            if search_string in line:
                new_txt += new_string

    with open(filename, "w") as w:
        w.write(new_txt)
