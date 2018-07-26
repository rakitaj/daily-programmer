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
        for j in range(i, 0, -1):
            if elements[j-1] > elements[j]:
                in_place_swap(elements, j, j-1)
    return elements

def selection_sort(elements: List) -> List:
    length = len(elements)
    for i in range(0, length):
        j = find_min_element_index(elements, i)
        in_place_swap(elements, i, j)
    return elements

def find_min_element_index(elements: List, start: int) -> int:
    min_index = start
    min_value = elements[start]
    for i in range(start, len(elements)):
        if elements[i] < min_value:
            min_value = elements[i]
            min_index = i
    return min_index
