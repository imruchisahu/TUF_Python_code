'''
Given the head of a doubly linked list and an integer X, insert a node with value X before the tail of the linked list and return the head of the modified list.


Examples:
Input: head -> 1 <-> 2 <-> 4, X = 3

Output: head -> 1 <-> 2 <-> 3 <-> 4

Explanation: 3 was added before the last node.

Input: head -> 4, X = 6

Output: head -> 6 <-> 4

Explanation: 6 was added before 4, note that the head was changed as a result.

Input: head -> 4 <-> 5, X = 6

Output:
head -> 4 <-> 6 <-> 5
Constraints:
n == Number of nodes in the Linked List
1 <= n <= 100
0 <= ListNode.val <= 100
0 <= X <= 100

Intuition:
Inserting a node before the tail of a doubly linked list involves traversing the list to locate the second-to-last node. Once found, a new node is created, and the pointers of the adjacent nodes are updated to place the new node correctly before the tail. This maintains the list structure and ensures the new node is properly integrated.
Approach:
Traverse to the tail of the linked list, keeping track of both the tail and the node previous to the tail.
Create a new node with the given value, setting its next pointer to the tail and its back pointer to the previous node.
Update the next pointer of the previous node to point to the new node and the back pointer of the tail to point to the new node, effectively inserting the new node before the tail.

# Definition of doubly linked list
class ListNode:
    def __init__(self, data1=0, next1=None, prev1=None):
        self.val = data1
        self.next = next1
        self.prev = prev1

# Solution class
class Solution:
    #Function to insert a node before tail of a doubly linked list 
    def insertBeforeTail(self, head, X):
        # Edge case
        if head.next is None:
            # Create new node with data as X
            newHead = ListNode(X, head, None)
            head.prev = newHead
            return newHead

        # Create pointer tail
        tail = head
        while tail.next is not None:
            tail = tail.next

        # Keep track of node before tail using prev
        prev = tail.prev

        # Create new node with value X
        newNode = ListNode(X, tail, prev)

        # Join the new node
        prev.next = newNode
        tail.prev = newNode

        # Return updated linked list
        return head

# Helper Function to convert an array to a doubly linked list
def arrayToLinkedList(nums):
    # If array is empty, return None
    if not nums:
        return None

    # Create head node with first element of the array
    head = ListNode(nums[0])
    # Initialize 'prev' to the head node
    prev = head

    for i in range(1, len(nums)):
        # Create a new node
        temp = ListNode(nums[i], None, prev)
        # Update 'next' pointer
        prev.next = temp
        # Move 'prev' to newly created node
        prev = temp

    # Return head
    return head

# Helper Function to print the linked list
def printLL(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()

if __name__ == "__main__":
    nums = [1, 2, 3, 5]

    # Creating the doubly linked list from given array
    head = arrayToLinkedList(nums)

    # Print the Original list
    print("Original List: ", end="")
    printLL(head)

    # Create an instance of Solution class
    sol = Solution()

    #Function call to insert a node before tail of a doubly linked list 
    head = sol.insertBeforeTail(head, 4)

    # Print the Modified list
    print("Modified list: ", end="")
    printLL(head)
Complexity Analysis:
Time Complexity: O(N) where N is the length of the array. We iterate through the input array exactly once and at each element perform constant time operations.

Space Complexity: O(1) as no extra space is used.

'''
# Definition of doubly linked list:
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def insertBeforeTail(self, head, X):
        if head.next is None:
            newHead = ListNode(X, head, None)
            head.prev = newHead
            return newHead

        # Create pointer tail
        tail = head
        while tail.next is not None:
            tail = tail.next
        prev = tail.prev
        newNode = ListNode(X, tail, prev)
        prev.next = newNode
        tail.prev = newNode
        return head
