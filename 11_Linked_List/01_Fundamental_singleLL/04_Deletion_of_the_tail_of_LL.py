'''Given the head of a singly linked list, delete the tail of the linked list and return the head of the modified list.



The tail is the last node of the linked list.


Examples:
Input: head -> 1 -> 2 -> 3

Output: head -> 1 -> 2

Explanation: The last node was removed.

Input: head -> 1

Output: head

Explanation: Note that the value of head is null here.

Input: head -> 7 -> 8

Output:
head -> 7
Constraints:
1 <= number of nodes in the Linked List <= 1000
0 <= ListNode.val <= 100
Intuition:
Update the linked list by pointing the second-to-last node to null. Iterate through the list until reaching this node, then set its next pointer to null. This will remove the last node from the list. In C++, remember to free the memory occupied by the last node to avoid memory leaks.
Approach:
Initialize a pointer to the head of the list and iterate to the second-to-last node, which will become the new tail.
Free the memory occupied by the last node. In languages with automatic garbage collection (e.g., Java, Python, JavaScript), this step is handled automatically.
Set the next pointer of the new tail (second-to-last node) to null to update the linked list.
Edge cases:
If the input linked list is empty, return null.
If there is only one node in the list, delete that node and return null.
Dry Run:
Image 1
Image 2
Image 3
Image 4

1/4


Solution:
Cpp
Java
Python
Javascript
C#
Go


# Node structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to delete the tail node of linked list
    def deleteTail(self, head):
        
        # If the list is empty or has only one node
        if head is None or head.next is None:
            return None  # Return None
        
        # Temporary pointer
        temp = head
        
        #Traverse to the second last node in the list
        while temp.next.next is not None:
            temp = temp.next
        
        # Delete the last node
        temp.next = None
        
        # Return head of modified list
        return head

# Helper Function to print the linked list
def printList(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Helper Function to insert a new node at 
# the beginning of the linked list
def insertAtHead(head, data):
    newNode = ListNode(data)
    newNode.next = head
    head = newNode
    return head

if __name__ == "__main__":
    # Create a linked list
    head = None
    head = insertAtHead(head, 3)
    head = insertAtHead(head, 2)
    head = insertAtHead(head, 1)

    print("Original list: ")
    printList(head)

    # Creating an instance of Solution class
    sol = Solution()

    # Function call to delete the tail node
    head = sol.deleteTail(head)

    print("List after deleting tail: ")
    printList(head)
Complexity Analysis:
Time Complexity: O(N) for traversing the linked list and updating the tail.

Space Complexity: O(1) as no extra space has been used.

'''