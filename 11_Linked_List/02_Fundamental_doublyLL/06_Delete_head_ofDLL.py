'''Given the head of a doubly linked list, remove the node at the head of the linked list and return the head of the modified list.



The head is the first node of the linked list.


Examples:
Input: head -> 1 <-> 2 <-> 3

Output: head -> 2 <-> 3

Explanation: The node with value 1 was removed.

Input: head -> 7

Output: head

Explanation: Note that the head has null value after the removal.

Input: head -> 2 <-> 4

Output:
head -> 4
Intuition:
Break the linkage of the current head to the Double Linked List, and return the next node as the new head.
Approach:
Set a pointer to the current head.
Make the next node the new head.
Remove the back pointer of the new head.
Remove the next pointer of the old head.
The new head is the result.
Note: In C++, explicitly delete the old head to free memory. In Java, Python garbage collection handles this.

Edge cases:
If the list is empty, return null.
If the list has only one node, delete it and return null.

# Definition of doubly linked list
class ListNode:
    def __init__(self, data1=0, next1=None, prev1=None):
        self.val = data1
        self.next = next1
        self.prev = prev1

# Solution class
class Solution:
    # Function to delete the head of the doubly linked list
    def deleteHead(self, head):
        if head is None or head.next is None:
            return None  # Return None if list is empty or has one node
        
        # Store current head as 'prev'
        prev = head
        # Move 'head' to next node
        head = head.next

        # Set 'prev' pointer
        head.prev = None

        # Set 'next' pointer
        prev.next = None

        # Return new head
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
    nums = [1, 2, 3, 4, 5]

    # Creating the doubly linked list from given array
    head = arrayToLinkedList(nums)

    # Print the Original list
    print("Original List: ", end="")
    printLL(head)

    # Create an instance of Solution class
    sol = Solution()

    # Function call to delete the head of the doubly linked list
    head = sol.deleteHead(head)

    # Print the Modified list
    print("Modified list: ", end="")
    printLL(head)
    
Complexity Analysis:
Time Complexity: O(1) because removing the head node from a doubly linked list is a constant-time operation. It's independent of the list's size, as it involves updating references to the head and the new head.

Space Complexity: O(1) as no extra space is used.'''
# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def deleteHead(self, head):
        if head is None or head.next is None:
            return None
        prev = head
        head = head.next
        head.prev = None
        prev.next = None
        return head