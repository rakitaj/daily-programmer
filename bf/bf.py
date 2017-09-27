class Tape:
    def __init__(self):
        self.thetape = [0]
        self.position = 0

    def get(self):
        return self.thetape[self.position]

    def set(self, value):
        self.thetape[self.position] = value

    def advance(self):
        self.position += 1
        if self.position >= len(self.thetape):
            self.thetape.append(0)

    def devance(self):
        self.position -= 1
        if self.position < 0:
            self.position = 0

    def increment(self):
        self.thetape[self.position] += 1

    def decrement(self):
        self.thetape[self.position] -= 1


def mainloop(program, bracket_map):
    tape = Tape()
    pc = 0
    while pc < len(program):
        code = program[pc]

        if code == ">":
            tape.advance()
        elif code == "<":
            tape.devance()
        elif code == "+":
            tape.increment()
        elif code == "-":
            tape.decrement()
        elif code == ".":
            sys.stdout.write(chr(tape.get()))
        elif code == ",":
            tape.set(ord(sys.stdin.read(1)))
        elif code == "[" and value() == 0:
            pos = bracket_map[left]
        elif code == "]" and value() != 0:
            pos = bracket_map[right]
        else:
            raise Exception("Invalid source code symbol")
        
        pc = pc + 1

def parse(program):
    parsed = []
    bracket_map = []
    leftstack = []
    pc = 0
    for char in program:
        if char in [">", "<", "+", "-", ".", ",", "[", "]"]:
            parsed.append(char)
            if char == "[":
                leftstack.append(pc)
            elif char == "]":
                left = leftstack.pop()
                right = pc
                bracket_map[left] = right
                bracket_map[right] = left
            pc += 1
    return "".join(parsed), bracket_map

def run(input):
    program, bracket_map = parse(input.read())
    mainloop(program, bracket_map)

if __name__ == "__main__":
    import sys
    run(open(sys.argv[1], 'r'))