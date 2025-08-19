'''
Given the head of a singly linked list and two integers X and val, insert a node with value val before the node with value X in the linked list and return the head of the modified list.


Examples:
Input: head -> 1 -> 2 -> 3, X = 2, val = 5

Output: head -> 1 -> 5 -> 2 -> 3

Explanation: The node with value 5 was added before the node with value 2

Input: head -> 1 -> 2 -> 3, X = 7, val = 5

Output: head -> 1 -> 2 -> 3

Explanation: No node was added as X was not found in the list.

Input: head -> 1, X = 1, val = 10

Output:
head -> 10 -> 1
Constraints:
n == number of nodes in the Linked List
1 <= n <= 1000
0 <= ListNode.val <= 100
0 <= X <= 100
0 <= val <= 100
Number of nodes with value X is 0 or 1

Intuition:
Find the node with the given value in the linked list and then insert the newly created node with data before the given node.
Approach:
Initialize a temporary pointer to traverse the list.
Traverse the list until you find a node whose next node has the target value, since the new node needs to be inserted before this node.
Once you find the correct position, create a new node with the given value.
To insert the new node:
Point the new node to the next node in the list.
Update the current node to point to the new node, completing the insertion.
If the traversal completes without finding the target value, it means the target value is not in the list, i.e., no insertion will occur.

# Definition of singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to insert a new node before the given node
    def insertBeforeX(self, head, X, val):
        if head is None:
            return None
        
        # Insert at the beginning if 
        # the value matches the head's data
        if head.val == X:
            return ListNode(val, head)
        
        temp = head
        while temp.next is not None:
            # Insert at the current position if 
            # the next node has the desired value
            if temp.next.val == X:
                newNode = ListNode(val, temp.next)
                temp.next = newNode
                break
            temp = temp.next
        
        return head

# Helper Function to print the linked list
def printLL(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()

if __name__ == "__main__":
    # Create a linked list from a list
    arr = [1, 2, 4, 5]
    X = 4
    val = 3
    head = ListNode(arr[0])
    head.next = ListNode(arr[1])
    head.next.next = ListNode(arr[2])

    # Print the original list
    print("Original List: ", end="")
    printLL(head)

    # Create a Solution object
    sol = Solution()
    head = sol.insertBeforeX(head, X, val)

    # Print the modified linked list
    print("List after inserting a new node before the given node: ", end="")
    printLL(head)
Complexity Analysis:
Time Complexity: O(N) worst case, when insertion happens at the tail and O(1) best case, when insertion happens at the head.

Space Complexity: O(1) as we have not used any extra space.

'''
# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertBeforeX(self, head, X, val):
        if head is None:
            return None
        
        if head.val == X:
            return ListNode(val, head)
        
        temp = head
        while temp.next is not None:
            if temp.next.val == X:
                newNode = ListNode(val, temp.next)
                temp.next = newNode
                break
            temp = temp.next
        
        return head