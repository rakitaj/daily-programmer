from typing import List

def true_for_all(items: List, func) -> bool:
    for item in items:
        result = func(item)
        if result is not True:
            return False
    return True
