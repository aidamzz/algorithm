# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def getMiddle(head):
            # This function will find the middle of the linked list
            if head is None:
                return head
            slow = head
            fast = head
            # Move fast by two steps and slow by one step to find the middle
            while fast.next is not None and fast.next.next is not None:
                slow = slow.next
                fast = fast.next.next
            return slow          
        def divideList(head):
            # Base case: when the list has zero or one element
            if head is None or head.next is None:
                return head

            middle = getMiddle(head)
            nextToMiddle = middle.next
            middle.next = None  # Correct way to split the list into two parts

            # Recursively divide the left and right parts
            left = divideList(head)
            right = divideList(nextToMiddle)

            # Merge the sorted halves
            return sortedMerge(left, right)
        def sortedMerge(left, right):
            result = None
            if left is None:
                return right
            if right is None:
                return left
            if left.val < right.val:
                result = left
                result.next = sortedMerge(left.next, right)
            else:
                result = right
                result.next = sortedMerge(left, right.next)
            return result
        return divideList(head)