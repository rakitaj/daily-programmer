from typing import List
from .problem023 import Solution, ListNode


def test_min_of_lists_flat_3():
    lists: List[ListNode] = [ListNode(12), ListNode(3), ListNode(15)]
    solution = Solution(lists)
    assert solution.find_min_index() == 1


def test_lists_all_none_should_be_true_when_every_list_element_is_none():
    lists = [None, None, None, None, None]
    assert Solution.all_none(lists) is True


def test_lists_all_none_should_be_false_when_any_element_is_not_none():
    lists = [None, None, None, ListNode(50000)]
    assert Solution.all_none(lists) is False


def test_min_and_remove():
    ln_1 = ListNode(1)
    ln_2 = ListNode(2)
    ln_3 = ListNode(3)
    ln_1.next = ln_3
    lists: List[ListNode] = [ln_1, ln_2]
    solution = Solution(lists)
    assert solution.dequeue_min_node() == ln_1
    assert solution.lists == [ln_3, ln_2]
    assert solution.dequeue_min_node() == ln_2
    assert solution.lists == [ln_3]


def test_get_last_node():
    ln_0 = ListNode(0)
    ln_1 = ListNode(1)
    ln_2 = ListNode(2)
    ln_0.next = ln_1
    ln_1.next = ln_2
    assert Solution.get_last_node(ln_0) == ln_2


def test_merge_lists():
    ln_1 = ListNode(1)
    ln_2 = ListNode(2)
    ln_3 = ListNode(3)
    ln_1.next = ln_3
    lists: List[ListNode] = [ln_1, ln_2]
    solution = Solution(lists)
    result = solution.merge_lists()
    assert result.val == ln_1.val
    assert result.next.val == ln_2.val
    assert result.next.next.val == ln_3.val


def test_merge_lists_2():
    """The test data from leetcode."""
    # [[1,4,5],[1,3,4],[2,6]]
    # [1,1,2,3,4,4,5,6]
    ll_1 = ListNode(1)
    ll_1.next = ListNode(4)
    ll_1.next.next = ListNode(5)

    ll_2 = ListNode(1)
    ll_2.next = ListNode(3)
    ll_2.next.next = ListNode(4)

    ll_3 = ListNode(2)
    ll_3.next = ListNode(6)

    expected = ListNode(1)
    expected.next = ListNode(1)
    expected.next.next = ListNode(2)
    expected.next.next = ListNode(3)
    expected.next.next.next = ListNode(4)
    expected.next.next.next.next = ListNode(4)
    expected.next.next.next.next.next = ListNode(5)
    expected.next.next.next.next.next.next = ListNode(6)

    solution = Solution([ll_1, ll_2, ll_3])
    result = solution.merge_lists()

    assert result == expected
