from typing import List, Tuple


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next: ListNode = None


class Solution:

    def merge_lists(self, lists: List[ListNode]) -> ListNode:
        node, new_lists = self.min_and_dequeue(lists)
        start = ListNode(node.val)
        lists = new_lists
        while self.all_none(lists) is False:
            node, new_lists = self.min_and_dequeue(lists)
            lists = new_lists
            last_node = self.get_last_node(start)
            last_node.next = ListNode(node.val)
        return start

    def get_last_node(self, node: ListNode) -> ListNode:
        current = node
        if current.next is None:
            return current
        else:
            while current.next is not None:
                current = current.next
            return current

    @staticmethod
    def find_min_index(lists: List[ListNode]) -> int:
        length = len(lists)
        if length == 0:
            return -1
        elif length == 1:
            return 0
        else:
            min_index = 0
            for i in range(length):
                if lists[i] is not None and lists[i].val < lists[min_index].val:
                    min_index = i
            return min_index

    @staticmethod
    def min_and_dequeue(lists: List[ListNode]) -> Tuple[ListNode, List[ListNode]]:
        min_index = Solution.find_min_index(lists)
        min_node = lists[min_index]
        lists[min_index] = lists[min_index].next
        return (min_node, lists)

    @staticmethod
    def all_none(lists) -> bool:
        return all(x is None for x in lists)

    mergeKLists = merge_lists
