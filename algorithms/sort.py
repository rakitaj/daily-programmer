"""
Collection of user created sorting functions.
"""
from typing import List

def in_place_swap(elements: List, i: int, j: int):
    temp = elements[i]
    elements[i] = elements[j]
    elements[j] = temp

def bubble_sort(elements: List) -> List:
    length = len(elements)
    for i in range(0, length):
        for j in range(i, length):
            if elements[i] > elements[j]:
                in_place_swap(elements, i, j)
    return elements

def insertion_sort(elements: List) -> List:
    length = len(elements)
    for i in range(1, length):
        for j in range(i, -1, -1):
            if elements[i] > elements[j]:
                in_place_swap(elements, i, j)
    return elements
