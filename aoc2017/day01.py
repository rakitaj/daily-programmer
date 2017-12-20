import common

class IterableNumber(object):

    def __init__(self, value: int) -> None:
        self.value = str(value)
        self.position = 0
        self.cycled = False

    def current(self) -> int:
        return int(self.value[self.position])

    def advance(self):
        if self.position + 1 == len(self.value):
            self.cycled = True
            self.position = 0
        else:
            self.position += 1

    def reset(self):
        self.position = 0


def inverse_captcha(input_number: int) -> int:
    sum = 0
    number = IterableNumber(input_number)
    while number.cycled is False:
        current = number.current()
        number.advance()
        next = number.current()
        if current == next:
            sum += number.current()
    return sum

if __name__ == "__main__":
    challenge_input = common.number_from_text_file("day01_input.txt")
    print(inverse_captcha(challenge_input))
