import heapq

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        class HeapNode:
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val

        min_heap = []
        dummy = ListNode(0)
        current = dummy

        # Initialize the heap with the head of each list
        for head in lists:
            if head:
                heapq.heappush(min_heap, HeapNode(head))
        
        # Merge the lists
        while min_heap:
            smallest_node = heapq.heappop(min_heap)
            current.next = smallest_node.node
            current = current.next
            if smallest_node.node.next:
                heapq.heappush(min_heap, HeapNode(smallest_node.node.next))

        return dummy.next