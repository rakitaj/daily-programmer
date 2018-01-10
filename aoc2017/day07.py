from typing import Sequence, List, Tuple
import re
import common

class Node(object):

    def __init__(self, name: str, weight: int, children: List[str] = None) -> None:
        self.name = name
        self.weight = weight
        self.children: List[str] = list()
        if children is not None:
            self.children.extend(children)
        self.parent = None
        self.child_nodes: List[Node] = list()

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
        return f"{self.name} ({self.weight}) \n-> {self.child_nodes}"

class Tree(object):
    """
    Representa a tree of the weighted node objects from Day 07.
    """

    def __init__(self, nodes: List[Node]) -> None:
        self.nodes = nodes
        self.root_node: Node = None
        self.build_tree()

    def build_tree(self):
        for node in self.nodes:
            for child_node_name in node.children:
                matching_nodes = self.nodes_with_name(child_node_name)
                node.child_nodes.extend(matching_nodes)
                for matching_node in matching_nodes:
                    matching_node.parent = node
        self.find_root(self.set_root_node)

    def nodes_with_name(self, name: str) -> List[Node]:
        result: List[Node] = list()
        for node in self.nodes:
            if node.name == name:
                result.append(node)
        return result

    def find_root(self, set_root_function) -> None:
        for node in self.nodes:
            if node.parent is None:
                set_root_function(node)
                break

    def set_root_node(self, value: Node) -> None:
        self.root_node = value

    @staticmethod
    def calculate_sub_weight(node: Node, accumulator: int) -> int:
        accumulator += node.weight
        if node.child_nodes is None or len(node.child_nodes) == 0:
            return accumulator
        else:
            for child_node in node.child_nodes:
                return Tree.calculate_sub_weight(child_node, accumulator)

    def print(self):
        print(self.root_node)

if __name__ == "__main__":
    lines = common.lines_from_text_file("C:\\Users\\joraki\\src\\daily-programmer\\aoc2017\day07_sample_input.txt")
    nodes: List[Node] = list()
    for line in lines:
        nodes.append(Node.create(line))
    tree = Tree(nodes)
    tree.print()
