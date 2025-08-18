'''
Given the head of a singly Linked List. Traverse the entire Linked List and return its elements in an array in the order of their appearance.


Examples:
Input: head -> 5 -> 4 -> 3 -> 1 -> 0

Output: [5, 4, 3, 1, 0]

Explanation: The nodes in the Linked List are 5 -> 4 -> 3 -> 1 -> 0, with the head pointing to node with value 5.

Input: head -> 1

Output: [1]

Explanation: Only one node present in the list.

Input: head -> 0 -> 2 -> 5

Output:
[0, 2, 5]
Constraints:
0 <= number of nodes in the Linked List <= 105
0 <= ListNode.val <= 104
Intuition
Start iterating from the head of the linked list and keep moving to the subsequent node until we reach the end node, which points to NULL.
Approach
Initialize a pointer variable let's say temp to store the copy of the original linked list's head because we need to preserve the original list.
Declare a vector data structure let's say ans to store the result.
Keep traversing the linked list and store the value of the present node in the ans vector, until the next node points to null. Return the ans vector.


Complexity Analysis
Time Complexity: O(N) since we are visiting each node once. Here N represents the length of the linked list or the number of nodes present in the linked list.

Space Complexity: O(N) since we are storing the result in a vector.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function for Linked List Traversal
    def LLTraversal(self, head: ListNode) -> list:
        # Storing a copy 
        #Of the linked list
        temp = head
        #To store 
        #Values sequentially
        ans = []

        #Keep traversing
        #Until the None 
        #Is not encountered
        while temp is not None:
            #Storing of the values
            ans.append(temp.val)
            #Storing the address 
            #Of the next node
            temp = temp.next

        #Returning the answer 
        return ans

if __name__ == "__main__":
    #Manual creation of nodes
    y1 = ListNode(2)
    y2 = ListNode(5)
    y3 = ListNode(8)
    y4 = ListNode(7)

    #Linking the nodes
    y1.next = y2
    y2.next = y3
    y3.next = y4

    #Solution class
    sol = Solution()

    #Calling LLTraversal method
    result = sol.LLTraversal(y1)

    #Printing the result
    print("Linked List Values:")
    for val in result:
        print(val, end=" ")
    print()

'''
    