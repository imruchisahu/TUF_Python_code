'''Given a node's reference within a doubly linked list, remove that node from the linked list while preserving the list's integrity.



You will only be given the node's reference, not the head of the list. It is guaranteed that the given node will not be the head of the list. For the custom testcase, give the index(0-indexed) of the node to be removed.


Examples:
Input: head -> 1 <-> 3 <-> 5, node = 3

Output: head -> 1 <-> 5

Explanation: The referenced node with value 3 was removed.

Input: head -> 1 <-> 3 <-> 7, node = 7

Output: head -> 1 <-> 3

Explanation: The referenced node with value 7 was removed.

Input: head -> 1 <-> 5, node = 5

Output:
head -> 1
Constraints:
2 <= Number of nodes in the list <= 100
0 <= ListNode.val <= 100
Node is guaranteed to be a part of the linked list and will not be the head

Intuition:
Deleting a node from a doubly linked list involves locating the node and adjusting the pointers of its adjacent nodes to bypass it, ensuring the previous node points to the next node and vice versa. Edge cases for the head and tail nodes should be handled separately, and the memory of the deleted node should be freed if required. This process maintains the list's integrity while removing the node.
Approach:
Identify the previous and next nodes of the node to be deleted using its back and next pointers.
Update the next pointer of the previous node to point to the next node, and update the back pointer of the next node to point to the previous node.
Set the next and back pointers of the node to be deleted to null to fully disconnect it from the list.
Delete the node (C++ only). In C++, explicitly delete the node to free memory. In Java, memory management is automatic and handled by the garbage collector.

# Definition of doubly linked list
class ListNode:
    def __init__(self, data1=0, next1=None, prev1=None):
        self.val = data1
        self.next = next1
        self.prev = prev1

# Solution class
class Solution:
# Function to delete the given node from doubly linked list
    def deleteGivenNode(self, node):
        prev = node.prev
        front = node.next

        # Edge case if the given node is the tail node
        if front is None:
            prev.next = None
            node.prev = None
            return

        # Disconnect node
        prev.next = front
        front.prev = prev

        # Set node's pointers to None
        node.next = None
        node.prev = None

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
    # Node to be deleted
    node = head.next.next

    # Print the Original list
    print("Original List: ", end="")
    printLL(head)

    # Create an instance of Solution class
    sol = Solution()

    #Function call to delete the given node from the doubly linked list 
    sol.deleteGivenNode(node)

    # Print the Modified list
    print("Modified list: ", end="")
    printLL(head)
Complexity Analysis:
Time Complexity: O(1) as it only involves updating references and is independent of the list’s length.

Space Complexity: O(1) as no extra space is used.


'''
# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def deleteGivenNode(self, node):
        prev = node.prev
        front = node.next

        if front is None:
            prev.next = None
            node.prev = None
            return

        prev.next = front
        front.prev = prev

        node.next = None
        node.prev = None