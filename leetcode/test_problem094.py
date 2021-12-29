import pytest
from leetcode.problem094 import TreeNode, Solution


@pytest.fixture
def example1() -> TreeNode[int]:
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    return root


@pytest.fixture
def breadth_first_example() -> TreeNode[int]:
    root = TreeNode(10)
    root.left = TreeNode(4)
    root.right = TreeNode(17)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(9)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(18)
    return root


def test_in_order_traversal_recursive(example1: TreeNode[int]):
    result = Solution().in_order_traversal(example1)
    assert result == [1, 3, 2]


@pytest.mark.skip
def test_in_order_traversal_iterative(example1: TreeNode[int]):
    result = Solution().in_order_traversal_iter(example1)
    assert result == [1, 3, 2]


def test_breadth_first_traversal(breadth_first_example: TreeNode[int]):
    result = Solution().breadth_first(breadth_first_example)
    assert result == [10, 4, 17, 1, 9, 12, 18]
