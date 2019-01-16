from typing import List, Sequence

class Solution:

    def is_valid(self, s: str) -> bool:
        opened_stack: List[str] = list()
        for char in s:
            if char == "(" or char == "[" or char == "{":
                opened_stack.append(char)
            else:
                if empty(opened_stack):
                    return False
                else:
                    most_recent_opened = opened_stack.pop()
                if (char == ")" and most_recent_opened == "(") or (char == "]" and most_recent_opened == "[") or (char == "}" and most_recent_opened == "{"):
                    pass
                else:
                    return False
        return empty(opened_stack)

    def char_closes(self, opening_char, closing_char) -> bool:
        return opening_char == "(" and closing_char == ")"

    isValid = is_valid


def empty(iterable) -> bool:
    return len(iterable) == 0
