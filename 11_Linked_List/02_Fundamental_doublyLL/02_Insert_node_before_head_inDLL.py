'''
Given the head of a doubly linked list and an integer X, insert a node with value X before the head of the linked list and return the head of the modified list.


Examples:
Input: head -> 1 <-> 2 <-> 3, X = 3

Output: head -> 3 <-> 1 <-> 2 <-> 3

Explanation: 3 was added before the 1st node. Note that the head's value is changed.

Input: head -> 5, X = 7

Output: head -> 7 <-> 5

Input: head -> 2 <-> 3, X = 10

Output:
head -> 10 <-> 2 <-> 3
Constraints:
n == Number of nodes in the Linked List
1 <= n <= 100
0 <= ListNode.val <= 100
0 <= X <= 100

Intuition:
Insert a new node at the beginning of a doubly linked list, create a new node, link it to the current head, make the new node the head, and adjust the previous pointer of the original head.
Approach:
Create a new node with the given value and set its back pointer to null and front pointer to the current head.
Update the current head's back pointer to point to the new node.
Return the new node as the updated head of the doubly linked list.

# Definition of doubly linked list
class ListNode:
    def __init__(self, data1=0, next1=None, prev1=None):
        self.val = data1
        self.next = next1
        self.prev = prev1

# Solution class
class Solution:
    #Function to insert a node before head in a doubly linked list 
    def insertBeforeHead(self, head, X):
        # Create new node which will be the new head
        newHead = ListNode(X, head, None)

        # Point the current head back to new one
        head.prev = newHead

        return newHead  # Return new head

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
    nums = [2, 3, 4, 5]

    # Creating the doubly linked list from given array
    head = arrayToLinkedList(nums)

    # Print the Original list
    print("Original List: ", end="")
    printLL(head)

    # Create an instance of Solution class
    sol = Solution()

    #Function call to insert a node before head in a doubly linked list 
    head = sol.insertBeforeHead(head, 1)

    # Print the Modified list
    print("Modified list: ", end="")
    printLL(head)
Complexity Analysis
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
    def insertBeforeHead(self, head, X):
        newHead = ListNode(X, head, None)
        head.prev = newHead
        return newHead