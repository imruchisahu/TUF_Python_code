'''Given a node's reference within a doubly linked list and an integer X, insert a node with value X before the given node in the linked list while preserving the list's integrity.



You will only be given the node's reference, not the head of the list. It is guaranteed that the given node will not be the head of the list.


Examples:
Input: head -> 1 <-> 2 <-> 6, node = 2, X = 7

Output: head -> 1 <-> 7 <-> 2 <-> 6

Explanation: Note that the head was not given to the function.

Input: head -> 7 <-> 5 <-> 5, node = 5 (node 3), X = 10

Output: head -> 7 <-> 5 <-> 10 <-> 5

Explanation: The last node with value 5 was referenced, thus the new node was added before the last node.

Input: head -> 7 <-> 6 <-> 5, node = 5, X = 10

Output:
head -> 7 <-> 6 <-> 10 <-> 5
Constraints:
n == Number of nodes in the Linked List
2 <= n <= 100
0 <= ListNode.val <= 100
0 <= X <= 100
It is guaranteed the given node will be a part of a doubly linked list and will not be its head.

Intuition:
Identify the preceding node, create a new node and insert it between the identified node and its successor, then readjust links.
Approach:
Track the node to which the back pointer of the referenced node is pointing, and call it the previous node.
Create a new node with its data as the given value, its back pointer as the previous node, and its next pointer as the referenced node.
Update the next pointer of the previous node to point to the newly created node.

# Definition of doubly linked list
class ListNode:
    def __init__(self, data1=0, next1=None, prev1=None):
        self.val = data1
        self.next = next1
        self.prev = prev1

# Solution class
class Solution:
#Function to insert a new node before given node in a doubly linked list 
    def insertBeforeGivenNode(self, node, X):
        # Get node before the given node
        prev = node.prev

        # Create new node
        newNode = ListNode(X, node, prev)

        # Connect newNode
        prev.next = newNode
        node.prev = newNode

        # void function to just update
        return

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
    nums = [1, 2, 4, 5]

    # Creating the doubly linked list from given array
    head = arrayToLinkedList(nums)

    # Node before which the new node must be inserted
    node = head.next.next

    # Print the Original list
    print("Original List: ", end="")
    printLL(head)

    # Create an instance of Solution class
    sol = Solution()

    #Function call to insert a new node before given node in a doubly linked list 
    sol.insertBeforeGivenNode(node, 3)

    # Print the Modified list
    print("Modified list: ", end="")
    printLL(head)
Complexity Analysis:
Time Complexity: O(1) because only a constant number of pointer updates are being performed regardless of the size of the Doubly Linked List.

Space Complexity: O(1) as no extra space is used.
'''
# Definition of doubly linked list:
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def insertBeforeGivenNode(self, node, X):
        prev = node.prev

        # Create new node
        newNode = ListNode(X, node, prev)

        # Connect newNode
        prev.next = newNode
        node.prev = newNode
        return