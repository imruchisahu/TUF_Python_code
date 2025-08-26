'''
Given the head of a doubly linked list with its values sorted in non-decreasing order. Remove all duplicate occurrences of any value in the list so that only distinct values are present in the list.



Return the head of the modified linked list.


Examples:
Input: head -> 1 <-> 1 <-> 3 <-> 3 <-> 4 <-> 5

Output: head -> 1 <-> 3 <-> 4 <-> 5

Explanation: head -> 1 <-> 1 <-> 3 <-> 3 <-> 4 <-> 5

The underlined nodes were deleted to get the desired result.

Input: head -> 1 <-> 1 <-> 1 <-> 1 <-> 1 <-> 2

Output: head -> 1 <-> 2

Explanation: head -> 1 <-> 1 <-> 1 <-> 1 <-> 1 <-> 2

The underlined nodes were deleted to get the desired result.

Input: head -> 1 <-> 2 <-> 3

Output:
head -> 1 <-> 2 <-> 3
Constraints:
1 <= number of nodes in the linked list <= 105
-104 <= ListNode.val <= 104
Values of nodes are sorted in non-decreasing order.

Intuition
Since the list is sorted, any duplicates will always occur contiguously. This allows us to traverse the list once and remove consecutive nodes with the same value. By updating the pointers of the previous and next nodes appropriately, we can ensure the list remains properly linked while removing duplicates.
Approach
Start by setting a temporary pointer to the head of the doubly linked list. This pointer will be used to traverse the list.
Loop through the list until the end is reached. For each node, check if its next node has the same value.
Remove Duplicate Nodes:
If the next node has the same value as the current node:
Continue moving to the next node until a node with a different value is found.
Delete all duplicate nodes encountered.
Link the current node to the next non-duplicate node.
Update the previous pointer of the next non-duplicate node (if it exists).
Move the temporary pointer to the next node and repeat the process.
After the traversal, return the updated head of the list.
# Definition of doubly linked list
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    # To remove duplicates from a sorted doubly linked list
    def removeDuplicates(self, head):
        temp = head
        
        # Traverse the list
        while temp is not None and temp.next is not None:
            nextNode = temp.next
            
            # Remove all duplicate nodes
            while nextNode is not None and nextNode.val == temp.val:
                # Store the duplicate node
                duplicate = nextNode
                # Move to the next node
                nextNode = nextNode.next
                # Delete the duplicate node
                del duplicate
            
            # Link the current node to the next non-duplicate node
            temp.next = nextNode
            # Update previous pointer of next non-duplicate node
            if nextNode is not None:
                nextNode.prev = temp
            
            # Move to the next node
            temp = temp.next
        
        return head

# Function to print doubly linked list
def printList(head):
    temp = head
    while temp is not None:
        print(temp.val, end=" ")
        temp = temp.next
    print()

# Helper function to create a new node
def newNode(data):
    return ListNode(data)

if __name__ == "__main__":
    # Creating a sorted doubly linked list:
    head = newNode(1)
    head.next = newNode(2)
    head.next.prev = head
    head.next.next = newNode(2)
    head.next.next.prev = head.next
    head.next.next.next = newNode(3)
    head.next.next.next.prev = head.next.next
    head.next.next.next.next = newNode(4)
    head.next.next.next.next.prev = head.next.next.next
    head.next.next.next.next.next = newNode(4)
    head.next.next.next.next.next.prev = head.next.next.next.next
    head.next.next.next.next.next.next = newNode(5)
    head.next.next.next.next.next.next.prev = head.next.next.next.next.next

    # Print original list
    print("Original list: ", end="")
    printList(head)

    # Remove duplicates
    sol = Solution()
    head = sol.removeDuplicates(head)

    # Print modified list
    print("Modified list: ", end="")
    printList(head)

    
Complexity Analysis
Time Complexity: O(n) and not O(n^2) because each node in the doubly linked list is visited exactly once. The outer loop traverses each distinct node, and the inner loop skips over consecutive duplicates in a single pass, ensuring a total linear traversal of the list. Thus the combined process does not create nested iterations and remains efficient.

Space Complexity: O(1) no extra space is used.

'''

# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def removeDuplicates(self, head):
        temp = head
        while temp is not None and temp.next is not None:
            nextNode = temp.next
            while nextNode is not None and nextNode.val == temp.val:
                duplicate = nextNode
                nextNode = nextNode.next
                del duplicate
            temp.next = nextNode
            if nextNode is not None:
                nextNode.prev = temp
            temp = temp.next
        
        return head