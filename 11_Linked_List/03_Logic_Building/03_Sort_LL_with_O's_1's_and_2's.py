'''
Given the head of a singly linked list consisting of only 0, 1 or 2. Sort the given linked list and return the head of the modified list. Do it in-place by changing the links between the nodes without creating new nodes.


Examples:
Input: head -> 1 -> 0 -> 2 -> 0 -> 1

Output: head -> 0 -> 0 -> 1 -> 1 -> 2

Explanation: The values after sorting are [0, 0, 1, 1, 2].

Input: head -> 1 -> 1 -> 1 -> 0

Output: head -> 0 -> 1 -> 1 -> 1

Explanation: The values after sorting are [0, 1, 1, 1].

Input: head -> 2 -> 2 -> 1 -> 2

Output:
head -> 1 -> 2 -> 2 -> 2
Constraints:
0 <= number of nodes in the Linked List <= 105
0 <= ListNode.val <= 2

#brute 

Intuition
Since there are only 3 distinct values in the linked list, it's straightforward to count the occurrences of 0s, 1s, and 2s. After counting, we can overwrite the linked list nodes based on these frequencies.
Approach
Take 3 variables to maintain the count of 0, 1, and 2.
Traverse the linked list to count the occurrences of each value.
In the second traversal of the linked list, overwrite the first 'a' nodes with '0', the next 'b' nodes with '1', and the remaining 'c' nodes with '2' based on the counts.
# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to sort the linked list
    def sortList(self, head):
        # Initialize counts
        c0 = 0
        c1 = 0
        c2 = 0
        temp = head

        # Count the number of 0s,
        # 1s, and 2s
        while temp is not None:
            if temp.val == 0:
                c0 += 1
            elif temp.val == 1:
                c1 += 1
            elif temp.val == 2:
                c2 += 1
            temp = temp.next

        temp = head

        # Reassign values to the
        # nodes based on the counts
        while temp is not None:
            if c0 > 0:
                temp.val = 0
                c0 -= 1
            elif c1 > 0:
                temp.val = 1
                c1 -= 1
            elif c2 > 0:
                temp.val = 2
                c2 -= 1
            temp = temp.next

        return head

# Function to print linked list
def printList(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()

# Function to create new node
def newNode(data):
    return ListNode(data)

if __name__ == "__main__":
    # Creating a linked list
    head = newNode(1)
    head.next = newNode(2)
    head.next.next = newNode(0)
    head.next.next.next = newNode(1)
    head.next.next.next.next = newNode(2)
    head.next.next.next.next.next = newNode(0)
    head.next.next.next.next.next.next = newNode(1)

    # Print original list
    print("Original list: ", end="")
    printList(head)

    # Sort the list
    sol = Solution()
    head = sol.sortList(head)

    # Print sorted list
    print("Sorted list: ", end="")
    printList(head)


Complexity Analysis
Time Complexity: O(2N) because the code traverses the linked list twice: once while counting the frequency of 0's, 1's, and 2's, and once again while reassigning the values to the nodes. Here, N represents the length of the linked list or the number of nodes present in the linked list.
Space Complexity: O(1) because no extra space is used.

#optimal

Intuition
Traverse the linked list to segregate nodes into three separate lists based on their values (0s, 1s, and 2s), then link these lists together to form a single sorted linked list.
Approach
Create three dummy nodes to serve as the heads of three separate lists for 0s, 1s, and 2s. Also, create pointers to track the current end of each of these lists.
Traverse the original linked list. For each node, append it to the appropriate list (0s, 1s, or 2s) based on its value and update the corresponding pointer.
Connect the three lists together. Link the end of the 0s list to the start of the 1s list (or directly to the 2s list if the 1s list is empty). Then, link the end of the 1s list to the start of the 2s list.
The new head of the sorted linked list will be the node following the dummy node for 0s.
Return the new head of the sorted linked list. This completes the process and results in a sorted linked list.

# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to sort the linked list
    def sortList(self, head):
    #If the list is empty or has only one node, return as it is already sorted
        if head is None or head.next is None:
            return head

        # Dummy nodes to point to heads of 
        # three lists
        zeroHead = ListNode(-1)
        oneHead = ListNode(-1)
        twoHead = ListNode(-1)

        # Pointers to current last nodes of 
        # three lists
        zero = zeroHead
        one = oneHead
        two = twoHead
        temp = head

    #Traverse the original list and distribute the nodes into three lists
        while temp is not None:
            if temp.val == 0:
                zero.next = temp
                zero = temp
            elif temp.val == 1:
                one.next = temp
                one = temp
            elif temp.val == 2:
                two.next = temp
                two = temp
            temp = temp.next

        # Connect the three lists together
        zero.next = oneHead.next if oneHead.next else twoHead.next
        one.next = twoHead.next
        two.next = None

        # New head of the sorted list
        newHead = zeroHead.next

        # Return the new head
        return newHead

# Helper function to print linked list
def printList(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()

# Helper function to create a new node
def newNode(data):
    return ListNode(data)

if __name__ == "__main__":
    # Creating a linked list
    head = newNode(1)
    head.next = newNode(2)
    head.next.next = newNode(0)
    head.next.next.next = newNode(1)
    head.next.next.next.next = newNode(2)
    head.next.next.next.next.next = newNode(0)
    head.next.next.next.next.next.next = newNode(1)

    # Print original list
    print("Original list: ", end="")
    printList(head)

    # Sort the list
    sol = Solution()
    head = sol.sortList(head)

    # Print sorted list
    print("Sorted list: ", end="")
    printList(head)

Complexity Analysis
Time Complexity: O(N) because the code traverses the linked list once. Here, N represents the length of the linked list or the number of nodes present in the linked list.
Space Complexity: O(1) because no extra space is used and we just change the links of the nodes.

'''
# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        if head is None or head.next is None:
            return head

        # Dummy nodes to point to heads of 
        # three lists
        zeroHead = ListNode(-1)
        oneHead = ListNode(-1)
        twoHead = ListNode(-1)
        zero = zeroHead
        one = oneHead
        two = twoHead
        temp = head


        while temp is not None:
            if temp.val == 0:
                zero.next = temp
                zero = temp
            elif temp.val == 1:
                one.next = temp
                one = temp
            elif temp.val == 2:
                two.next = temp
                two = temp
            temp = temp.next

        zero.next = oneHead.next if oneHead.next else twoHead.next
        one.next = twoHead.next
        two.next = None
        newHead = zeroHead.next
        return newHead