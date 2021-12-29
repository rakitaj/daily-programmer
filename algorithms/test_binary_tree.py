"""Tests for binary trees."""
import pytest
from typing import Callable
from .binary_tree import TreeNode, Solution


def create_tree_1() -> TreeNode[int]:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    return root


def create_tree_2() -> TreeNode[int]:
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    return root


@pytest.mark.parametrize(
    "tree_func, algorithm_func",
    [
        (create_tree_1, Solution().preorder_iter),
        (create_tree_2, Solution().preorder_iter),
        (create_tree_1, Solution().preorder_recurse),
        (create_tree_2, Solution().preorder_recurse),
    ],
)
def test_preorder_traversal(
    tree_func: Callable[[], TreeNode[int]], algorithm_func: Callable[[TreeNode[int]], list[int]]
):
    tree = tree_func()
    assert algorithm_func(tree) == [1, 2, 3]


@pytest.mark.parametrize(
    "tree_func, algorithm_func, expected",
    [
        (create_tree_1, Solution().inorder_recurse, [2, 1, 3]),
        (create_tree_2, Solution().inorder_recurse, [1, 2, 3]),
        (create_tree_1, Solution().inorder_iter, [2, 1, 3]),
        (create_tree_2, Solution().inorder_iter, [1, 3, 2]),
    ],
)
def test_inorder_traversal(
    tree_func: Callable[[], TreeNode[int]],
    algorithm_func: Callable[[TreeNode[int]], list[int]],
    expected: list[int],
):
    tree = tree_func()
    assert algorithm_func(tree) == expected
