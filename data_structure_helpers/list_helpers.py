#!/usr/bin/env python3
"""
    Purpose:
        Provide List Helper Functions
"""

# Python Library Imports
import logging
import random


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

    sorted_list = []
    list_1_idx, list_2_idx, sorted_list_idx = 0, 0, 0

    while list_1_idx < len(list_1) and list_2_idx < len(list_2):
        if list_1[list_1_idx] < list_2[list_2_idx]:
            sorted_list.append(list_1[list_1_idx])
            list_1_idx += 1
        else:
            sorted_list.append(list_2[list_2_idx])
            list_2_idx += 1

    if list_1_idx < len(list_1):
        while list_1_idx < len(list_1):
            sorted_list.append(list_1[list_1_idx])
            list_1_idx += 1

    if list_2_idx < len(list_2):
        while list_2_idx < len(list_2):
            sorted_list.append(list_2[list_2_idx])
            list_2_idx += 1

    return sorted_list


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

    randomized_list = []

    if not list_size:
        list_size = random.randint(1, 50)

    for x in range(list_size):
        randomized_list.append(
            random.randint(0, 10000)
        )

    return list(set(randomized_list))


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

    return list(set(original_list))


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

    temp = unsorted_list[index_1]
    unsorted_list[index_1] = unsorted_list[index_2]
    unsorted_list[index_2] = temp

    return


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

    temp = unsorted_list[index_1]
    unsorted_list[index_1] = unsorted_list[index_2]
    unsorted_list[index_2] = temp

    return
