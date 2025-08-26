'''
Given the head of a singly linked list representing a positive integer number. Each node of the linked list represents a digit of the number, with the 1st node containing the leftmost digit of the number and so on. Check whether the linked list values form a palindrome or not. Return true if it forms a palindrome, otherwise, return false.



A palindrome is a sequence that reads the same forward and backwards.


Examples:
Input: head -> 3 -> 7 -> 5 -> 7 -> 3

Output: true

Explanation: 37573 is a palindrome.

Input: head -> 1 -> 1 -> 2 -> 1

Output: false

Explanation: 1121 is not a palindrome.

Input: head -> 9 -> 9 -> 9 -> 9

Output:
true
Constraints:
1 <= number of nodes in the Linked List <= 105
0 <= ListNode.val <= 9
The number represented does not contain any leading zeroes.

#Brute
Intuition
A simple way to determine if a given linked list is a palindrome is to use an additional data structure to temporarily store the node values. We can utilize a stack for this purpose. As we traverse the linked list, we push each node's value onto the stack, which stores the values in reverse order. After traversing the entire list, we traverse it again and compare each node's value with the values popped from the top of the stack. If all values match, the linked list is a palindrome.

Approach
Initialize: Begin by creating an empty stack. This stack will help us temporarily store the nodes' values as we traverse the linked list.
Traverse and Store: Traverse the linked list using a temporary pointer `temp`. As we move through each node, push its value onto the stack. This action stacks the values in reverse order—starting from the head to the tail of the linked list.
Comparison: Reset the `temp` pointer back to the head of the linked list after storing all values. While the stack is not empty:
Pop the top value from the stack.
Compare this value with the value at the current `temp` node.
If they match, move `temp` to the next node and continue the comparison.
If any value does not match during this traversal, conclude that the linked list is not a palindrome and return false.
Palindrome Check: If all values match until the `temp` pointer reaches the end of the linked list, conclude that the linked list is a palindrome and return true.
This approach uses a stack to reverse the order of values temporarily, allowing efficient comparison to check if the linked list maintains symmetry both forwards and backwards.


# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        # Create an empty stack
        stack = []
        
        # Initialize temporary pointer
        temp = head
        
        # Traverse the linked list
        while temp is not None:
            # Push the data from 
            # the current node onto the stack
            stack.append(temp.val)
            
            # Move to the next node
            temp = temp.next
        
        # Reset temporary pointer 
        # back to the head of the 
        # linked list
        temp = head
        
        # Compare values by popping from the 
        # stack and checking against linked list nodes
        while temp is not None:
            if temp.val != stack.pop():
                # If values don't match, 
                # it's not a palindrome
                return False
            
            # Move to the next node 
            # in the linked list
            temp = temp.next
        
        # If all values match,
        # it's a palindrome
        return True

# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.val, end=" ")
        temp = temp.next
    print()

if __name__ == "__main__":
    # Create a linked list with values 1, 5, 2, 5, and 1 (15251, a palindrome)
    head = ListNode(1)
    head.next = ListNode(5)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(1)
    
    # Print the original linked list
    print("Original Linked List: ", end="")
    print_linked_list(head)
    
    # Check if the linked list is a palindrome
    solution = Solution()
    if solution.isPalindrome(head):
        print("The linked list is a palindrome.")
    else:
        print("The linked list is not a palindrome.")

Complexity Analysis
Time Complexity: O(2xN) because we need to traverse the linked list twice: once to push the values onto the stack and once more to pop the values and compare them with the nodes in the linked list. Here, N represents the number of nodes in the linked list. Even though it's O(2xN), it effectively simplifies to O(N).

Space Complexity: O(N) We use a stack to store the values of the linked list. In the worst-case scenario, the stack will hold all N values from the linked list, essentially storing the entire list.

#Optimal
Intuition
The previous approach uses O(N) additional space, which can be avoided by reversing only half of the linked list and comparing the first and second halves. If they match, reverse the portion that was originally reversed, and then return true; otherwise, return false. To implement this, we need to reverse the second half and compare it with the first half in phases. The first step is to divide the linked list into two halves by finding the middle node using the Tortoise and Hare Algorithm.



Approach
Find the middle of the linked list using the Tortoise and Hare Algorithm, then reverse the second half of the list and compare it with the first half. If all values match, the list is a palindrome; otherwise, it is not. This approach ensures that the list is correctly checked without using additional space beyond the stack space used during recursion.

Detailed Steps to Check Palindrome in a Linked List
Check Base Case: If the linked list is empty or has only one node, it is a palindrome by definition. Return true.

Find the Middle: Initialize two pointers, ‘slow’ and ‘fast’. Use the Tortoise and Hare Algorithm where ‘slow’ moves one step at a time and ‘fast’ moves two steps at a time. Continue until ‘fast’ reaches the end or the second last node. The ‘slow’ pointer will be at the middle.

Reverse Second Half: Reverse the second half of the linked list starting from the node after the middle (‘slow->next’). Use a function to reverse the linked list and return the head of the reversed list.

Initialize Pointers for Comparison: Create two pointers, ‘first’ pointing to the head of the linked list and ‘second’ pointing to the head of the reversed second half.

Compare Halves: Compare the data values of nodes from both halves. If any values do not match, return false. Move both ‘first’ and ‘second’ pointers through their respective halves, comparing values until one of them reaches the end.

Restore Original List: After comparison, reverse the second half back to its original state and reattach it to the first half. If all values matched, return true. If not, return false.


# Definition of singly linked list:
class ListNode:
    def __init__(self, data1=0, next1=None):
        self.val = data1
        self.next = next1

class Solution:
    
    # Function to reverse a linked list
    # using the recursive approach
    def reverseLinkedList(self, head):
        # Check if the list is empty
        # or has only one node
        if head is None or head.next is None:
            # No change is needed;
            # return the current head
            return head
        
        # Reverse the remaining 
        # part of the list and get the new head
        newHead = self.reverseLinkedList(head.next)
        
        # Store the next node in 'front'
        # to reverse the link
        front = head.next
        
        # Update the 'next' pointer of 'front' to
        # point to the current head, effectively
        # reversing the link direction
        front.next = head
        
        # Set the 'next' pointer of the
        # current head to 'null' to
        # break the original link
        head.next = None
        
        # Return the new head obtained
        # from the recursion
        return newHead
    
    def isPalindrome(self, head):
        # Check if the linked list is empty
        # or has only one node
        if head is None or head.next is None:
            # It's a palindrome by definition
            return True
        
        # Initialize two pointers, slow and fast,
        # to find the middle of the linked list
        slow = head
        fast = head
        
        # Traverse the linked list to find the
        # middle using slow and fast pointers
        while fast.next is not None and fast.next.next is not None:
            # Move slow pointer one step
            slow = slow.next
            
            # Move fast pointer two steps
            fast = fast.next.next
        
        # Reverse the second half of the
        # linked list starting from the middle
        newHead = self.reverseLinkedList(slow.next)
        
        # Pointer to the first half
        first = head
        
        # Pointer to the reversed second half
        second = newHead
        while second is not None:
            # Compare data values of 
            # nodes from both halves.
            # If values do not match,
            # the list is not a palindrome
            if first.val != second.val:
                # Reverse the second half 
                # back to its original state
                self.reverseLinkedList(newHead)
                
                # Not a palindrome
                return False
            
            # Move the first pointer
            first = first.next
            
            # Move the second pointer
            second = second.next
        
        # Reverse the second half
        # back to its original state
        self.reverseLinkedList(newHead)
        
        # Linked List is a palindrome
        return True

# Function to print the linked list
def printLinkedList(head):
    temp = head
    while temp is not None:
        print(temp.val, end=" ")
        temp = temp.next
    print()

if __name__ == "__main__":
    # Create a linked list with values 1, 5, 2, 5, and 1 (15251, a palindrome)
    head = ListNode(1)
    head.next = ListNode(5)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(1)
    
    # Print the original linked list
    print("Original Linked List: ", end="")
    printLinkedList(head)
    
    # Check if the linked list is a palindrome
    solution = Solution()
    if solution.isPalindrome(head):
        print("The linked list is a palindrome.")
    else:
        print("The linked list is not a palindrome.")
        
Complexity Analysis
Time Complexity: O(2xN) The algorithm involves traversing the linked list twice. The first traversal finds the middle and reverses the second half, while the second traversal compares elements from both halves. Since each traversal covers N/2 elements, the total time complexity is O(N/2 + N/2 + N/2 + N/2), which simplifies to O(2N), ultimately reducing to O(N).

Space Complexity: O(1) This approach uses a constant amount of additional space, regardless of the linked list's size. It does not require any extra data structures that depend on the input size, resulting in a space complexity of O(1).

'''
# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head):
        stack = []
        temp = head
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next
        temp = head
        while temp is not None:
            if temp.val != stack.pop():
                return False
            temp = temp.next
        return True