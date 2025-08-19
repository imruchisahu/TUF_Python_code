'''
Given the head of a singly linked list and two integers X and K, insert a node with value X as the kth node of the linked list and return the head of the modified list.


Examples:
Input: head -> 1 -> 2 -> 3, X = 5, K = 2

Output: head -> 1 -> 5 -> 2 -> 3

Input: head, X = 7, K = 1

Output: head -> 7

Explanation: Note that the value of the head was changed.

Input: head -> 1 -> 2, X = 15, K = 3

Output:
head -> 1 -> 2 -> 15
Constraints:
n == number of nodes in the Linked List
0 <= n <= 1000
0 <= ListNode.val <= 100
0 <= X <= 100
1 <= K <= n+1

Intuition:
The intuition is to traverse the linked list up to the position just before the desired insertion point. Once there, create a new node with the given value and update the links so that the new node is inserted at the correct position. This involves pointing the new node to the subsequent node and updating the previous node to point to the new node.
Approach:
Initialize a temporary pointer to traverse the list and a counter variable to track the number of nodes traversed.
Move the pointer until you reach the node just before the desired insertion position (k-1).
Create the new node with the given value.
To insert the new node:
Set the new node's next pointer to the current (k)th node (temp->next).
Update the (k-1)th node's next pointer to the new node, completing the insertion.
If the traversal finishes before reaching the (k-1)th node, it means k is larger than the length of the list plus one, so no node will be inserted.

# Definition of singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to insert a new node at the kth position 
    def insertAtKthPosition(self, head, X, K):
        #If the linked list is empty and k is 1, insert the new node as the head 
        if head is None:
            if K == 1:
                return ListNode(X)
            else:
                return head
        
        #If K is 1, insert the new node at the beginning of the linked list 
        if K == 1:
            return ListNode(X, head)
        
        cnt = 0
        temp = head

        #Traverse the linked list to find the node at position k-1 
        while temp is not None:
            cnt += 1
            if cnt == K - 1:
            #Insert the new node after the node at position k-1 
                newNode = ListNode(X, temp.next)
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
    arr = [10, 30, 40]
    X = 20
    K = 2
    head = ListNode(arr[0])
    head.next = ListNode(arr[1])
    head.next.next = ListNode(arr[2])

    # Print the original list
    print("Original List: ", end="")
    printLL(head)

    # Create a Solution object
    sol = Solution()
    head = sol.insertAtKthPosition(head, X, K)

    # Print the modified linked list
    print("List after inserting the given value at the Kth position: ", end="")
    printLL(head)
Complexity Analysis:
Time Complexity: O(N) worst case, when insertion happens at the tail and O(1) best case, when insertion happens at the head.

Space Complexity: O(1) no extra space used.

'''
# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertAtKthPosition(self, head, X, K):
        if head is None:
            if K == 1:
                return ListNode(X)
            else:
                return head
        if K == 1:
            return ListNode(X, head)
        
        cnt = 0
        temp = head
        while temp is not None:
            cnt += 1
            if cnt == K - 1:
                newNode = ListNode(X, temp.next)
                temp.next = newNode
                break
            temp = temp.next
        
        return head