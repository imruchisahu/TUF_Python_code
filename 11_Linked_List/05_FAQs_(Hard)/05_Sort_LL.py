'''
Given the head of a singly linked list. Sort the values of the linked list in non-decreasing order and return the head of the modified linked list.


Examples:
Input: head -> 5 -> 6 -> 1 -> 2 -> 1

Output: head -> 1 -> 1 -> 2 -> 5 -> 6

Explanation: 1 <= 1 <= 2 <= 5 <= 6

Input: head -> 6 -> 5 -> -1 -> -2 -> -3

Output: head -> -3 -> -2 -> -1 -> 5 -> 6

Explanation: -3 <= -2 <= -1 <= 5 <= 6

Input: head -> -1 -> -2 -> -3 -> -1

Output:
head -> -3 -> -2 -> -1 -> -1
Constraints:
0 <= number of nodes in the linked list <= 1000
-104 <= ListNode.val <= 104

#Brute
#Intuition
A straightforward approach to sorting a linked list involves converting the linked list into an array. Once converted, the array can be sorted using any standard sorting algorithm. After sorting, a new linked list can be created using the sorted values from the array.

Approach
Create an empty array to store the node values.
Traverse the linked list using a temporary pointer starting at the head, pushing each node's value into the array, and moving the pointer to the next node.
Sort the array containing the node values in ascending order.
Convert the sorted array back into a linked list by reassigning the values from the sorted array to the nodes, overwriting the values sequentially according to the order in the array.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to sort Linked List
    def sortList(self, head):
        # List to store node values
        arr = []

        # Temporary pointer to traverse
        # the linked list
        temp = head

        # Traverse the linked list
        while temp:
            arr.append(temp.val)
            temp = temp.next

        # Sort list containing node values
        arr.sort()

        # Reassign sorted values to
        # linked list nodes
        temp = head
        for val in arr:
            # Update the node's data
            temp.val = val
            # Move to the next node
            temp = temp.next

        # Return the head
        return head

# Function to print the linked list
def printLinkedList(head):
    temp = head
    while temp:
        # Print the data of the current node
        print(temp.val, end=" ")
        # Move to the next node
        temp = temp.next
    print()

# Linked List: 3 2 5 4 1
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(5)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(1)

print("Original Linked List: ", end="")
printLinkedList(head)

solution = Solution()
# Sort the linked list
head = solution.sortList(head)

print("Sorted Linked List: ", end="")
printLinkedList(head)
                
Complexity Analysis
Time Complexity: O(N) + O(N log N) + O(N) for the following reasons:-

O(N): Time taken to traverse the linked list and store its data values in an array.
O(N log N): Time taken to sort the array of node values.
O(N): Time taken to traverse the sorted array and reassign values back to the linked list.
Here N represents the number of nodes in the linked list.

Space Complexity: O(N) because we need to store values of nodes of the linked lists in the array of size N where N is the length of the linked list.


#Optimal
#Intuition
Instead of using an external array to store node values, we can utilize an in-place sorting algorithm such as Merge Sort or Quick Sort, which can be adapted for linked lists. This approach avoids using additional space.
Merge Sort employs the divide and conquer strategy:-
Divides the linked list into smaller parts until they become trivial to sort (single node or empty list).
Merges and sorts the divided parts while combining them back together.
Approach
Base Case: If the linked list contains zero or one element, it is already sorted. Return the head node.
Split the List: Find the middle of the linked list using a slow and a fast pointer. Split the linked list into two halves at the middle node. The two halves will be left and right.
Recursion: Recursively apply merge sort to both halves obtained in the previous step. This step continues dividing the linked list until there's only one node in each half.
Merge Sorted Lists: Merge the sorted halves obtained from the recursive calls into a single sorted linked list. Compare the nodes from both halves and rearrange them to form a single sorted list. Update the head pointer to the beginning of the newly sorted list.
Return: Once the merging is complete, return the head of the sorted linked list.
Dry Run
Breaking down the list and then sorting the smaller parts
class ListNode:
    def _init_(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to merge two sorted linked lists
    def mergeTwoSortedLinkedLists(self, list1, list2):
        # Create dummy node to serve as head of merged list
        dummyNode = ListNode(-1)
        temp = dummyNode

        # Traverse both lists simultaneously
        while list1 is not None and list2 is not None:
            # Compare elements of both lists and link the smaller node to the merged list
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            # Move the temporary pointer to the next node
            temp = temp.next

        # If any list still has remaining elements, append them to the merged list
        if list1 is not None:
            temp.next = list1
        else:
            temp.next = list2

        # Return the merged list starting from the next of the dummy node
        return dummyNode.next

    # Function to find the middle of a linked list
    def findMiddle(self, head):
        # If the list is empty or has only one node, the middle is the head itself
        if head is None or head.next is None:
            return head

        # Initializing slow and fast pointers
        slow = head
        fast = head.next

        # Move the fast pointer twice as fast as the slow pointer
        # When the fast pointer reaches the end, the slow pointer will be at the middle
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    # Function to perform merge sort on a linked list
    def sortList(self, head):
        # Base case: if the list is empty or has only one node, it is already sorted, so return the head
        if head is None or head.next is None:
            return head
        
        # Find middle of list using findMiddle function
        middle = self.findMiddle(head)
        
        # Divide the list into two halves
        right = middle.next
        middle.next = None
        left = head
        
        # Recursively sort left and right halves
        left = self.sortList(left)
        right = self.sortList(right)
        
        # Merge the sorted halves using the mergeTwoSortedLinkedLists function
        return self.mergeTwoSortedLinkedLists(left, right)

# Function to print the linked list
def printLinkedList(head):
    temp = head
    while temp is not None:
        # Print the data of the current node
        print(temp.val, end=" ") 
        # Move to the next node
        temp = temp.next
    print()

if _name_ == "_main_":
    # Linked List: 3 2 5 4 1
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(5)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(1)

    print("Original Linked List: ", end="")
    printLinkedList(head)

    solution = Solution()
    # Sort the linked list
    head = solution.sortList(head)

    print("Sorted Linked List: ", end="")
    printLinkedList(head)


Complexity Analysis
Time Complexity: O(N log N) where N is the number of nodes in the linked list. Finding the middle node of the linked list requires traversing it linearly taking O(N) time complexity and to reach the individual nodes of the list, it has to be split log N times (continuously halve the list until we have individual elements).

Space Complexity: O(1) as no additional data structures or space is allocated for storage during the merging process. However, space proportional to O(log N) stack space is required for the recursive calls. The maximum recursion depth of log N height is occupied on the call stack.

'''
# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head):
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        arr.sort()
        temp = head
        for val in arr:
            temp.val = val
            temp = temp.next
        return head