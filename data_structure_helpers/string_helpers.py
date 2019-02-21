#!/usr/bin/env python3
"""
    Purpose: Modify and Work with Strings
"""

# Python Library Imports
import sys
import re
import logging


def convert_to_title_case(string_to_convert):
    """
    Purpose:
        Convert Any string into title case. Special characters,
        numbers, and whitespace will be removed and replaced
        with a string with each word's first letter capitalized.
    Args:
        string_to_convert (String): String convert to title case
    Returns:
        converted_string (String): String with title case
    Examples:
        >>> string_to_convert = 'some_variable_name'
        >>> convert_to_title(strings_to_convert)
        >>> 'Some Variable Name'
    """
    logging.info(
        'Converting String Into Titles: {0}'.format(string_to_convert)
    )

    words = re.findall("[a-zA-Z]+", string_to_convert)
    return ' '.join([x.title() for x in words])


def convert_to_camel_case(string_to_convert, camel_caps=False):
    """
    Purpose:
        Convert Any string into camelCase. Special characters,
        numbers, and whitespace will be removed and replaced
        with a string with each word's first letter capitalized.
        There will be no spaces between each work and every word
        following the first will be capitalized. If CamelCaps is
        true, the first word will also be capital
    Args:
        string_to_convert (String): String convert to title case
        camel_caps (Boolean): If first word should be capitalized
    Returns:
        converted_string (String): String with camelCase
    Examples:
        >>> string_to_convert = 'some_variable_name'
        >>> convert_to_camel_case(strings_to_convert, camel_caps=False)
        >>> 'someVariableName'
        >>> convert_to_camel_case(strings_to_convert, camel_caps=True)
        >>> 'SomeVariableName'
    """
    logging.info(
        'Converting String Into Camel Case (camelCaps {0}): {1}'.format(
            camel_caps, string_to_convert
        )
    )

    words = re.findall("[a-zA-Z]+", string_to_convert)
    if camel_caps:
        return words[0].title() + ''.join([x.title() for x in words[1:]])
    else:
        return words[0] + ''.join([x.title() for x in words[1:]])


def convert_to_snake_case(string_to_convert):
    """
    Purpose:
        Convert Any string into snake_case. Special characters,
        numbers, and whitespace will be removed and replaced
        with a string with a _ between each work and all letters
        lower case.
    Args:
        string_to_convert (String): String convert to snake_case
    Returns:
        converted_string (String): String with snake_case
    Examples:
        >>> string_to_convert = 'Some Variable Name'
        >>> convert_to_title(strings_to_convert)
        >>> 'some_variable_name'
        >>> string_to_convert = 'SomeVariableName'
        >>> convert_to_title(strings_to_convert)
        >>> 'some_variable_name'
    """
    logging.info(
        'Converting String Into Snake Case: {0}'.format(string_to_convert)
    )

    words = re.findall("[A-Z][^A-Z]*", string_to_convert)
    return '_'.join([x.lower().strip() for x in words])
