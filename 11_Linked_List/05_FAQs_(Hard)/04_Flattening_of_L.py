'''
Given a special linked list containing n head nodes where every node in the linked list contains two pointers:

‘Next’ points to the next node in the list
‘Child’ pointer to a linked list where the current node is the head
Each of these child linked lists is in sorted order and connected by a 'child' pointer.



Flatten this linked list such that all nodes appear in a single sorted layer connected by the 'child' pointer and return the head of the modified list.


Examples:
Input:



Output: head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12

Explanation: All the linked lists are joined together and sorted in a single level through the child pointer.

Input:



Output: head -> 2 -> 4 -> 5 -> 10 -> 12 -> 13 -> 16 -> 17 -> 20

Explanation: All the linked lists are joined together and sorted in a single level through the child pointer.

Constraints:
n == Number of head nodes
1 <= n <= 100
1 <= Number of nodes in each child linked list <= 100
0 <= ListNode.val <= 1000
All child linked lists are sorted in non-decreasing order

Hint 1

Hint 2

#brute
Intuition
The given linked list can be transformed into a single level sorted list by initializing an array to temporarily store nodes during traversal. Traverse the list, first following the top-level next pointers, then accessing each node's child pointers, adding all nodes to the array.

Sort the array to arrange the values sequentially, then create and return a new linked list from the sorted array.

Approach
Initialize an array to store node values and traverse the list, collecting values from both top-level and child nodes.
Sort the array to arrange the values in ascending order.
Create and return a new linked list from the sorted array.

class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

class Solution:
    # Function to convert a vector to a linked list
    def convertArrToLinkedList(self, arr):
        #Create a dummy node to serve as the head of the linked list 
        dummyNode = ListNode(-1)
        temp = dummyNode

        # Iterate through the vector and create nodes with vector elements 
        for i in range(len(arr)):
            # Create a new node with the vector element
            temp.child = ListNode(arr[i])
            
            # Update the temporary pointer
            temp = temp.child
        
        #Return the linked list starting from the next of the dummy node 
        return dummyNode.child

    # Function to flatten a linked list with child pointers 
    def flattenLinkedList(self, head):
        arr = []

        # Traverse through the linked list
        while head is not None:
            #Traverse through the child nodes of each head node 
            t2 = head
            
            while t2 is not None:
                # Store each node's data in the array
                arr.append(t2.val)
                
                # Move to the next child node
                t2 = t2.child

            # Move to the next head node
            head = head.next

        # Sort the array containing node values
        arr.sort()

        # Convert the sorted array back to a linked list
        return self.convertArrToLinkedList(arr)

# Function to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.child
    print()

# Function to print the linked list in a grid-like structure
def printOriginalLinkedList(head, depth):
    while head is not None:
        print(head.val, end="")

        #If child exists, recursively print it with indentation 
        if head.child:
            print(" -> ", end="")
            printOriginalLinkedList(head.child, depth + 1)

        # Add vertical bars for each level in the grid
        if head.next:
            print()
            for i in range(depth):
                print("| ", end="")
        
        head = head.next

if __name__ == "__main__":
    # Create a linked list with child pointers
    head = ListNode(5)
    head.child = ListNode(14)

    head.next = ListNode(10)
    head.next.child = ListNode(4)

    head.next.next = ListNode(12)
    head.next.next.child = ListNode(20)
    head.next.next.child.child = ListNode(13)

    head.next.next.next = ListNode(7)
    head.next.next.next.child = ListNode(17)

    # Print the original linked list structure
    print("Original linked list:")
    printOriginalLinkedList(head, 0)

    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to flatten the linked list
    flattened = sol.flattenLinkedList(head)
    
    # Printing the flattened linked list
    print("\nFlattened linked list: ", end="")
    printLinkedList(flattened)

Complexity Analysis
Time Complexity: O(NxM) + O(NxM log(NxM)) + O(NxM) where N is the number of nodes along the next pointers and M is the number of nodes along the child pointers.

O(NxM) because we traverse through all the nodes, iterating through N nodes along the next pointers and M nodes along the child pointers.
O(NxM log(NxM)) because we sort the array containing NxM total elements.
O(NxM) because we reconstruct the linked list from the sorted array by iterating over the NxM elements.
Space Complexity: O(NxM) + O(NxM) where N is the number of nodes along the next pointers and M is the number of nodes along the child pointers.

O(NxM) for storing all the elements in an additional array for sorting.
O(NxM) to reconstruct the linked list from the array after sorting.


#Optimal
Intuition
The optimized approach is based on the fact that the child linked lists are already sorted. By merging these pre-sorted lists directly during traversal, we can eliminate the additional space and time complexity generated by sorting.

Instead of collecting all node values into an array and then sorting them, we can merge these sorted vertical linked lists efficiently in place. This eliminates the need for additional sorting steps and avoids allocating extra space for the combined linked list.

The base case ensures the termination of the recursion when there's either no list or only a single node remaining. The recursive function then handles the merging of the remaining lists after recursive flattening, creating a sorted flattened linked list.

Approach
Establish base case conditions by checking if the head is null or has no next pointer. If either condition is met, return the head, as there is no further flattening or merging required.

Recursively initiate the flattening process by calling flattenLinkedList on the next node (head -> next). The result of this recursive call will be the head of the flattened and merged linked list.

Within the recursive call, perform merge operations by calling a merge function. This function merges the current list with the already flattened and merged list based on their data values. The merged list is then updated in the head and returned as the result of the flattening process.

class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

class Solution:
    #Merge the two linked lists in a particular order based on the data value
    def merge(self, list1, list2):
        #Create a dummy node as a  placeholder for the result 
        dummyNode = ListNode(-1)
        res = dummyNode

        # Merge the lists based on data values
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                res.child = list1
                res = list1
                list1 = list1.child
            else:
                res.child = list2
                res = list2
                list2 = list2.child
            res.next = None

        # Connect the remaining elements if any
        if list1:
            res.child = list1
        else:
            res.child = list2

        # Break the last node's link to prevent cycles
        if dummyNode.child:
            dummyNode.child.next = None

        return dummyNode.child

    # Function to flatten a linked list with child pointers 
    def flattenLinkedList(self, head):
        # If head is null or there is no next node
        if head is None or head.next is None:
            return head # Return head

        # Recursively flatten the rest of the linked list
        mergedHead = self.flattenLinkedList(head.next)

        # Merge the lists
        head = self.merge(head, mergedHead)
        return head

# Function to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.child
    print()

# Function to print the linked list in a grid-like structure
def printOriginalLinkedList(head, depth):
    while head is not None:
        print(head.val, end="")

        #If child exists, recursively print it with indentation 
        if head.child:
            print(" -> ", end="")
            printOriginalLinkedList(head.child, depth + 1)

        # Add vertical bars for each level in the grid
        if head.next:
            print()
            for i in range(depth):
                print("| ", end="")
        
        head = head.next

if __name__ == "__main__":
    # Create a linked list with child pointers
    head = ListNode(5)
    head.child = ListNode(14)

    head.next = ListNode(10)
    head.next.child = ListNode(4)

    head.next.next = ListNode(12)
    head.next.next.child = ListNode(20)
    head.next.next.child.child = ListNode(13)

    head.next.next.next = ListNode(7)
    head.next.next.next.child = ListNode(17)

    # Print the original linked list structure
    print("Original linked list:")
    printOriginalLinkedList(head, 0)

    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to flatten the linked list
    flattened = sol.flattenLinkedList(head)
    
    # Printing the flattened linked list
    print("\nFlattened linked list: ", end="")
    printLinkedList(flattened)

Complexity Analysis
Time Complexity: O(Nx(2M)) ~ O(2NxM) where N is the length of the linked list along the next pointer and M is the length of the linked list along the child pointers.

The merge operation in each recursive call takes time complexity proportional to the length of the linked lists being merged as they have to iterate over the entire lists. Since the vertical depth of the linked lists is assumed to be M, the time complexity for a single merge operation is proportional to O(2M).
This operation is performed N number of times (to each and every node along the next pointer list) hence the resultant time complexity becomes O(Nx2M).
Space Complexity: O(1) as this code uses no external space or additional data structures to store values. But a recursive stack uses O(N) space to build the recursive calls for each node along the next pointer list.

'''

# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

class Solution:
    def convertArrToLinkedList(self, arr):
        dummyNode = ListNode(-1)
        temp = dummyNode
        for i in range(len(arr)):
            temp.child = ListNode(arr[i])
            temp = temp.child
        return dummyNode.child

    # Function to flatten a linked list with child pointers 
    def flattenLinkedList(self, head):
        arr = []
        while head is not None:
            t2 = head
            while t2 is not None:
                arr.append(t2.val)
                t2 = t2.child
            head = head.next
        arr.sort()
        return self.convertArrToLinkedList(arr)
    