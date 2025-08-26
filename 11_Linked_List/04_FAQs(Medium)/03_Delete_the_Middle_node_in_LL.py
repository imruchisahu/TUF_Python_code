'''Given the head of a non-empty singly linked list containing integers, 
delete the middle node of the linked list. Return the head of the modified linked list.



The middle node of a linked list of size n is the (⌊n / 2⌋ + 1)th node from the start using 1-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.


Examples:
Input: head -> 1 -> 2 -> 3 -> 4 -> 5

Output: head -> 1 -> 2 -> 4 -> 5

Explanation: n = 5.

⌊n / 2⌋ + 1 = 3, therefore middle node has index 3 and so the node with value 3 was deleted.

Input: head -> 7 -> 6 -> 5 -> 4

Output: head -> 7 -> 6 -> 4

Expl﻿anation: n = 4.

⌊n / 2⌋ + 1 = 3, therefore middle node has index 3 and so the node with value 5 was deleted.

Input: head -> 7

Output:
head
Constraints:
1 <= number of nodes in the Linked List <= 105
0 <= ListNode.val <= 104

#Brute
Intuition
First, count all the nodes by going through the list. Then, start again from the beginning and go to the node just before the middle one. Change the links to skip over the middle node, taking it out of the list.
Approach
First, count all the nodes in the linked list to find out how many there are. Then, figure out which node is in the middle by dividing the total number of nodes by 2.

Next, start from the beginning of the list and move through the nodes until you reach the middle one.

When you reach the middle node, remove it by linking the previous node directly to the node after the middle one. Finally, clear the space that was taken up by the middle node.

# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to delete middle node of linked list
    def deleteMiddle(self, head):
        """ Edge case: if the list is empty 
        or has only one node, return null """
        if not head or not head.next:
            return None

        # Temporary node to traverse
        temp = head
        
        # Variable to store number of nodes
        n = 0
        
        """ Loop to count the number of nodes 
        in the linked list """
        while temp:
            n += 1
            temp = temp.next
        
        # Index of the middle node
        middleIndex = n // 2
        
        # Reset temporary node 
        # to beginning of linked list
        temp = head
        
        """ Loop to find the node 
        just before the middle node """
        for _ in range(1, middleIndex):
            temp = temp.next
        
        # If the middle node is found
        if temp.next:
            # Create pointer to the middle node
            middle = temp.next
            
            # Adjust pointers to skip middle node
            temp.next = temp.next.next
            
            """ Free the memory allocated 
            to the middle node """
            del middle
        
        # Return the head of the modified linked list
        return head

# Function to print the linked list
def printLL(head):
    temp = head
    while temp:
        print(temp.val, end=" ")
        temp = temp.next
    print()

# Creating a sample linked list: 
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Display the original linked list
print("Original Linked List: ", end="")
printLL(head)

# Deleting the middle node
solution = Solution()
head = solution.deleteMiddle(head)

# Displaying the updated linked list
print("Updated Linked List: ", end="")
printLL(head)

Time Complexity
Time Complexity: O(N + N/2) because the loop traverses the entire linked list once to count the total number of nodes then the loop iterates halfway through the linked list to reach the middle node. Hence, the time complexity is O(N + N/2) ~ O(N).

Space Complexity: O(1) because the code uses a constant amount of extra space regardless of the size of the linked list. It doesn't use any additional data structures in proportion to the input size.

#Optimal
Intuition
The brute force method involves traversing the linked list twice to find and delete the middle node. To make this more efficient,we use the Tortoise and Hare approach which helps in finding the middle node in one traversal by moving the 'slow' pointer one step and the 'fast' pointer two steps at a time.

This ensures the 'slow' pointer reaches the middle when the 'fast' pointer reaches the end. To have 'slow' reach just before the middle, the 'fast' pointer gets a head start.

Approach
Initialization: Check if the list is empty or has only one node. If so, there is no middle node to delete, so return NULL. Set 'slow' and 'fast' pointers at the head of the list, and move 'fast' two nodes ahead initially.

Traverse the List: Move the 'slow' pointer one step at a time and the 'fast' pointer two steps at a time. Continue this process until the 'fast' pointer reaches the end of the list.

Middle Node Detection: When the 'fast' pointer reaches the end of the list, the 'slow' pointer will be at the node just before the middle node.

Delete Middle Node: Remove the middle node by adjusting the 'next' pointer of the 'slow' node to skip over the middle node.

Return Modified List: Return the head of the modified linked list.

# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to delete the middle node of a linked list
    def deleteMiddle(self, head):
        """ If the list is empty or has only one node,
        return None as there is no middle node to delete """
        if not head or not head.next:
            return None

        # Initialize slow and fast pointers
        slow = head
        fast = head.next.next

        # Move 'fast' pointer twice as fast as 'slow'
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node by skipping it
        slow.next = slow.next.next
        return head

# Function to print the linked list
def printLL(head):
    temp = head
    while temp:
        print(temp.val, end=" ")
        temp = temp.next
    print()

# Creating a sample linked list: 
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Display the original linked list
print("Original Linked List: ", end="")
printLL(head)

# Deleting the middle node
solution = Solution()
head = solution.deleteMiddle(head)

# Displaying the updated linked list
print("Updated Linked List: ", end="")
printLL(head)

Time Complexity
Time Complexity: O(N/2) because the code traverses the linked list using the Tortoise and Hare approach. The code increments both 'slow' and 'fast' pointers at different rates, effectively covering about half the list before reaching the midpoint, hence the time complexity of the algorithm is O(N/2) ~ O(N).

Space Complexity: O(1) because the code uses a constant amount of extra space regardless of the size of the input (linked list). It doesn't use any additional data structures in proportion to the input size.

'''
# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head