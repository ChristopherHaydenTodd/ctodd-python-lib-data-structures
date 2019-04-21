# Christopher H. Todd's Python Library For Interacting With and Creating Python Datastructures

The ctodd-python-lib-data-structures project is responsible for aiding interacting with Pythons base datastructures, creating higher level data structures for projects and code, and other misc tasks. Example would be flattening out a python dict.

The library utilizes Python's built in datastrctures and some libraries (like Anytree) to generate new data sctructures. this can be useful for repetitive tasks or aiding with testing code and algorithms.

## Table of Contents

- [Dependencies](#dependencies)
- [Libraries](#libraries)
- [Example Scripts](#example-scripts)
- [Notes](#notes)
- [TODO](#todo)

## Dependencies

### Python Packages

- anytree>=2.6.0

## Libraries

### (dict_helpers.py)[https://github.com/ChristopherHaydenTodd/ctodd-python-lib-data-structures/blob/master/data_structure_helpers/dict_helpers.py]

Provide Dictionary Helper Functions

Functions:

```
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
```


### (linked_list.py)[https://github.com/ChristopherHaydenTodd/ctodd-python-lib-data-structures/blob/master/data_structure_helpers/linked_list.py]

Linked List Class for Link List DataTypes in Python

Examples of Create Object of Class:
```
    linked_list_object = LinkedList()
```

Classes:

```
class LinkedList(object):
    """
        LinkedList Class
    """
```

### (linked_list_node.py)[https://github.com/ChristopherHaydenTodd/ctodd-python-lib-data-structures/blob/master/data_structure_helpers/linked_list_node.py]

Nodes Supporting the Linked List DataTypes in Python

Examples of Create Object of Class:
```
linked_list_node_object = LinkedListNode()
```

Classes:

```
class LinkedListNode(object):
    """
        LinkedListNode Class
    """
```

### (list_helpers.py)[https://github.com/ChristopherHaydenTodd/ctodd-python-lib-data-structures/blob/master/data_structure_helpers/list_helpers.py]

Provide List Helper Functions

Functions:

```
def merge_two_sorted_lists(list_1, list_2):
    """
    Purpose:
        Merge two sorted lists into one sorted list
    Args:
        list_1 (List): Sorted List to Merge
        list_2 (List): Sorted List to Merge
    Returns:
        sorted_list (List): Merged Sorted List
    """
```

```
def generate_unique_randomized_list(list_size=None):
    """
    Purpose:
        Generate a Randomized List with Unique Values
        of a sepcified size
    Args:
        list_size (Int): Size of list to generate. Lists
        default to 50 ints
    Returns:
        randomized_list (List): Unsorted and randomized
        list
    """
```

```
def remove_duplicates(original_list):
    """
    Purpose:
        Remove Duplicates in a List in Python (convert to set and
        back to a list)
    Args:
        original_list (Int): List with duplicates
    Returns:
        unique_list (List): List with duplicates removed
    """
```

```
def perform_list_swap(unsorted_list, index_1, index_2):
    """
    Purpose:
        Swap values in a list by reference. Utilizes
        a temp varilable and swaps any two values
        based on passed in indexes
    Args:
        unsorted_list (List): List to perform swap on
        index_1 (List Index, as Int): index position to swap
        index_2 (List Index, as Int): index position to swap
    Returns:
        unsorted_list (List): List with indexes swapped
    """
```

```
def get_list_intersection(list_1, list_2):
    """
    Purpose:
        Check for intersecting objects in two lists
    Args:
        list_1 (List of Objects): List with Objects
        list_2 (List of Objects): List with Objects
    Returns:
        intesecting_values (List of Objects): List with objects
            that appear in both lists
    """
```

### (string_helpers.py)[https://github.com/ChristopherHaydenTodd/ctodd-python-lib-data-structures/blob/master/data_structure_helpers/string_helpers.py]

Modify and Work with Strings

Functions:

```
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
```

```
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
```

```
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
```


### (tree.py)[https://github.com/ChristopherHaydenTodd/ctodd-python-lib-data-structures/blob/master/data_structure_helpers/tree.py]

Generate Tree for testing and traversal

Functions:

```
def generate_tree(node_count, max_depth, max_children):
    """
    Purpose:
        Generate A Random Tree
    Args:
        node_count (Int): Count of nodes in generated tree
        max_depth (Int): Max depth of tree
        max_children (Int): Max children per node
    Returns:
        root_node (Node Obj): Root node of the tree
        nodes (Dict of Node Obj): Nodes in the tree
    """
```

## Example Scripts

Example executable Python scripts/modules for testing and interacting with the library. These show example use-cases for the libraries and can be used as templates for developing with the libraries or to use as one-off development efforts.

### N/A

## Notes

 - Relies on f-string notation, which is limited to Python3.6.  A refactor to remove these could allow for development with Python3.0.x through 3.5.x

## TODO

 - Unittest framework in place, but lacking tests
