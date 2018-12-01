from typing import List
from .problem023 import Solution, ListNode


def test_min_of_lists_flat_3():
    lists: List[ListNode] = [ListNode(12), ListNode(3), ListNode(15)]
    min_index = Solution.find_min_index(lists)
    assert min_index == 1


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
    result = Solution.min_and_dequeue(lists)
    assert result[0].val == ln_1.val
    assert result[1] == [ln_3, ln_2]


def test_get_last_node():
    ln_0 = ListNode(0)
    ln_1 = ListNode(1)
    ln_2 = ListNode(2)
    ln_0.next = ln_1
    ln_1.next = ln_2
    assert Solution().get_last_node(ln_0) == ln_2


def test_merge_lists():
    ln_1 = ListNode(1)
    ln_2 = ListNode(2)
    ln_3 = ListNode(3)
    ln_1.next = ln_3
    lists: List[ListNode] = [ln_1, ln_2]
    result = Solution().merge_lists(lists)
    assert result.val == ln_1.val
    assert result.next.val == ln_2.val
    assert result.next.next.val == ln_3.val
