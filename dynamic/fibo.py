from typing import List, Dict

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

solved: Dict[int, int] = dict()
solved[0] = 0
solved[1] = 1


def fibonacci_dynamic(n: int) -> int:
    if n in solved:
        return solved[n]
    else:
        solved[n] = fibonacci_dynamic(n - 1) + fibonacci_dynamic(n - 2)
        return solved[n]

print(fibonacci_dynamic(40))