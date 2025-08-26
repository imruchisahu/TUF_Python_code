'''
Given the head of a singly linked list containing integers, shift the elements of the linked list to the right by k places and return the head of the modified list. Do not change the values of the nodes, only change the links between nodes.


Examples:
Input: head -> 1 -> 2 -> 3 -> 4 -> 5, k = 2

Output: head -> 4 -> 5 -> 1 -> 2 -> 3

Explanation:

List after 1 shift to right: head -> 5 -> 1 -> 2 -> 3 -> 4.

List after 2 shift to right: head -> 4 -> 5 -> 1 -> 2 -> 3.

Input: head -> 1 -> 2 -> 3 -> 4 -> 5, k = 4

Output: head -> 2 -> 3 -> 4 -> 5 -> 1

Explanation:

List after 1 shift to right: head -> 5 -> 1 -> 2 -> 3 -> 4.

List after 2 shift to right: head -> 4 -> 5 -> 1 -> 2 -> 3.

List after 3 shift to right: head -> 3 -> 4 -> 5 -> 1 -> 2.

List after 4 shift to right: head -> 2 -> 3 -> 4 -> 5 -> 1.

Input: head -> 1 -> 2 -> 3 -> 4 -> 5, k = 7

Output:
head -> 4 -> 5 -> 1 -> 2 -> 3
Constraints:
0 <= number of nodes in the linked list <= 105
-104 <= ListNode.val <= 104
0 <= k <= 5 * 105
k may have values greater than number of nodes in the linked list.

#Brute Force
#Intuition
For each k step, move the last element of a linked list to the front. This shifts all elements from one position to the right, with the last element wrapping around to become the first.
Approach
Move the last element to first for each k.
For each k, find the last element from the list. Move it to the first.

# Definition of Single Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to rotate the list by k steps
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Base case: if list is empty or has only one node
        if not head or not head.next:
            return head

        # Perform rotation k times
        for _ in range(k):
            temp = head
            # Find the second last node
            while temp.next.next:
                temp = temp.next
            # Get the last node
            end = temp.next
            # Break the link between 
            # second last and last node
            temp.next = None
            # Make the last node 
            # as new head
            end.next = head
            head = end

        return head

# Utility function to insert node at end of list
def insert_node(head, val):
    new_node = ListNode(val)
    if not head:
        return new_node
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head

# Utility function to print list
def print_list(head):
    while head:
        print(head.val, end="->" if head.next else "")
        head = head.next
    print()

if __name__ == "__main__":
    head = ListNode(1)
    # Inserting nodes
    head = insert_node(head, 2)
    head = insert_node(head, 3)
    head = insert_node(head, 4)
    head = insert_node(head, 5)

    print("Original list: ", end="")
    print_list(head)

    k = 2
    solution = Solution()
    # Calling function for rotating right by k times
    new_head = solution.rotateRight(head, k)

    print(f"After {k} iterations: ", end="")
    # List after rotating nodes
    print_list(new_head)

Complexity Analysis
Time Complexity: O(NxK) because for K times, we are iterating through the entire list to get the last element and move it to the first position. Here, N represents the number of nodes in the linked list, and K is the number of steps by which the list has to be rotated.

Space Complexity: O(1) because no extra data structure is required for computation.

#Optimal Solution
Intuition
For every k that is a multiple of the length of the list, the linked list returns to its original state after rotation. By using brute force with k as a multiple of the list's length, we notice this pattern. This insight suggests that for k greater than the length of the list, we only need to rotate the list by k % length of the list, thus optimizing our time complexity.
Approach
Calculate the length of the list.
Connect the last node to the first node, converting it to a circular linked list.
Iterate to cut the link of the last node and start a node of k%length of the list rotated list.

# Definition of Single Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to rotate the list by k steps
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head

        # Calculating length
        temp = head
        length = 1
        while temp.next:
            length += 1
            temp = temp.next

        # Link last node to first node
        temp.next = head
        # When k is more than length of list
        k = k % length
        # To get end of the list
        end = length - k
        while end > 0:
            temp = temp.next
            end -= 1

        # Breaking last node link and pointing to NULL
        head = temp.next
        temp.next = None

        return head

# Utility function to insert node at end of list
def insert_node(head, val):
    new_node = ListNode(val)
    if not head:
        return new_node
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head

# Utility function to print list
def print_list(head):
    while head:
        print(head.val, end="->" if head.next else "")
        head = head.next
    print()

if __name__ == "__main__":
    head = ListNode(1)
    # Inserting nodes
    head = insert_node(head, 2)
    head = insert_node(head, 3)
    head = insert_node(head, 4)
    head = insert_node(head, 5)

    print("Original list: ", end="")
    print_list(head)

    k = 2
    solution = Solution()
    # Calling function for rotating right by k times
    new_head = solution.rotateRight(head, k)

    print(f"After {k} iterations: ", end="")
    # List after rotating nodes
    print_list(new_head)

Complexity Analysis
Time Complexity: O(N) + O(N - (N % k)) because O(N) is for calculating the length of the list, and O(N - (N % k)) is for breaking the link and pointing to NULL. Here N is the length of the linked list and K is the number of iterations required. Space Complexity: O(1) because no extra data structure is required for computation.

'''
# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        temp = head
        length = 1
        while temp.next:
            length += 1
            temp = temp.next
        temp.next = head
        k = k % length
        end = length - k
        while end > 0:
            temp = temp.next
            end -= 1
        head = temp.next
        temp.next = None

        return head