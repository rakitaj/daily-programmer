from typing import List


class Problem011:

    def container_most_water(self, numbers: List[int]) -> int:
        """Find the number combo which gives the container with the most water."""
        max_area = 0
        for i in range(len(numbers)):
            for j in range(i, len(numbers)):
                area = self.calculate_area(numbers[i], numbers[j], j - i)
                if area > max_area:
                    max_area = area
        return max_area

    def container_most_water_linear(self, numbers: List[int]) -> int:
        """Find the number combo which gives the container with the most water
        use a linear algorithm that contracts from both sides."""
        max_area = 0
        start = 0
        end = len(numbers) - 1
        while start != end:
            area = self.calculate_area(numbers[start], numbers[end], end - start)
            if area > max_area:
                max_area = area
            if numbers[start] <= numbers[end]:
                start += 1
            else:
                end -= 1
        return max_area

    def calculate_area(self, height1, height2, distance):
        lower_bound = min(height1, height2)
        return lower_bound * distance
