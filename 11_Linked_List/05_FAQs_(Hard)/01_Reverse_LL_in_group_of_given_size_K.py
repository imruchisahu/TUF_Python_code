'''
Given the head of a singly linked list containing integers, reverse the nodes of the list in groups of k and return the head of the modified list. If the number of nodes is not a multiple of k, then the remaining nodes at the end should be kept as is and not reversed.



Do not change the values of the nodes, only change the links between nodes.


Examples:
Input: head -> 1 -> 2 -> 3 -> 4 -> 5, k = 2

Output: head -> 2 -> 1 -> 4 -> 3 -> 5

Explanation: The groups 1 -> 2 and 3 -> 4 were reversed as 2 -> 1 and 4 -> 3.

Input: head -> 1 -> 2 -> 3 -> 4 -> 5, k = 3

Output: head -> 3 -> 2 -> 1 -> 4 -> 5

Explanation: The groups 1 -> 2 -> 3 were reversed as 3 -> 2 -> 1.

Note that 4 -> 5 was not reversed.

Input: head -> 6 -> 1 -> 2 -> 3 -> 4 -> 7, k = 4

Output:
head -> 3 -> 2 -> 1 -> 6 -> 4 -> 7
Constraints:
1 <= k <= number of nodes in the linked list <= 105
-104 <= ListNode.val <= 104

Intuition
The intuition is to reverse the nodes of the linked list in groups of k by identifying each group, reversing the links within that group, and then connecting the reversed groups, leaving any remaining nodes as they are if the group is less than k.

Approach
First, traverse the linked list to identify segments of K nodes. For each segment, adjust the pointers within the segment to reverse the direction of the nodes. This involves iterating through the segment and changing the links between nodes.

Next, after reversing a segment, connect the reversed segment to the previous part of the list. Continue this process until you reach the end of the list.

Finally, if there are fewer than K nodes left at the end of the list, leave them as they are. Return the head of the modified linked list.

Below is the algorithm for the approach:-
Initialize a pointer temp to the head of the linked list. Using temp, traverse to the Kth node iteratively.
Upon reaching the Kth node, preserve the Kth node’s next node as nextNode and set the Kth node’s next pointer to null. This effectively breaks the linked list into a smaller list of size K that can be reversed and attached back.
Treat this segment from temp to the Kth node as an individual linked list and reverse it. This can be done using a helper function that reverses the linked list.
The reversed linked list segment returns a modified list with temp now at its tail and the Kth node pointing to its head. Update temp's next pointer to nextNode. If reversing the first segment of K nodes, update the head to the Kth node.
Continue this reversal process for further groups. If a segment has fewer than K nodes, leave them unmodified and return the new head. Use the prevLast pointer to maintain the link between the end of the previous reversed segment and the current segment.

# Definition of singly linked list:
class ListNode:
    def __init__(self, data1=0, next1=None):
        self.val = data1
        self.next = next1

class Solution:
    # Function to reverse a linked list 
    # Using the 3-pointer approach
    def reverseLinkedList(self, head):
    
        #Initialize 'temp' at head of linked list
        
        temp = head

    
        #Initialize pointer 'prev' to NULL, representing the previous node
        
        prev = None

        # Continue till 'temp' 
        # reaches the end (NULL)
        while temp is not None:
            
            #Store the next node in 'front' to preserve the reference
        
            front = temp.next

        
            #Reverse the direction of the current node's 'next' pointer to point to 'prev'
            
            temp.next = prev

        
            #Move 'prev' to the current node for the next iteration
        
            prev = temp

            
            #Move 'temp' to the 'front' node advancing the traversal
        
            temp = front

        # Return the new head 
        # of the reversed linked list
        return prev

    # Function to get the Kth node from a 
    # given position in the linked list
    def getKthNode(self, temp, k):
        # Decrement K 
        # as we already start 
        # from the 1st node
        k -= 1

        # Decrement K until it reaches the desired position
        while temp is not None and k > 0:
            # Decrement k as temp progresses
            k -= 1

            # Move to the next node
            temp = temp.next

        # Return the Kth node
        return temp

    # Function to reverse nodes in groups of K
    def reverseKGroup(self, head, k):
        
        #Initialize a temporary node to traverse the list
    
        temp = head

       
        #Initialize a pointer to track the last node of the previous group
    
        prevLast = None

        # Traverse through the linked list
        while temp is not None:
            # Get the Kth node of the current group
            kThNode = self.getKthNode(temp, k)

            
            #If the Kth node is NULL (not a complete group)
        
            if kThNode is None:
                
                #If there was a previous group, link the last node to the current node
                
                if prevLast:
                    prevLast.next = temp

                # Exit the loop
                break

            
            #Store the next node after the Kth node
            
            nextNode = kThNode.next

        
            #Disconnect the Kth node to prepare for reversal
            
            kThNode.next = None

            # Reverse the nodes from temp to the Kth node
            self.reverseLinkedList(temp)

        
            #Adjust the head if the reversal starts from the head
            
            if temp == head:
                head = kThNode
            else:
                
                #Link the last node of the previous group to the reversed group
                
                prevLast.next = kThNode

            
            #Update the pointer to the last node of the previous group
            
            prevLast = temp

            # Move to the next group
            temp = nextNode

        # Return the head of the modified linked list
        return head

# Function to print the linked list
def printLinkedList(head):
    temp = head
    while temp is not None:
        print(temp.val, end=" ")
        temp = temp.next
    print()

if __name__ == "__main__":
    # Create a linked list with values 5, 4, 3, 7, 9 and 2
    head = ListNode(5)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(7)
    head.next.next.next.next = ListNode(9)
    head.next.next.next.next.next = ListNode(2)

    # Print the original linked list
    print("Original Linked List: ", end="")
    printLinkedList(head)

    # Reverse the linked list in groups of K
    solution = Solution()
    head = solution.reverseKGroup(head, 4)

    # Print the reversed linked list
    print("Reversed Linked List: ", end="")
    printLinkedList(head)

Complexity Analysis
Time Complexity: O(2N) because it consists of actions of reversing segments of K and finding the Kth node, both of which operate in linear time. Thus, O(N) + O(N) = O(2N), which simplifies to O(N).

Space Complexity: O(1) because the code operates in place without any additional space requirements.

'''
# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLinkedList(self, head):
        temp = head
        prev=None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

    def getKthNode(self, temp, k):
        k -= 1
        while temp is not None and k > 0:
            k -= 1
            temp = temp.next
        return temp
    def reverseKGroup(self, head, k):
        temp = head
        prevLast= None
        while temp is not None:
            kThNode = self.getKthNode(temp, k)
            if kThNode is None:
                if prevLast:
                    prevLast.next = temp
                break

            nextNode = kThNode.next
            kThNode.next = None
            self.reverseLinkedList(temp)
            if temp == head:
                head = kThNode
            else:
                prevLast.next = kThNode
            prevLast = temp
            temp = nextNode
        return head

        
