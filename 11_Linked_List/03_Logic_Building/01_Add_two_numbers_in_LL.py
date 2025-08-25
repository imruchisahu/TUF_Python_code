'''
Given two non-empty linked lists l1 and l2 which represent two non-negative integers.



The digits are stored in reverse order with each node storing one digit.

Add two numbers and return the sum as a linked list.



The sum Linked List will be in reverse order as well.
The Two given Linked Lists represent numbers without any leading zeros, except when the number is zero itself.

Examples:
Input: l1 = head -> 5 -> 4, l2 = head -> 4

Output: head -> 9 -> 4

Explanation: l1 = 45, l2 = 4.

l1 + l2 = 45 + 4 = 49.

Input: l1 = head -> 4 -> 5 -> 6, l2 = head -> 1 -> 2 -> 3

Output: head -> 5 -> 7 -> 9

Explanation: l1 = 654, l2 = 321.

l1 + l2 = 654 + 321 = 975.

Input: l1 = head -> 1, l2 = head -> 8 -> 7

Output:
head -> 9 -> 7
Constraints:
1 <= Number of nodes in each Linked List <= 100
0 <= value of each node in both Linked List <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

Intuition
Imagine you have two numbers written on paper, with the digits arranged backward:

Number 1: 3 -> 2 -> 1 (Represents 123)
Number 2: 4 -> 5 -> 6 (Represents 654)

To add them, you'd start from the rightmost digits (ones place), add them up (1 + 4 = 5), then move left to the next pair (tens place: 2 + 5 = 7), and so on. If the sum of two digits is greater than or equal to 10, you'd carry over the '1' to the next digit position.

In this problem, the numbers are stored in linked lists, which are essentially chains of nodes, each holding a single digit. The linked lists are in reverse order, just like our example.

Approach
Simultaneous Traversal: Traverse both linked lists at the same time, node by node.

Digit-wise Addition: At each step, add the values stored in the current nodes from both lists. Also, add any carry-over from the previous addition.

Create New Node: Calculate the result digit by taking the modulo 10 of the sum. Create a new node to store this digit.

Carry Over: If the sum is 10 or greater, carry over the '1' to the next addition.

Update Pointers: Move the pointers of both lists to their next nodes, and the pointer of the result list to the newly created node.

Continue: Repeat steps 2-5 until you reach the end of both input lists. If there's a carry-over at the end, create one more node for it.

Note that we use a dummy head to simplify the code. Without a dummy head, you would have to write extra conditional statements to initialize the head's value.

# Definition of Singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to add two numbers as linked list
    def addTwoNumbers(self, l1, l2):
        # Dummy node to act as the 
        # starting point of the result list
        dummy = ListNode()
        # Temp pointer to build 
        # the result list
        temp = dummy
        # Initialize carry
        carry = 0

        # Iterate while there are nodes in l1 or l2, 
        # or there's a carry to process
        while l1 or l2 or carry:
            sum = 0

            # Add the value from l1 
            # if available
            if l1:
                sum += l1.val
                l1 = l1.next

            # Add the value from l2 
            # if available
            if l2:
                sum += l2.val
                l2 = l2.next

            # Add the carry
            sum += carry
            # Update the carry
            carry = sum // 10

            # Create a new node with the digit value 
            # and attach it to the result list
            node = ListNode(sum % 10)
            temp.next = node
            # Move to the 
            # next position in the result list
            temp = temp.next

        # Return the result list
        # skipping the dummy node
        return dummy.next

# Function to print the linked list
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

if __name__ == "__main__":
    # Manual creation of linked list
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    # Instance of solution class
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    # Print the result
    printList(result)

    

# Function to print the linked list
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

if __name__ == "__main__":

Complexity Analysis
Time Complexity: O(max(M, N)) Here, M and N represent the sizes of the linked lists l1 and l2, respectively. The algorithm traverses both lists at most once, hence, the time complexity depends on the length of the longer list.

Space Complexity: O(max(M,N)) The length of the new list is at most max(M, N)+1.

'''
# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        # Temp pointer to build 
        # the result list
        temp = dummy
        # Initialize carry
        carry = 0

        # Iterate while there are nodes in l1 or l2, 
        # or there's a carry to process
        while l1 or l2 or carry:
            sum = 0

            # Add the value from l1 
            # if available
            if l1:
                sum += l1.val
                l1 = l1.next

            # Add the value from l2 
            # if available
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum // 10
            node = ListNode(sum % 10)
            temp.next = node
            temp = temp.next
        return dummy.next
