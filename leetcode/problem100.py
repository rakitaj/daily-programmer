from __future__ import annotations


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_same_tree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True
        elif p and q:
            return (
                p.val == q.val and self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
            )
        else:
            return False
