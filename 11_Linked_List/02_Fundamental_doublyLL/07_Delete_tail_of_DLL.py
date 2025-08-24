'''Given the head of a doubly linked list, remove the node at the tail of the linked list and return the head of the modified list.



The tail is the last node of the linked list.


Examples:
Input: head -> 1 <-> 2 <-> 3

Output: head -> 1 <-> 2

Explanation: The node with value 3 was removed.

Input: head -> 7

Output: head

Explanation: Note that the head has null value after the removal.

Input: head -> 2 <-> 4

Output:
head -> 2
Constraints:
n == Number of nodes in the linked list
1 <= n <= 100
0 <= ListNode.val <= 100

Intuition:
Update the linkage between its last node and its second last node. As a doubly linked list is bidirectional, set the second last node's next pointer and the last node's back pointer to null. Then,return the head as the result.
Approach:
Start at the head of the list.
Iterate through the list until the last node (tail) is reached.
Find the second-to-last node (prev) using the tail's back pointer.
Set the next pointer of the prev node to null.
Set the back pointer of the tail node to null.
Return the head of the list.
Note: In C++, explicitly delete the last node to free memory. In Java, garbage collection handles this.
# Definition of doubly linked list
class ListNode:
    def __init__(self, data1=0, next1=None, prev1=None):
        self.val = data1
        self.next = next1
        self.prev = prev1

# Solution class
class Solution:
    # Function to delete the tail of a doubly linked list
    def deleteTail(self, head):
        if head is None or head.next is None:
            return None  # Return None if list is empty or has only one node
        
        # Navigate to the tail of the linked list
        tail = head
        while tail.next is not None:
            tail = tail.next
        
        # Update the pointers
        newTail = tail.prev
        newTail.next = None
        tail.prev = None

        # Return head of modified list
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

    # Function call to delete the tail of the doubly linked list
    head = sol.deleteTail(head)

    # Print the Modified list
    print("Modified list: ", end="")
    printLL(head)

Complexity Analysis:
Time Complexity: O(N), where N is the number of nodes in the DLL.
This is because we traverse the entire DLL to reach the end to delete the tail.

Space Complexity: O(1) as no extra space used.
'''
# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def deleteTail(self, head):
        if head is None or head.next is None:
            return None
        tail=head
        while tail.next is not None:
            tail = tail.next

        newTail= tail.prev
        newTail.next = None
        tail.prev = None

        return head