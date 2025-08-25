'''
Given the head of a singly linked list and an integer n. Remove the nth node from the back of the linked List and return the head of the modified list. The value of n will always be less than or equal to the number of nodes in the linked list.


Examples:
Input: head -> 1 -> 2 -> 3 -> 4 -> 5, n = 2

Output: head -> 1 -> 2 -> 3 -> 5

Explanation: The 2nd node from the back was the node with value 4.

Input: head -> 5 -> 4 -> 3 -> 2 -> 1, n = 5

Output: head -> 4 -> 3 -> 2 -> 1

Explanation: The 5th node from the back is the first node.

Input: head -> 9 -> 8 -> 7, n = 1

Output:
head -> 9 -> 8
Constraints:
1 <= number of nodes in the Linked List <= 105
0 <= ListNode.val <= 104
1 <= n <= number of nodes in the Linked List.

#Brute
Intuition
To delete the nth node from the end of a linked list, we first need to understand the formula (L-N+1), where L is the total length of the linked list. This formula helps us find the position of the node to delete from the start of the list:

L is the total number of nodes in the list. N is the position of the node from the end.
L - N gives the position of the node from the start in a 0-based index. Adding 1 converts it to a 1-based index, resulting in (L-N+1).

Using this formula, break the problem into two main steps:
Calculating the Length of the Linked List.
Deleting the (L-N+1)th Node from the Start.

Edge Cases to Consider:
If N equals 1: We need to delete the tail node.
If N equals the length of the linked list: We need to delete the head node.
Approach
Initialize and Traverse: Set a temp pointer to the head of the list and create a counter cnt initialized to 0. Traverse the list, incrementing cnt at each node to find the total length L.

Determine Position to Delete: Calculate the position of the node to delete as (L-N+1) from the start.

Traverse to Target Node: Reinitialize temp to the head and initialize a variable res to (L-N). Traverse the list, decrementing res at each node until it reaches 0, positioning temp at the (L-N)th node.

Delete the Node: Adjust the pointers to skip the (L-N+1)th node by linking the (L-N)th node to the (L-N+2)th node. Free the memory of the (L-N+1)th node.

Note: In the case of languages like Java, Python, and JavaScript, there is no need for the deletion of objects or nodes because these have an automatic garbage collection mechanism that automatically identifies and reclaims memory that is no longer in use.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to remove the nth node from end
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        cnt = 0
        temp = head

        # Count the number of nodes
        while temp:
            cnt += 1
            temp = temp.next

        # If N equals the total number of nodes, delete the head
        if cnt == n:
            return head.next

        # Calculate the position of the node to delete (res)
        res = cnt - n
        temp = head

        # Traverse to the node just before the one to delete
        while res > 1:
            res -= 1
            temp = temp.next

        # Delete the Nth node from the end
        temp.next = temp.next.next
        return head

# Function to print the linked list
def printLL(head: ListNode):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    N = 3
    head = ListNode(arr[0])
    head.next = ListNode(arr[1])
    head.next.next = ListNode(arr[2])
    head.next.next.next = ListNode(arr[3])
    head.next.next.next.next = ListNode(arr[4])

    # Solution instance
    solution = Solution()
    head = solution.removeNthFromEnd(head, N)
    printLL(head)

Complexity Analysis
Time Complexity: O(L) + O(L-N) We are calculating the length of the linked list and then iterating up to the (L-N)th node of the linked list, where L is the total length of the list and N is the position of the node to delete.

Space Complexity: O(1) as we have not used any extra space.


#optimal
Intuition
The brute force method for removing the nth node from the end of a linked list has a time complexity of O(2xL) in the worst case, where L is the length of the linked list. This is because the list is traversed twice: once to calculate the length and once to find and remove the node. Therefore, it is not the most efficient algorithm.

To enhance efficiency, we use a two-pointer technique involving a fast pointer and a slow pointer. The fast pointer is initially positioned exactly N nodes ahead of the slow pointer. Then, both pointers move one step at a time. When the fast pointer reaches the last node (the L-th node), the slow pointer will be at the (L-N)-th node. This allows us to remove the nth node from the end in a single traversal, improving the time complexity to O(L).

Approach
Initialize Pointers: Start by setting two pointers, slow and fast, at the head of the linked list. Move the fast pointer N nodes ahead of the slow pointer.

Simultaneous Traversal: Traverse the linked list with both pointers moving one step at a time. Continue this until the fast pointer reaches the end of the list (the Lth node). At this point, the slow pointer will be at the (L-N)th node.

Adjust Pointers: Update the slow pointer to skip the next node by pointing it to the (L-N+2)th node. This effectively removes the Nth node from the end of the list.

Delete the Node: Free the memory occupied by the node that was skipped to complete the deletion process.

Note: Freeing up memory space explicitly is not available in some languages like Java and JavaScript. These languages rely on garbage collection to automatically manage memory. In these languages, the garbage collector will eventually remove the skipped node once there are no references to it. However, in languages like C++ and C, it's essential to free the memory to prevent memory leaks explicitly.

# Definition of Single Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to remove the nth node from end
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Creating pointers
        fastp = head
        slowp = head

        # Move the fastp pointer N nodes ahead
        for _ in range(n):
            fastp = fastp.next

        # If fastp becomes NULL the Nth node from the end is the head
        if not fastp:
            return head.next

        # Move both pointers Until fastp reaches the end
        while fastp.next:
            fastp = fastp.next
            slowp = slowp.next

        # Delete the Nth node from the end
        slowp.next = slowp.next.next
        return head

# Function to print the linked list
def printLL(head: ListNode):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    N = 3
    # Creation of linked list
    head = ListNode(arr[0])
    head.next = ListNode(arr[1])
    head.next.next = ListNode(arr[2])
    head.next.next.next = ListNode(arr[3])
    head.next.next.next.next = ListNode(arr[4])

    # Solution instance
    solution = Solution()
    head = solution.removeNthFromEnd(head, N)
    printLL(head)

Complexity Analysis
Time Complexity: O(N) since the fast pointer will traverse the entire linked list, where N is the length of the linked list.

Space Complexity: O(1), as we have not used any extra space.
'''
# Definition for Singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        fastp = head
        slowp = head
        for _ in range(n):
            fastp = fastp.next
        if not fastp:
            return head.next
        while fastp.next:
            fastp = fastp.next
            slowp = slowp.next

        # Delete the Nth node from the end
        slowp.next = slowp.next.next
        return head