import common

class IterableNumber(object):

    def __init__(self, value: int) -> None:
        self.value = str(value)
        self.position = 0
        self.cycled = False

    def next(self) -> int:
        if self.position + 1 == len(self.value):
            self.cycled = True
            return int(self.value[self.position])
        else:
            self.position += 1
            return int(self.value[self.position])

    def reset(self):
        self.position = 0


def inverse_captcha(input_number: int) -> int:
    sum = 0
    string_number = str(input_number)
    for i in range(0, len(string_number)):
        if i + 1 == len(string_number):
            if string_number[i] == string_number[0]:
                sum += int(string_number[i])
        else:
            if string_number[i] == string_number[i + 1]:
                sum += int(string_number[i])
    return sum

if __name__ == "__main__":
    number = common.number_from_text_file("day01_input.txt")
    print(inverse_captcha(number))
