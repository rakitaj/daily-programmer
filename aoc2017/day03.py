class SpiralMemorySequence(object):

    def __init__(self, start_value:int = 0) -> None:
        self.counter = start_value
        self.num_repeated = False

    def next(self):
        current = self.counter
        if current == 0:
            self.counter += 1
            self.num_repeated = True
            return 0
        elif self.num_repeated is False:
            self.counter += 1
            self.num_repeated = True
            return current
        else:
            self.num_repeated = False
            return current

class SpiralMemory(object):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.memory_matrix = self.create()

    def create(self):
        pass

def manhattan_path(x_pos: int, y_pos: int) -> int:
    return abs(x_pos) + abs(y_pos)