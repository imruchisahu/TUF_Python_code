'''Given an array nums, convert it into a doubly linked list and return the head of the list.


Examples:
Input: nums = [1, 2, 3, 4]

Output: head -> 1 <-> 2 <-> 3 <-> 4

Input: nums = [7, 7]

Output: head -> 7 <-> 7

Input: nums = [3]

Output:
head -> 3
Constraints:
n == nums.length
0 <= n <= 100
0 <= nums[i] <= 100
Intuition:
Begin the conversion of an array to a doubly linked list by creating the head node of the list. Then, iterate over each array element, constructing a new node for each element encountered. As each new node is created, link its next pointer to the subsequent node in the list, and link its back pointer to the preceding node. Upon completion, the head of the doubly linked list can be returned as the final result.
Approach:
Begin by creating the head of the doubly linked list (DLL) using the first element of the array. Set both the previous and next pointers of this node to NULL, as it is the first node in the list.
Iterate over the array starting from the second element, i.e., from index 1 to the last element of the array.
For each element in the array, create a new node with the current value from the array. Set the backward link of this new node to point to the node created in the previous step, establishing a connection to the previous node.
Update the forward link of the node from the previous iteration to connect it to the newly created node, establishing a forward connection.
Shift the reference of the previous node to the newly created node, which will serve as the previous node for the next iteration.
Repeat this process for each element in the array. Once the iteration is complete, the head node represents the start of the doubly linked list and can be returned as the final result.

# Definition of doubly linked list
class ListNode:
    def __init__(self, data1=0, next1=None, prev1=None):
        self.val = data1
        self.next = next1
        self.prev = prev1

# Solution class
class Solution:
    # Function to convert an array to a doubly linked list
    def arrayToLinkedList(self, nums):
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

# Helper function to print the linked list
def printLL(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]

    # Create an instance of Solution class
    sol = Solution()

    # Function call to convert an array to a doubly linked list
    head = sol.arrayToLinkedList(nums)

    # Print the doubly linked list
    print("The doubly linked list is: ")
    printLL(head)
Complexity Analysis:
Time Complexity: O(N) where N is the length of the array. The code iterates over the array once creating a new node for each element.

Space Complexity: O(N) The space complexity depends on the memory used to store doubly linked list nodes. Each node, storing data and two pointers ('next' and 'back'), requires constant space. Thus, space complexity is O(N) as it scales linearly with the array's size.

'''
# Definition of doubly linked list:
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def arrayToLinkedList(self, nums):
        if not nums:
            return None

        head = ListNode(nums[0])
        prev= head

        for i in range(1, len(nums)):
            temp = ListNode(nums[i], None, prev)
            prev.next = temp
            prev = temp
        return head