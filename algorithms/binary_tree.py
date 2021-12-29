"""
Finally learn how to traverse trees in my sleep.
"""
from __future__ import annotations
from typing import Generic, TypeVar

T = TypeVar("T")


class TreeNode(Generic[T]):
    def __init__(self, x: T) -> None:
        self.val = x
        self.left: TreeNode[T] | None = None
        self.right: TreeNode[T] | None = None


class Solution:
    """Traverse a binary tree."""

    def preorderTraversal(self, root: TreeNode[int]) -> list[int]:
        return self.preorder_iter(root)

    def inorderTraversal(self, root: TreeNode[int]) -> list[int]:
        return self.inorder_recurse(root)

    def preorder_recurse(self, root: TreeNode[int] | None) -> list[int]:
        result: list[int] = []
        if root is not None:
            result.append(root.val)
            result.extend(self.preorder_recurse(root.left))
            result.extend(self.preorder_recurse(root.right))
        return result

    def preorder_iter(self, root: TreeNode[int]) -> list[int]:
        result: list[int] = []
        stack: list[TreeNode[int] | None] = [root]
        node: TreeNode[int] | None = root
        while len(stack) > 0:
            node = stack.pop()
            if node is not None:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return result

    def inorder_recurse(self, root: TreeNode[int]) -> list[int]:
        result: list[int] = []
        if root is not None:
            result.extend(self.preorder_recurse(root.left))
            result.append(root.val)
            result.extend(self.preorder_recurse(root.right))
        return result

    def inorder_iter(self, root: TreeNode[int]) -> list[int]:
        result: list[int] = []
        stack: list[TreeNode[int]] = []
        node: TreeNode[int] | None = root
        while 0 < len(stack) or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result
