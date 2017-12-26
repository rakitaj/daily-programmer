from typing import List

def generate_spiral_sequence(num_terms: int):
    current, counter = 0, 0
    number_repeated = False
    while counter < num_terms:
        if number_repeated is False:
            current += 1
            number_repeated = True
        else:
            number_repeated = False
        counter += 1
        yield current

class SpiralMemory(object):

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.matrix: List[List[int]] = list(list())
        self.memory_matrix = self.create()

    def create(self):
        counter = 0
        current_position = [0][0]
        for i in generate_spiral_sequence(capacity):
            if counter % 4 == 0:
                self.matrix.append()
            elif counter % 4 == 1:
                pass
            elif counter % 4 == 2:
                pass
            else:
                pass

def manhattan_path(x_pos: int, y_pos: int) -> int:
    return abs(x_pos) + abs(y_pos)
