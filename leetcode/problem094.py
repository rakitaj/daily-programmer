# from __future__ import annotations
from typing import Generic, TypeVar

T = TypeVar("T")


class TreeNode(Generic[T]):
    """Definition for a binary tree node."""

    def __init__(self, x: T):
        self.val = x
        self.left: TreeNode[T] | None = None
        self.right: TreeNode[T] | None = None


class Solution:
    def in_order_traversal_iter(self, root: TreeNode[int]) -> list[int]:
        result: list[int] = []
        stack: list[TreeNode[int] | None] = [root]
        while 0 < len(stack):
            current = stack.pop()
            if current:
                result.append(current.val)
                stack.append(current.right)
                stack.append(current.left)
        return result

    def in_order_traversal(self, root: TreeNode[int]) -> list[int]:
        accumulator: list[int] = list()
        self.in_order_helper(root, accumulator)
        return accumulator

    def in_order_helper(self, node: TreeNode[int] | None, accumulator: list[int]):
        if node:
            self.in_order_helper(node.left, accumulator)
            accumulator.append(node.val)
            self.in_order_helper(node.right, accumulator)

    def breadth_first(self, root: TreeNode[int]) -> list[int]:
        result: list[int] = list()
        queue: list[TreeNode[int]] = [root]
        while 0 < len(queue):
            current = queue.pop(0)
            result.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result
