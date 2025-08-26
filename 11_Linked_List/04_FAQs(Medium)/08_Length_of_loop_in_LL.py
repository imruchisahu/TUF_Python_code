'''

Given the head of a singly linked list, find the length of the loop in the linked list if it exists. Return the length of the loop if it exists; otherwise, return 0.



A loop exists in a linked list if some node in the list can be reached again by continuously following the next pointer. Internally, pos is used to denote the index (0-based) of the node from where the loop starts.



Note that pos is not passed as a parameter.


Examples:


Input: head -> 1 -> 2 -> 3 -> 4 -> 5, pos = 1

Output: 4

Explanation: 2 -> 3 -> 4 -> 5 - >2, length of loop = 4.



Input: head -> 1 -> 3 -> 7 -> 4, pos = -1

Output: 0

Explanation: No loop is present in the linked list.





Input: head -> 6 -> 3 -> 7, pos = 0

Output:
3
Constraints:
0 <= number of nodes in the cycle <= 105
0 <= ListNode.val <= 104
pos is -1 or a valid index in the linked list

#Brute
Intuition
First, detect the loop in the linked list, then count the nodes within the loop to determine its length.
Approach
While traversing the linked list, use a timer to count the number of nodes visited. Assign each node a timer value when it is first encountered. If you visit a node that has already been encountered, you can determine the length of the loop by subtracting the timer value from when the node was first visited from the current timer value. This requires keeping track of each node and its associated timer value, which can be done using a hashmap where nodes are the keys and their timer values are the values.


Below is the algorithm for the approach
Start at the head of the linked list and use a temporary pointer to traverse the list. Move through each node until you reach the end (null). During traversal, store each visited node along with a timer value in a hashmap to track the nodes and their visit times.
As you continue traversing, if you encounter a node that is already in the hashmap, a loop is detected. The length of the loop is determined by subtracting the timer value of the first visit from the current timer value.
If the traversal completes and you reach null, it indicates that there is no loop in the linked list. In this case, return 0 to signify no loop found.

# Definition of singly linked list:
 class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
         self.next = next

class Solution:
    def findLengthOfLoop(self, head):
        # Dictionary to store visited nodes and their timer values
        visited_nodes = {}

        # Initialize pointer to traverse the linked list
        temp = head

        # Initialize timer 
        # to track visited nodes
        timer = 0

        # Traverse the linked list 
        # till temp reaches None
        while temp is not None:
            # If revisiting a node return difference of timer values
            if temp in visited_nodes:
                # Calculate the length of the loop
                loop_length = timer - visited_nodes[temp]

                # Return length of loop
                return loop_length
            # Store the current node 
            # and its timer value in 
            # the dictionary
            visited_nodes[temp] = timer

            # Move to the next node
            temp = temp.next

            # Increment the timer
            timer += 1

        # If traversal is completed 
        # and we reach the end 
        # of the list (None)
        # means there is no loop
        return 0

# Sample linked list with a loop
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)
fifth = ListNode(5)

# Create a loop from fifth to second
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = second

solution = Solution()
loop_length = solution.findLengthOfLoop(head)
if loop_length > 0:
    print("Length of the loop:", loop_length)
else:
    print("No loop found in the linked list.")

Complexity Analysis
Time Complexity: O(N) because the code traverses the entire linked list at least once, where 'N' is the number of nodes in the list.

Space Complexity: O(N) because the code uses a hashmap/dictionary to store encountered nodes, which can take up to O(N) additional space, where 'N' is the number of nodes in the list. Hence, the space complexity is O(N) due to the use of the map to track nodes.


#optimal
Intuition
The brute force method uses O(N) additional memory. To improve efficiency, the Tortoise and Hare approach is introduced as an optimized method because it detects loops using constant space. This approach uses two pointers moving at different speeds, ensuring that if a loop exists, they will meet within the loop, allowing detection without extra memory.
Approach
Begin with two pointers, slow and fast, both starting at the head of the linked list. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
Move slow one step and fast two steps at a time until fast or next of fast is null (indicating no loop) or slow meets fast (indicating a loop). If slow and fast meet, this confirms a loop.

Then, initialize a counter and move fast one step at a time while incrementing the counter. Continue until fast meets slow again; the counter value at this point represents the length of the loop.

# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to find the length of the loop
    def findLength(self, slow, fast):
        # Count to keep track of nodes encountered in loop
        cnt = 1
        
        # Move fast by one step
        fast = fast.next
        
        # Traverse fast till it reaches back to slow
        while slow != fast:
            """ At each node 
            increase count by 1
            move fast forward 
            by one step """
            cnt += 1
            fast = fast.next
        
        """ Loop terminates 
        when fast reaches slow again 
        and the count is returned"""
        return cnt

    # Function to find the length of the loop
    def findLengthOfLoop(self, head):
        slow = head
        fast = head

        # Traverse the list to detect a loop
        while fast is not None and fast.next is not None:
            # Move slow one step
            slow = slow.next
            # Move fast two steps
            fast = fast.next.next

            # If the slow and fast pointers meet
            # there is a loop
            if slow == fast:
                # return the number of nodes 
                return self.findLength(slow, fast)

        """ If the fast pointer 
        reaches the end, 
        there is no loop """
        return 0

# Create a sample linked list with a loop
head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)
fifth = ListNode(5)

# Create a loop from fifth to second
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = second

solution = Solution()
loopLength = solution.findLengthOfLoop(head)
if loopLength > 0:
    print("Length of the loop:", loopLength)
else:
    print("No loop found in the linked list.")

Complextiy Analysis
Time Complexity: O(N) because the code traverses the entire linked list once, where 'N' is the number of nodes in the list.

Space Complexity: O(1) because the code uses only a constant amount of additional space, regardless of the linked list's length. This is achieved by using two pointers (slow and fast) to detect the loop without any significant extra memory usage, resulting in constant space complexity, O(1).

'''
# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findLengthOfLoop(self, head):
        visited_nodes = {}
        temp = head
        timer = 0
        while temp is not None:
            if temp in visited_nodes:
                loop_length = timer - visited_nodes[temp]
                return loop_length
            visited_nodes[temp] = timer
            temp = temp.next
            timer += 1
        return 0