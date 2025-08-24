'''Given the head of a doubly linked list and two integers X and K, insert a new node with value X, before the Kth node of the linked list and return the head of the modified linked list.


Examples:
Input: head -> 1 <-> 3 <-> 5, X = 7, K = 2

Output: head -> 1 <-> 7 <-> 3 <-> 5

Explanation: A node with value 7 was added before the 2nd node.

Input: head -> 5, X = 7, K = 1

Output: head -> 7 <-> 5

Explanation: A node with value 7 was added, note that the head was changed.

Input: head -> 4 <-> 5, X = 10, K = 2

Output:
head -> 4 <-> 10 <-> 5
Constraints:
n == Number of nodes in the linked list
1 <= n <= 100
0 <= ListNode.val <= 100
0 <= X <= 100
1 <= K <= n

Intuition:
Inserting a node in front of the Kth node in a doubly linked list involves first locating the Kth node by counting up to the Kth position. Then, adjust the pointers of the adjacent nodes to insert the new node before the Kth node.
Approach:
Traverse the doubly linked list until reaching the Kth node, keeping a count. When the count reaches K, stop the traversal. Use a temporary pointer to mark the Kth node.
Identify the node before the Kth node and prepare a new node with the required data, setting its previous and next pointers to the appropriate nodes.
Update the next pointer of the node before the Kth node to point to the new node, and update the back pointer of the Kth node to point to the new node.

# Definition of doubly linked list
class ListNode:
    def __init__(self, data1=0, next1=None, prev1=None):
        self.val = data1
        self.next = next1
        self.prev = prev1

# Solution class
class Solution:
    #Function to insert a node before the Kth node in a doubly linked list 
    def insertBeforeKthPosition(self, head, X, K):
        # If node has to be inserted before the head
        if K == 1:
            newHead = ListNode(X, head, None)
            head.prev = newHead
            return newHead

        # Temporary pointer
        temp = head

        # Reach Kth node
        count = 0
        while temp is not None:
            count += 1

            # If Kth node is reached, Break out of the loop
            if count == K:
                break

            # Otherwise Keep moving temp forward
            temp = temp.next

        # Track the node
        prev = temp.prev

        # Create new node with data as X
        newNode = ListNode(X, temp, prev)

        # Join new node
        prev.next = newNode
        temp.prev = newNode

        # Return head
        return head

# Helper Function to convert an array to a doubly linked list
def arrayToLinkedList(nums):
    # If array is empty, return None
    if not nums:
        return None

    # Create head node with first element of the array
    head = ListNode(nums[0])
    # Initialize 'prev' to the head node
    prev = head

    for i in range(1, len(nums)):
        # Create a new node
        temp = ListNode(nums[i], None, prev)
        # Update 'next' pointer
        prev.next = temp
        # Move 'prev' to newly created node
        prev = temp

    # Return head
    return head

# Helper Function to print the linked list
def printLL(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()

if __name__ == "__main__":
    nums = [1, 2, 3, 5]

    # Creating the doubly linked list from given array
    head = arrayToLinkedList(nums)

    # Print the Original list
    print("Original List: ", end="")
    printLL(head)

    # Create an instance of Solution class
    sol = Solution()

    #Function call to insert a node before the Kth node in a doubly linked list 
    head = sol.insertBeforeKthPosition(head, 4, 4)

    # Print the Modified list
    print("Modified list: ", end="")
    printLL(head)
Complexity Analysis:
Time Complexity: O(N), where N is the number of nodes in the Linked List. In the worst case, it involves traversing N nodes in the Doubly Linked List to reach the last element. In the best case, when K is 0 (insertion at the head), the time complexity is O(1) as it involves a constant number of operations. In the average case, it's O(K).

Space Complexity: O(1) as no extra space is used.
'''
# Definition of doubly linked list:
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def insertBeforeKthPosition(self, head, X, K):
        if K == 1:
            newHead = ListNode(X, head, None)
            head.prev = newHead
            return newHead

        # Temporary pointer
        temp = head

        # Reach Kth node
        count = 0
        while temp is not None:
            count += 1

            # If Kth node is reached, Break out of the loop
            if count == K:
                break

            # Otherwise Keep moving temp forward
            temp = temp.next

        # Track the node
        prev = temp.prev

        # Create new node with data as X
        newNode = ListNode(X, temp, prev)

        # Join new node
        prev.next = newNode
        temp.prev = newNode

        # Return head
        return head