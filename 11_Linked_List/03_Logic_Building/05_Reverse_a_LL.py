'''
Given the head of a singly linked list. Reverse the given linked list and return the head of the modified list.


Examples:
Input: head -> 1 -> 2 -> 3 -> 4 -> 5

Output: head -> 5 -> 4 -> 3 -> 2 -> 1

Explanation: All the links are reversed and the head now points to the last node of the original list.

Input: head -> 6 -> 8

Output: head -> 8 -> 6

Explanation: All the links are reversed and the head now points to the last node of the original list.

This can be seen like: 6 <- 8 <- head.

Input: head -> 1

Output:
head -> 1
Constraints:
0 <= number of nodes in the Linked List <= 105
0 <= ListNode.val <= 104

#Iterative
Intuition
To reverse a linked list without using extra space, we change the direction of the links between the nodes. Think of it like flipping the arrows between the nodes. This means each node will point to the one before it instead of the one after it. By doing this, the last node in the original list becomes the first node in the reversed list. This way, we efficiently reverse the list without needing any extra memory.

Approach
Initialize Pointers: Start by setting two pointers, temp and prev, at the head of the linked list and NULL respectively. The temp pointer will be used to traverse the list, while the prev pointer will help reverse the direction of the links.

Traverse and Reverse: Move through the linked list with the temp pointer. For each node:

Save the next node in a variable called front. This ensures you don't lose track of the remaining list.
Change the next pointer of the current node (temp) to point to the previous node (prev). This action reverses the link.
Move the prev pointer to the current node (temp). This prepares prev for the next iteration.
Move the temp pointer to the next node (front). This continues the traversal.
Complete the Reversal: Continue the process until the temp pointer reaches the end of the list (NULL). At this point, the prev pointer will be at the new head of the reversed list.

Return the New Head: Finally, return the prev pointer as it now points to the head of the reversed linked list.

# Definition of singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #Function to reverse a linked list Using the 3-pointer approach
    def reverseList(self, head: ListNode) -> ListNode:
        #Initialize 'temp' at head of linked list
        temp = head
        
        #Initialize pointer 'prev' to NULL,representing the previous node
        prev = None
        
        #Traverse the list, continue till 'temp' reaches the end (NULL)
        while temp:
            #Store the next node in 'front' to preserve the reference
            front = temp.next
            
        #Reverse the direction of the current node's 'next' pointerto point to 'prev
            temp.next = prev
            
            #Move 'prev' to the current node for the next iteration
            prev = temp
            
            #Move 'temp' to the 'front' node advancing the traversal
            temp = front
        
    #Return the new head of the reversed linked list
        return prev

# Function to print the linked list
def printLinkedList(head: ListNode):
    temp = head
    while temp:
        print(temp.val, end=" ")
        temp = temp.next
    print()

if __name__ == "__main__":
    # Create a linked list with
    # Values 1, 3, 2, and 4
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(4)

    # Print the original linked list
    print("Original Linked List: ", end="")
    printLinkedList(head)

    # Solution instance
    solution = Solution()
    # Reverse the linked list
    head = solution.reverseList(head)

    # Print the reversed linked list
    print("Reversed Linked List: ", end="")
    printLinkedList(head)


Complexity Analysis
Time Complexity: O(N) because the algorithm traverses the entire linked list once, where 'N' is the number of nodes in the list. Since each node is visited exactly once during the traversal, the time complexity is linear, O(N).

Space Complexity: O(1) because the algorithm uses only a constant amount of additional space. This is achieved by utilizing three pointers (prev, temp, and front) to reverse the list without any significant extra memory usage, resulting in constant space complexity, O(1).


#Recursive
Intuition
Recursion enables us to decompose a problem into more manageable, smaller subproblems, which we can then solve one at a time until we get to the base case, or most straightforward answer. After that, we solve the initial problem by combining the outcomes of these smaller solutions.

When recursively reversing a linked list, we start by taking into account the complete list with N nodes. We can break this down recursively by starting with N-1 nodes, moving on to N-2 nodes, and so on, until we reach a single node.

In the base case, reversing a list with one node is straightforward because the list is already in reverse. We simply return this node. When we return from each recursive call, we flip the pointers to reverse the linkages between nodes, thereby reversing the entire list.

This method effectively manages the reversal process by using the power of recursion to break down the task into smaller, more manageable parts.

Approach
Base Case:
First, check if the linked list is empty or has only one node. In these cases, the list is already reversed, so simply return the head.

Recursive Function:
The main part of the algorithm is a recursive function that handles the reversal of the linked list. This function works as follows:

If the base case is not met, the function calls itself recursively. This process continues until the base case is reached, effectively reversing the list starting from the second node onwards.

Returning the New Head:
After the recursion completes, the function returns the new head of the reversed linked list. This new head was the last node of the original list before the reversal, and it becomes the first node in the newly reversed list.

Steps:

Step 1: Establish Base Case Conditions: First, check if the linked list is either empty or has only one node. If this condition is met, the list is already reversed, so return the head as it is.

Step 2: Recursively Reverse the List: Begin the recursive step by starting to reverse the linked list from the second node onward. Make a recursive call to the function, passing the next node as the argument.

Step 3: Preserve Access to Remaining Nodes: To ensure access to the rest of the linked list while reversing, store a reference to the node following the current head node. This maintains the continuity of the link sequence during the reversal process.

Step 4: Reverse Link Direction: Adjust the 'next' pointer of the node following the current head to point back to the current head. This effectively reverses the link between these two nodes.

Step 5: Prevent Cyclic References: To prevent creating a cycle, break the old link from the current head node to the next node by setting the head's next pointer to NULL. This ensures that the reversed part of the list does not form a loop.

Step 6: Return the New Head: Finally, return the new head of the reversed linked list. This new head is the node that was last in the original list before the reversal started.

# Definition of singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #Function to reverse a singly linked list using recursion 
    def reverseList(self, head: ListNode) -> ListNode:
        #Base case:
        #If the linked list is empty or has only one node,
        #return the head as it is already reversed. 
        if not head or not head.next:
            return head
        
        #Recursive step:
        #Reverse the linked list starting from the second node (head.next). 
        newHead = self.reverseList(head.next)
        
        #Save a reference to the node following the current 'head' node. 
        front = head.next
        
        #Make the 'front' node point to the current 'head' node in the reversed order. 
        front.next = head
        
        #Break the link from the current 'head' node to the 'front' node to avoid cycles.
        head.next = None
        
        # Return the 'newHead,' which is the new head of the reversed 
        linked list. 
        return newHead

# Function to print the linked list
def printLinkedList(head: ListNode):
    temp = head
    while temp:
        print(temp.val, end=" ")
        temp = temp.next
    print()

if __name__ == "__main__":
    # Create a linked list with values 1, 3, 2, and 4
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(4)

    # Print the original linked list
    print("Original Linked List: ", end="")
    printLinkedList(head)

    # Solution instance
    solution = Solution()
    # Reverse the linked list
    head = solution.reverseList(head)

    # Print the reversed linked list
    print("Reversed Linked List: ", end="")
    printLinkedList(head)


Complexity Analysis
Time Complexity: O(N) because the algorithm traverses the linked list twice: once to push the values onto the stack, and once to pop the values and update the linked list. Since each node is visited during both traversals, the time complexity is linear, O(N).

Space Complexity: O(1) The algorithm does not use additional space explicitly for data structures or allocations during the reversal process. However, it does use stack space due to recursion, storing function calls and associated variables during the recursive traversal and reversal of the list. Despite this, no extra memory beyond the program's existing execution space is allocated, maintaining a space complexity of O(1).
'''
# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        temp = head
        prev = None
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev