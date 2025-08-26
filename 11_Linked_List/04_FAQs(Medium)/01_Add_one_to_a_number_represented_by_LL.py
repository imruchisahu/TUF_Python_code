'''
Given the head of a singly linked list representing a positive integer number. Each node of the linked list represents a digit of the number, with the 1st node containing the leftmost digit of the number and so on. The task is to add one to the value represented by the linked list and return the head of a linked list containing the final value.



The number will contain no leading zeroes except when the value represented is zero itself.


Examples:
Input: head -> 1 -> 2 -> 3

Output: head -> 1 -> 2 -> 4

Explanation: The number represented by the linked list = 123.

123 + 1 = 124.

Input: head -> 9 -> 9

Output: head -> 1 -> 0 -> 0

Explanation: The number represented by the linked list = 99.

99 + 1 = 100.

Input: head -> 9

Output:
head -> 1 -> 0
Constraints:
0 <= number of nodes in the Linked List <= 105
0 <= ListNode.val <= 9
No leading zeroes in the value represented.

#Iterative Solution
#Intuition
Imagine you have a number represented as a linked list, where each node contains a single digit. The first node contains the leftmost digit. Our goal is to add one to this number. This might sound simple, but we need to handle the digit carry-over, just like we do when adding numbers manually. Starting from the rightmost digit makes it easier to manage carry-overs. However, since our linked list starts from the leftmost digit, we need to reverse the list first. This makes it easier to add one from the least significant digit and manage any carry-over.

Approach
Reverse the Linked List: Reverse the linked list so we can start the addition from the rightmost digit.
Add One: Add one to the first digit of the reversed list. If there’s a carry (result is 10), set the current digit to 0 and carry over 1 to the next digit.
Handle the Carry: If there’s still a carry after reaching the end of the list, add a new node with the digit 1.
Reverse Again: Reverse the list again to restore the original order, now with the added value.
Return the New Head: Return the head of the modified linked list.

# Definition of singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to reverse the linked list
    def reverseList(self, head: ListNode) -> ListNode:
        # Initialize pointers
        prev = None
        current = head
        next = None
        
        while current is not None:
            # Store next node
            next = current.next
            # Reverse the link
            current.next = prev
            # Move prev to current
            prev = current
            # Move current to next
            current = next
        
        return prev
    
    # Function to add one to Linked List
    def addOne(self, head: ListNode) -> ListNode:
        # Reverse the linked list
        head = self.reverseList(head)
        
        # Create a dummy node
        current = head
        # Initialize carry with 1
        carry = 1  
        
        while current is not None:
            # Sum the current node's value and the carry
            sum = current.val + carry
            # Update carry
            carry = sum // 10
            # Update the node's value
            current.val = sum % 10
            
            # If no carry left, break the loop
            if carry == 0:
                break
            
            # If we've reached the end of the list and there's still a carry,
            # add a new node with the carry value
            if current.next is None and carry != 0:
                current.next = ListNode(carry)
                break
            
            # Move to the next node
            current = current.next
        
        # Reverse the list 
        head = self.reverseList(head)
        
        # New head
        return head

# Function to print the linked list
def printList(head: ListNode):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()

if __name__ == "__main__":
    # Creation of Linked List
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)

    # Solution instance
    solution = Solution()
    head1 = solution.addOne(head1)
    print("Result after adding one: ", end="")
    printList(head1)

Complexity Analysis
Time Complexity: O(N) because we traverse the linked list three times, each with a time complexity of O(N), resulting in O(3N), which simplifies to O(N) since constant factors are ignored in Big-O notation. Here, N is the number of nodes in the linked list.

Space Complexity: O(1) because we use a constant amount of extra space for pointers and variables.

#Recursive Solution
Intuition
When adding one to a number represented as a linked list, think of it as the process of incrementing the least significant digit (the last node) and propagating any carry to the more significant digits (the previous nodes). This process is similar to the manual addition we do with pen and paper. Starting from the least significant digit, if there is a carry (i.e., the digit becomes 10 after addition), set the current digit to 0 and move the carry to the next significant digit. If there's still a carry after processing the most significant digit (the head of the list), we need to add a new node to the front of the list to accommodate the carry.
Approach
To add one to a number represented as a linked list, we use a recursive function addHelper. This function traverses the list to the end, with the base case being when the current node is NULL, returning a carry of 1 to signify adding one to the number.

During each recursive call, we add the carry returned by the next node to the current node's value. If the current node's value is less than 10, no further carry is needed, so we return 0. If the value is 10 or more, we set the current node's value to 0 and return a carry of 1 to be added to the next significant digit.

After processing all nodes, we check if there's a carry left. If there is, we create a new node with a value of 1 and set it as the new head of the list. This handles cases where an additional digit is needed, like converting 999 into 1000.
# Definition of singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Helper function to add one to the linked list
    def addHelper(self, temp: ListNode) -> int:
        #If the list is empty return a carry of 1 
        if temp is None:
            return 1
        
        #Recursively call addHelper For the next node 
        carry = self.addHelper(temp.next)
        
        # Add the carry to the current node's value 
        temp.val += carry
        
        # If the current node's value is less than 10 no further carry is needed 
        if temp.val < 10:
            return 0
        
        #If the current node's value is 10 or more set it to 0 and return a carry of 1 
        temp.val = 0
        return 1

    def addOne(self, head: ListNode) -> ListNode:
        #Call the helper function to start the addition process 
        carry = self.addHelper(head)
        
        #If there is a carry left after processing all nodes add a new node at the head 
        if carry == 1:
            newNode = ListNode(1)
            #Link the new node to the current head 
            newNode.next = head
            #Update the head to the new node 
            head = newNode
        # Return the head 
        return head

# Function to print the linked list
def printLinkedList(head: ListNode):
    temp = head
    # Traverse the linked list and print each node's value
    while temp:
        print(temp.val, end=" ")
        temp = temp.next
    print()

if __name__ == "__main__":
    # Create a linked list with values 9, 9, 9 (999 + 1 = 1000)
    head = ListNode(9)
    head.next = ListNode(9)
    head.next.next = ListNode(9)

    # Print the original linked list
    print("Original Linked List: ", end="")
    printLinkedList(head)

    # Add one to the linked list
    solution = Solution()
    head = solution.addOne(head)

    # Print the modified linked list
    print("Linked List after adding one: ", end="")
    printLinkedList(head)


Complexity Analysis
Time Complexity: O(N), where N is the number of nodes in the linked list. This is because each node in the linked list is visited exactly once by the recursive addHelper function. The process involves traversing the entire list to reach the end, and then propagating the carry back through each node, resulting in a linear time complexity of O(N).

Space Complexity: O(N), due to the recursion stack. Since the addHelper function calls itself recursively for each node in the list, the maximum depth of the recursion stack is N, where N is the number of nodes in the linked list. This means the space required for the recursion stack grows linearly with the size of the list, leading to a space complexity of O(N).

'''
# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addHelper(self, temp: ListNode) -> int:

        if temp is None:
            return 1
        carry = self.addHelper(temp.next)
        temp.val += carry
        if temp.val < 10:
            return 0
        temp.val = 0
        return 1

    def addOne(self, head):
        carry = self.addHelper(head)
        if carry == 1:
            newNode = ListNode(1)
            newNode.next = head
            head = newNode
        # Return the head 
        return head