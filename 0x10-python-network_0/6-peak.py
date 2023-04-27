#!/usr/bin/python3
"""
Contains function that finds the peak of a list of integer
"""


def find_peak(list_of_integers):
    """
    Finds the peak of a list of integers
    Args:
    list: list_of_integers
    Returns:
    int: peak if list is not empty else None
    """
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
