'''
Given the head of a singly linked list and an integer X, insert a node with value X at the head of the linked list and return the head of the modified list.



The head is the first node of the linked list.


Examples:
Input: head -> 1 -> 2 -> 3, X = 7

Output: head -> 7 -> 1 -> 2 -> 3

Explanation: 7 was added as the 1st node.

Input: head, X = 7

Output: head -> 7

Explanation: 7 was added as the 1st node.

Input: head -> 1 -> 3, X = 4

Output:
head -> 4 -> 1 -> 3
Constraints:
0 <= number of nodes in the Linked List <= 1000
0 <= ListNode.val <= 100
0 <= X <= 100
Intuition:
Insert at the head of a linked list by creating a new node, linking it to the current head, and updating the head pointer.
Approach:
Create a new node with the value to be inserted at the beginning of the linked list.
Set the new node's pointer to the current head of the linked list.
Update the head of the linked list to the newly created node.


# Definition of singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to insert at head
    def insertAtHead(self, head, X):
        # Creating a new node
        newnode = ListNode(X)
        
       #Making next of newly created node to point to the head of the LinkedList
        newnode.next = head
        
        # Making newly created node as head
        head = newnode
        
        # Return the head of modified list
        return head

# Helper Function to print the linked list
def printLL(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()

if __name__ == "__main__":
    # Create a linked list from a list
    arr = [20, 30, 40]
    X= 10
    head = ListNode(arr[0])
    head.next = ListNode(arr[1])
    head.next.next = ListNode(arr[2])

    # Print the original list
    print("Original List: ", end="")
    printLL(head)

    # Create a Solution object
    sol = Solution()
    head = sol.insertAtHead(head, X)

    # Print the modified linked list
    print("List after inserting the given value at head: ", end="")
    printLL(head)
        return head

# Helper Function to print the linked list
def printLL(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()

if __name__ == "__main__":

Complexity Analysis:
Time Complexity: O(1) for inserting the new node at the head of the linked list

Space Complexity: O(1) no extra space used.

'''
# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertAtHead(self, head, X):
        newnode = ListNode(X)
        newnode.next = head
        head = newnode
        return head