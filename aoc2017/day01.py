import common

class IterableNumber(object):

    def __init__(self, value: int) -> None:
        self.value = str(value)
        self.position = 0
        self.cycled = False

    def advance(self):
        if self.position + 1 == len(self.value):
            self.cycled = True
            self.position = 0
        else:
            self.position += 1

    def get(self, offset: int = 0):
        if self.position + offset < len(self.value):
            return int(self.value[self.position + offset])
        else:
            return int(self.value[self.position + offset - len(self.value)])

    def reset(self):
        self.position = 0


def inverse_captcha(offset:int, input_number: int) -> int:
    sum = 0
    number = IterableNumber(input_number)
    while number.cycled is False:
        current = number.get()
        next = number.get(offset)
        number.advance()
        if current == next:
            sum += number.get()
    return sum

if __name__ == "__main__":
    challenge_input = common.number_from_text_file("day01_input.txt")
    print(inverse_captcha(1, challenge_input))
