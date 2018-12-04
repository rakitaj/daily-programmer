from typing import List, Union
import sys


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next: ListNode = None

    def __repr__(self):
        if self.next is None:
            return f"{self.val}"
        else:
            return f"{self.val} -> {self.next.val}"

    def __eq__(self, other):
        if self.next is None:
            return self.val == other.val
        else:
            return self.val == other.val and self.next.val == other.next.val


class Solution:

    def __init__(self, lists: List[ListNode]) -> None:
        self.lists = lists
        self.sorted_list: Union[ListNode, None] = None

    def merge_lists(self) -> ListNode:
        min_node = self.dequeue_min_node()
        while min_node is not None:
            self.append_to_sorted_list(min_node)
            min_node = self.dequeue_min_node()
        return self.sorted_list

    def find_min_index(self) -> int:
        if len(self.lists) == 1:
            return self.lists[0].val
        else:
            min_index = 0
            min_value = sys.maxsize
            for index, node in enumerate(self.lists):
                if node is None:
                    continue
                else:
                    if node.val < min_value:
                        min_index = index
                        min_value = node.val
        return min_index

    def dequeue_min_node(self) -> ListNode:
        min_index = self.find_min_index()
        node = self.lists[min_index]
        if self.lists[min_index].next is None:
            del self.lists[min_index]
        else:
            self.lists[min_index] = self.lists[min_index].next
        return node

    def append_to_sorted_list(self, node: ListNode) -> None:
        if self.sorted_list is None:
            self.sorted_list = node
        else:
            last_node = Solution.get_last_node(self.sorted_list)
            last_node.next = node

    @staticmethod
    def get_last_node(node: ListNode) -> ListNode:
        current = node
        if current.next is None:
            return current
        else:
            while current.next is not None:
                current = current.next
            return current

    @staticmethod
    def all_none(lists) -> bool:
        for l in lists:
            if l is None:
                continue
            else:
                return False
        return True

    mergeKLists = merge_lists
