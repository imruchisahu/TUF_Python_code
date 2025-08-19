'''
Given the head of a singly linked list, delete the head of the linked list and return the head of the modified list.



The head is the first node of the linked list.





Please note that this section might seem a bit difficult without prior knowledge on what linkedlist is, we will soon try to add basics concepts for your ease! If you know the concepts already please go ahead to give a shot to the problem. Cheers!


Examples:
Input: head -> 1 -> 2 -> 3

Output: head -> 2 -> 3

Explanation: The first node was removed.

Input: head -> 1

Output: head

Explanation: Note that the head of the linked list gets changed.

Input: head -> 7 -> 8

Output:
head -> 8
Constraints:
1 <= number of nodes in the Linked List <= 1000
0 <= ListNode.val <= 100
Intuition:
Deleting the head node of a linked list involves changing the head pointer to point to the next node. This makes the second node the new head of the list, effectively removing the original head node.
Approach:
Set a temporary pointer to the current head of the linked list and update the head to point to the next node, effectively skipping the original head node.
The original head node is now disconnected and can be deleted to free up memory. Note that in languages with automatic garbage collection like Java, Python, and JavaScript, manual deletion is not needed.
Return the new head of the linked list, which is now the original second node.
Edge Cases:
If the input linked list is empty, we return null.
If there is only one node in the list, we return null after deleting that node.
# Node structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to delete the head node of the linked list
    def deleteHead(self, head):
        # If list is empty, nothing to delete
        if head is None:
            return None
        
        # Set temporary pointer
        temp = head
        
        # Update head to the next node 
        head = head.next
        
        # Delete original head    
        del temp
        
        # Return new head          
        return head

# Function to print the linked list
def printList(head):
    current = head
    while current is not None:
        print(current.val, end=" ")
        current = current.next
    print()

# Function to insert a new node at the beginning of the linked list
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

    print("Original list: ", end="")
    printList(head)
    
    # Creating an instance of Solution Class
    sol = Solution()
    
    # Function call to delete the head node
    head = sol.deleteHead(head)

    print("List after deleting head: ", end="")
    printList(head)
    
Complexity Analysis
Time Complexity: O(1) for updating the head of the linked list.

Space Complexity: O(1) as no extra space is used.

'''
# Definiton of singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteHead(self, head):
        if head is None:
            return None
        temp = head
        head = head.next
        del temp
        return head