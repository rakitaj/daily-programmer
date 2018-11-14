from typing import List

def container_most_water(numbers: List[int]) -> int:
    """Find the number combo which gives the container with the most water."""
    max_area = 0
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            area = calculate_area(numbers[i], numbers[j], j - i)
            if area > max_area:
                max_area = area
    return max_area

def calculate_area(height1, height2, distance):
    lower_bound = min(height1, height2)
    return lower_bound * distance
