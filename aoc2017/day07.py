from typing import Sequence, List
import common

class TowerPrimative(object):

    def __init__(self, name: str, weight: int, children: Sequence[str]) -> None:
        self.name = name
        self.weight = weight
        if children is None:
            self.children = None
        else:
            self.children = tuple(children)
        

    def __eq__(self, other) -> bool:
        if self.name != other.name or self.weight != other.weight:
            return False
        for i, item in enumerate(self.children):
            if self.children[i] != other.children[i]:
                return False
        return True

    def __repr__(self):
        return f"{self.name} ({self.weight}) -> {self.children}"

    @classmethod
    def create(cls, text: str) -> 'TowerPrimative':
        name = text[:4].strip()
        weight = text[6:8]
        if "->" in text:
            children = text[13:].split(",")
            children = [child.strip() for child in children]
        else:
            children = None
        return cls(name, int(weight), children)

    @classmethod
    def create_all(cls, path: str) -> Sequence['TowerPrimative']:
        lines = common.lines_from_text_file(path)
        tower_primatives: List['TowerPrimative'] = list()
        for line in lines:
            tower_primatives.append(cls.create(line))
        return tower_primatives

if __name__ == "__main__":
    towers = TowerPrimative.create_all("day07_input_sample.txt")
    for tower in towers:
        print(tower)
    tower = Tower.assemble(towers)
    print(tower)