'''
Given the head of a singly linked list and an integer X, insert a node with value X at the tail of the linked list and return the head of the modified list.



The tail is the last node of the linked list.


Examples:
Input: head -> 1 -> 2 -> 3, X = 7

Output: head -> 1 -> 2 -> 3 -> 7

Explanation: 7 was added as the last node.

Input: head, X = 0

Output: head -> 0

Explanation: 0 was added as the last/only node.

Input: head -> 5 -> 6, X = 8

Output:
head -> 5 -> 6 -> 8

Intuition:
Traverse the list to the last node, then set it's next to the new node. If the list is empty, set the head to the new node.
Approach:
Create a new node with the given value and set its next to NULL.
Initialize a temporary pointer to the head to traverse the linked list.
Traverse the list using the temporary pointer until you reach the last node.
Point the next of the last node to the newly created node, making it the new tail of the linked list.
Return the head of the linked list to get the updated linked list.

# Definition of singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to insert a new node at the tail of the linked list
    def insertAtTail(self, head, X):
        if head is None:
            return ListNode(X)

        temp = head
        # Traversing until the last node
        while temp.next is not None:
            temp = temp.next

        newNode = ListNode(X)
        temp.next = newNode

        return head

# Helper Function to print the linked list
def printLL(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()

if __name__ == "__main__":
    # Create a linked list from a list
    arr = [10, 20, 30]
    val = 40
    head = ListNode(arr[0])
    head.next = ListNode(arr[1])
    head.next.next = ListNode(arr[2])

    # Print the original list
    print("Original List: ", end="")
    printLL(head)

    # Create a Solution object
    sol = Solution()
    head = sol.insertAtTail(head, val)

    # Print the modified linked list
    print("List after inserting the given value at the tail: ", end="")
    printLL(head)

Complexity Analysis:
Time Complexity: O(N) for traversing the linked list and inserting the new node after the tail. Here N is the length of the Linked List.

Space Complexity: O(1) as no extra space used.

'''
# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertAtTail(self, head, X):
        if head is None:
            return ListNode(X)
        temp = head
        while temp.next is not None:
            temp=temp.next
        newNode = ListNode( X)
        temp.next = newNode
        return head