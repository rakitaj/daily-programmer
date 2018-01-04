from typing import Sequence, Dict, Tuple
import common

class Cycle(object):

    def __init__(self, count: int, previous_dupe: int) -> None:
        self.count = count
        self.previous_dupe = previous_dupe

    def __str__(self):
        return f"Total count: {self.count}\nFrom previous duplicate: {self.previous_dupe}"

def memory_cycles(memory_banks: Sequence[int]) -> Cycle:
    memory_banks = tuple(memory_banks)
    previous_states: Dict[Tuple[int, ...], int] = {}
    counter = 0
    while memory_banks not in previous_states:
        previous_states[memory_banks] = counter
        memory_banks = balance(memory_banks)
        counter += 1
    return Cycle(counter, counter - previous_states[memory_banks])

def balance(memory_banks: Sequence[int]) -> Sequence[int]:
    mut_memory_banks = list(memory_banks)
    index, max_value = max(enumerate(memory_banks), key=lambda p: p[1])
    mut_memory_banks[index] = 0
    for i in range(max_value):
        j = (i + index + 1) % len(mut_memory_banks)
        mut_memory_banks[j] += 1
    return tuple(mut_memory_banks)

if __name__ == "__main__":
    challenge_input = common.numbers_from_text_file("day06_input.txt")
    print(memory_cycles(challenge_input))
