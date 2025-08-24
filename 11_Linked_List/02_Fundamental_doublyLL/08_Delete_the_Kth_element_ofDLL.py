'''Given the head of a doubly linked list and an integer k, remove the node at the kth position of the linked list and return the head of the modified list.


Examples:
Input: head -> 2 <-> 5 <-> 7 <-> 9, k = 2

Output: head -> 2 <-> 7 <-> 9

Explanation: The node with value 5 was removed.

Input: head -> 2 <-> 5 <-> 7, k = 1

Output: head -> 5 <-> 7

Explanation: The node with value 2 was removed, note that the head was modified.

Input: head -> 2 <-> 5 <-> 7, k = 3

Output:
head -> 2 <-> 5
Constraints:
n == Number of nodes in the linked list
1 <= n <= 100
0 <= ListNode.val <= 100
1 <= k <= n

Intuition:
Locate the node just before the kth node by traversing the list. Then, change the pointer of this node to bypass the k-th node and connect directly to the node after it.
Approach:
Traverse the doubly linked list to find the K-th node, maintaining a counter. Use a while loop to increment the counter and move to the next node until the counter equals K. Use a temporary pointer to point to the K-th node to be deleted.
Set the previous node to the node to which the temporary pointer’s back pointer is pointing. Track the temporary pointer’s next node using the front pointer.
Update the 'next' pointer of the previous node to point to the front node.
Update the 'back' pointer of the front node to point to the back node.
Set the temporary pointer’s next and back pointers to null so it does not point to anything. This updates the doubly linked list to be one node shorter.
(C++ Only) Explicitly delete the previous head to free memory. In Java, the garbage collector automatically handles memory management for unreferenced objects.
Edge Cases:
If the input doubly linked list is empty, return null as there is nothing to delete.
If K equals 1 (deleting the first node), follow the steps to delete the head of the list.
If K equals the length of the doubly linked list, delete the tail of the list.
If the list has a single element, K can only be 1, so delete this node and return null.

# Definition of doubly linked list
class ListNode:
    def __init__(self, data1=0, next1=None, prev1=None):
        self.val = data1
        self.next = next1
        self.prev = prev1

# Solution class
class Solution:
    # Function to remove the Kth element
    def deleteKthElement(self, head, k):
        # If the list is empty, return None
        if head is None:
            return None
        
        count = 0
        kNode = head

        # Traverse the list
        while kNode is not None:
            count += 1
            if count == k:
                break
            kNode = kNode.next

        # If k is larger than the list size
        if kNode is None:
            return head

        # Update the pointers
        prev = kNode.prev
        front = kNode.next

        # If node to be deleted is the only node in the list
        if prev is None and front is None:
            return None
        
        # If node to be deleted is head of the list
        elif prev is None:
            head = front
            front.prev = None
        
        # If node to be deleted is tail of the list
        elif front is None:
            prev.next = None
        
        # If node to be deleted is in the middle of the list
        else:
            prev.next = front
            front.prev = prev

        # Return modified list head
        return head

# Helper Function to convert an array to a doubly linked list
def arrayToLinkedList(nums):
    # If array is empty, return None
    if not nums:
        return None

    # Create head node with first element of the array
    head = ListNode(nums[0])
    # Initialize 'prev' to the head node
    prev = head

    for i in range(1, len(nums)):
        # Create a new node
        temp = ListNode(nums[i], None, prev)
        # Update 'next' pointer
        prev.next = temp
        # Move 'prev' to newly created node
        prev = temp

    # Return head
    return head

# Helper Function to print the linked list
def printLL(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    k = 2

    # Creating the doubly linked list from given array
    head = arrayToLinkedList(nums)

    # Print the Original list
    print("Original List: ", end="")
    printLL(head)

    # Create an instance of Solution class
    sol = Solution()

    # Function call to delete the kth Node of the doubly linked list
    head = sol.deleteKthElement(head, k)

    # Print the Modified list
    print("Modified list: ", end="")
    printLL(head)
Complexity Analysis:
Time Complexity: O(k) because it only involves identifying the Kth node and updating its references to delete it.

Space Complexity: O(1) as no extra space is used.



'''
# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def deleteKthElement(self, head, k):
        # If the list is empty, return None
        if head is None:
            return None
        
        count = 0
        kNode = head

        # Traverse the list
        while kNode is not None:
            count += 1
            if count == k:
                break
            kNode = kNode.next

        # If k is larger than the list size
        if kNode is None:
            return head

        # Update the pointers
        prev = kNode.prev
        front = kNode.next

        # If node to be deleted is the only node in the list
        if prev is None and front is None:
            return None
        
        # If node to be deleted is head of the list
        elif prev is None:
            head = front
            front.prev = None
        
        # If node to be deleted is tail of the list
        elif front is None:
            prev.next = None
        
        # If node to be deleted is in the middle of the list
        else:
            prev.next = front
            front.prev = prev

        # Return modified list head
        return head
