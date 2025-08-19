'''Given the head of a singly linked list and an integer X, delete the node with value X and return the head of the modified list.


Examples:
Input: head -> 3 -> 4 -> 5, X = 5

Output: head -> 3 -> 4

Explanation: The node with value 5 was removed.

Input: head -> 3 -> 4 -> 5, X = 7

Output: head -> 3 -> 4 -> 5

Explanation: No nodes were removed.

Input: head -> 3 -> 4 -> 5, X = 3

Output:
head -> 4 -> 5
Constraints:
n == number of nodes in the Linked list
1 <= n <= 1000
0 <= ListNode.val <= 100
0 <= X <= 100
Number of nodes with value X is either 0 or 1
Intuition
Traverse the linked list and check if the data in the current node matches the given value. If a match is found, remove this node by updating the previous node's next reference to point to the node following the current one. If the traversal completes without finding a match, the linked list remains unchanged.
Approach
Initialize a pointer to the head of the list and another to null. The first pointer will traverse the list, while the second keeps track of the node before the current node.
Traverse the linked list until the data in the current node matches the target value. Consider two scenarios:
If a match is found:
Update the previous node’s reference to point to the node following the current one.
Release the memory occupied by the current node, effectively removing it from the list.
If the traversal completes without finding a match:
No changes are made to the linked list.
Note: In languages with automatic garbage collection (e.g., Java, Python, JavaScript), explicit node deletion is unnecessary as the garbage collector will automatically reclaim memory that is no longer in use.

# Definition of singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # To delete a node with a specific value in a linked list
    def deleteNodeWithValueX(self, head, X):
        # Check if list is empty
        if head is None:
            return head
        
        # If first node has target value, delete
        if head.val == X:
            head = head.next
            return head
        
        temp = head
        prev = None
        
    #Traverse the list to find the node with the target value 
        while temp is not None:
            if temp.val == X:
                # Adjust the pointers
                prev.next = temp.next
                return head
            prev = temp
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
    arr = [0, 1, 2]
    X = 1
    head = ListNode(arr[0])
    head.next = ListNode(arr[1])
    head.next.next = ListNode(arr[2])

    # Print the original list
    print("Original List: ", end="")
    printLL(head)

    # Create a Solution object
    sol = Solution()
    head = sol.deleteNodeWithValueX(head, X)

    # Print the modified linked list
    print("List after deleting the given value: ", end="")
    printLL(head)

Complexity Analysis:
Time Complexity: O(N) worst case, when the value is found at the tail, and O(1) best case, when the value is found at the head. Here N is the length of the linked list.

Space Complexity: O(1) as no extra space used.

'''
# Definiton of singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodeWithValueX(self, head, X):
        if head is None:
            return head
        if head.val == X:
            head = head.next
            return head
        
        temp = head
        prev = None
        while temp is not None:
            if temp.val == X:
                prev.next = temp.next
                return head
            prev = temp
            temp = temp.next
        
        return head