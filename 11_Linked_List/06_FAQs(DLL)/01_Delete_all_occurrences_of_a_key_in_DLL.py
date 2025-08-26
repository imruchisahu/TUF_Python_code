'''
Given the head of a doubly linked list and an integer target. Delete all nodes in the linked list with the value target and return the head of the modified linked list.


Examples:
Input: head -> 1 <-> 2 <-> 3 <-> 1 <-> 4, target = 1

Output: head -> 2 <-> 3 <-> 4

Explanation: All nodes with the value 1 were removed.

Input: head -> 2 <-> 3 <-> -1 <-> 4 <-> 2, target = 2

Output: head -> 3 <-> -1 <-> 4

Explanation: All nodes with the value 2 were removed.

Note that the value of head is changed.

Input: head -> 7 <-> 7 <-> 7 <-> 7, target = 7

Output:
head
Constraints:
0 <= number of nodes in the linked list <= 105
-104 <= ListNode.val <= 104
-104 <= target <= 104


Intuition
Go through each and every node of the doubly linked list and delete the node which matches the target/key value.
Approach
Start by setting a temporary pointer to the head of the doubly linked list. This pointer will be used to traverse the list.
Loop through the list until the end is reached. For each node, check if its value equals the target value to be deleted.
Delete Target Nodes:
If the node's value matches the target:
If the node is the head of the list, update the head to the next node.
Update the next pointer of the previous node (if it exists) to skip the current node.
Update the prev pointer of the next node (if it exists) to skip the current node.
Delete the current node and move the temporary pointer to the next node.
If the node's value does not match the target, move the temporary pointer to the next node.
After the traversal, return the updated head of the list, which may have been modified if the head node was deleted.

# Definition of doubly linked list
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    # Function to delete all occurrences of a target value
    def deleteAllOccurrences(self, head, target):
        temp = head
        
        while temp is not None:
            if temp.val == target:
                # Update head if needed
                if temp == head:
                    head = temp.next
                
                nextNode = temp.next
                prevNode = temp.prev

                # Update next node's previous
                if nextNode is not None:
                    nextNode.prev = prevNode
                
                # Update previous node's next
                if prevNode is not None:
                    prevNode.next = nextNode

                # Delete the current node
                temp = nextNode
            else:
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
    # Creating doubly linked list
    head = newNode(1)
    head.next = newNode(2)
    head.next.prev = head
    head.next.next = newNode(3)
    head.next.next.prev = head.next
    head.next.next.next = newNode(2)
    head.next.next.next.prev = head.next.next
    head.next.next.next.next = newNode(4)
    head.next.next.next.next.prev = head.next.next.next
    head.next.next.next.next.next = newNode(2)
    head.next.next.next.next.next.prev = head.next.next.next.next
    head.next.next.next.next.next.next = newNode(5)
    head.next.next.next.next.next.next.prev = head.next.next.next.next.next

    # Print original list
    print("Original list: ", end="")
    printList(head)

    # Delete all occurrences of 2
    sol = Solution()
    head = sol.deleteAllOccurrences(head, 2)

    # Print modified list
    print("Modified list: ", end="")
    printList(head)

Complexity Analysis
Time Complexity: O(N) because the linked list is traversed only once. Here, N represents the number of nodes in the linked list.

Space Complexity: O(1) because no extra space used.

'''
# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def deleteAllOccurrences(self, head, target):
        temp = head
        
        while temp is not None:
            if temp.val == target:
                if temp == head:
                    head = temp.next
                
                nextNode = temp.next
                prevNode = temp.prev
                if nextNode is not None:
                    nextNode.prev = prevNode
                if prevNode is not None:
                    prevNode.next = nextNode
                temp = nextNode
            else:
                temp = temp.next
        
        return head