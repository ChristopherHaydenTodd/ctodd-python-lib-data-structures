#!/usr/bin/env python3
"""
    Purpose:
        Provide Dictionary Helper Functions
"""

# Python Library Imports
import logging
import random
import collections


def flatten_dict_keys(dict_to_convert, parent="", separator="/", only_leaves=False):
    """
    Purpose:
        Flatten out a dictionaryies keys as a list of strings so that functions
        can consume the list in a certain fashion

        a dict with paths to create on an OS as shown in
        os_helpers.directory_helpers.create_directories()
    Args:
        dict_to_convert (Dictionary): Dictionary with key/values. Will traverse the
            dict and convert all keys into a single list of strings
        separator (String): String separator of the keys
        only_leaves (Boolean): Whether or not to return non-leaf keys
    Return:
        dict_keys (List of Strings): The list of all keys and paths to each key
            in the provided dict
    """

    dict_keys = []
    for key, value in dict_to_convert.items():
        full_key = f"{parent}{separator}{key}" if parent else key
        if isinstance(value, collections.MutableMapping) and value:
            dict_keys.extend(
                flatten_dict_keys(
                    value, parent=full_key, separator=separator, only_leaves=only_leaves
                )
            )
            if not only_leaves:
                dict_keys.append(full_key)
        else:
            dict_keys.append(full_key)

    return dict_keys
