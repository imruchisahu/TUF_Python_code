'''
Given the head of a singly linked list and an integer k, delete the kth node of the linked list and return the head of the modified list.


Examples:
Input: head -> 3 -> 4 -> 5, k = 2

Output: head -> 3 -> 5

Explanation: The 2nd node with value 4 was removed.

Input: head -> 1 -> 2 -> 3, k = 1

Output: head -> 2 -> 3

Explanation: The 1st Node was removed, note that the value of the head has changed.

Input: head -> 7 -> 7 -> 7, k = 3

Output:
head -> 7 -> 7
Constraints:
n == number of nodes in the Linked list
1 <= n <= 1000
0 <= ListNode.val <= 100
1 <= k <= n

Intuition:
The most straightforward way to approach this problem is to delete the k-th node and point the previous node (the (k-1)th node) to the next node (the (k+1)th node) to maintain the linked list.
Approach:
Initialize one pointer to the head of the list and another to NULL.
Traverse the list with one pointer, counting nodes until the count matches the desired position.
If the count equals the position and the pointer is not NULL:
Update the previous node’s next reference to skip the node to be deleted.
Deallocate the node if manual deletion is required.
If the count does not match the position (i.e., the position is greater than the list length), no node is deleted.
In languages with automatic garbage collection (e.g., Java, Python, JavaScript), explicit deletion is not needed.
Edge Cases:
If the input linked list is empty, return null, as there is nothing to delete.
If the position equals 1 (meaning we need to delete the first node), follow the same steps as deleting the head of the list.
If the position equals the length of the linked list, delete the tail of the linked list.
If the linked list has a single element, the position can only be 1; hence delete this node and return null.


# Node structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to delete the k-th node of a linked list
    def deleteKthNode(self, head, k):
        # If the list is empty, return None
        if head is None:
            return None
        
        # If k is 1, delete the head node
        if k == 1:
            head = head.next
            return head
        
        # Initialize a temporary pointer
        temp = head
        
        # Traverse to the (k-1)th node
        for i in range(k - 2):
            if temp is None:
                break
            temp = temp.next
        
        #If k is greater than the number of nodes, return the unchanged list 
        if temp is None or temp.next is None:
            return head
        
        # Delete the k-th node
        temp.next = temp.next.next
        
        # Return head
        return head

# Function to print the linked list
def printLL(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

if __name__ == "__main__":
    # Initialize a list with values for the linked list
    arr = [12, 5, 8, 7]
    
    # Create a linked list with the values from the list
    head = ListNode(arr[0])
    head.next = ListNode(arr[1])
    head.next.next = ListNode(arr[2])
    head.next.next.next = ListNode(arr[3])
    
    # Print the original linked list
    print("Original list: ", end="")
    printLL(head)
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Call the deleteKthNode function to delete the k-th node
    k = 2
    head = sol.deleteKthNode(head, k)
    
    # Print the linked list after deletion
    print("List after deleting the kth node: ", end="")
    printLL(head)
Complexity Analysis:
Time Complexity: O(N) worst case, when deleting the tail and O(1) best case, when deleting the head.

Space Complexity: O(1) no extra space used.



'''