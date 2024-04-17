class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
    def sortedMerge(self, left, right):
        result = None
        if left is None:
            return right
        if right is None:
            return left
        if left.data < right.data:
            result = left
            result.next = self.sortedMerge(left.next, right)
        else:
            result = right
            result.next = self.sortedMerge(left, right.next)
        return result
    def divideAndMerge(self, head):
        if head is None or head.next is None:
            return head
        
        middle = self.getMiddle(head)
        nextToMiddle = middle.next
        middle.next = None

        left = self.divideAndMerge(head)
        right = self.divideAndMerge(nextToMiddle)
        return self.sortedMerge(left, right)

    def getMiddle(self, head):
        if head == None:
            return head
        slow = head
        fast = head
        while(fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow
def printList(head):
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next
    print()

# Create and sort linked list
li = LinkedList()
li.append(15)
li.append(10)
li.append(5)
li.append(20)
li.append(3)
li.append(2)

# Sort the linked list
li.head = li.divideAndMerge(li.head)

# Output the sorted linked list
print("Sorted Linked List is:")
printList(li.head)


    

