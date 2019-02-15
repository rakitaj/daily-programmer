"""
Finally learn how to traverse trees in my sleep.
"""
from __future__ import annotations
from typing import Optional, List

class TreeNode():

    def __init__(self, x) -> None:
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class Solution:
    """Traverse a binary tree."""

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return self.preorder_iter(root)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.inorder_recurse(root)

    def preorder_recurse(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is not None:
            result.append(root.val)
            result.extend(self.preorder_recurse(root.left))
            result.extend(self.preorder_recurse(root.right))
        return result

    def preorder_iter(self, root: TreeNode) -> List[int]:
        result: List[int] = []
        stack: List[TreeNode] = [root]
        while len(stack) > 0:
            root = stack.pop()
            if root is not None:
                result.append(root.val)
                stack.append(root.right)
                stack.append(root.left)
        return result

    def inorder_recurse(self, root: TreeNode) -> List[int]:
        result = []
        if root is not None:
            result.extend(self.preorder_recurse(root.left))
            result.append(root.val)
            result.extend(self.preorder_recurse(root.right))
        return result

    def inorder_iter(self, root: TreeNode) -> List[int]:
        result: List[int] = []
        stack: List[TreeNode] = [root]
        while len(stack) > 0:
            root = stack.pop()
            if root is not None:
                stack.append(root.right)
                stack.append(root.left)
                result.append(root.val)
        return result
