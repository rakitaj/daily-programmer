from typing import Sequence, List
import re
import common

class Node(object):

    def __init__(self, name: str, weight: int, children: Sequence[str] = None, parent: str = None) -> None:
        self.name = name
        self.weight = weight
        if children is None:
            self.children = None
        else:
            self.children = tuple(children)
        self.parent = parent

    @classmethod
    def create(cls, text: str) -> 'Node':
        """
        Create a Node from the text given in Advent of Code 2017 day 7
        """
        result = None
        regex = re.compile(r"\((\d*)\)")
        if "->" in text:
            parts: List[str] = text.split("->")
            first_half_parts = parts[0].split()
            name = first_half_parts[0]
            weight = int(regex.match(first_half_parts[1]).groups()[0])
            children_raw = parts[1].split(",")
            children = [child.strip() for child in children_raw]
            result = Node(name, weight, children)
        else:
            parts = text.split()
            name = parts[0]
            weight = int(regex.match(parts[1]).groups()[0])
            result = Node(name, weight)
        return result

    def __eq__(self, other):
        if self.name == other.name and self.weight == other.weight and self.children == other.children and self.parent == other.parent:
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.name} ({self.weight}) -> {self.children}"

class Tree(object):
    """
    Representa a tree of the weighted node objects from Day 07. 
    """

    def __init__(self, nodes):
        self.nodes = nodes
        self.root = None
        self.build_tree()

    def build_tree(self):
        for n1 in self.nodes:
            for n2 in self.nodes:
                if n1.children != None and n2.name in n1.children:
                    n2.parent = n1.name
        for node in self.nodes:
            if node.parent == None:
                self.root = node
                break

    def print(self):
        print(self.root)

if __name__ == "__main__":
    lines = common.lines_from_text_file("day07_challenge_input.txt")
    nodes: List[Node] = list()
    for line in lines:
        nodes.append(Node.create(line))
    tree = Tree(nodes)
    tree.print()