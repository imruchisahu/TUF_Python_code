'''
Given the head of a singly linked list, the task is to find the starting point of a loop in the linked list if it exists. Return the starting node if a loop exists; otherwise, return null.



A loop exists in a linked list if some node in the list can be reached again by continuously following the next pointer. Internally, pos denotes the index (0-based) of the node from where the loop starts.



Note that pos is not passed as a parameter.


Examples:


Input: head -> 1 -> 2 -> 3 -> 4 -> 5, pos = 1

Output(value of the returned node is displayed): 2

Expla﻿nation: The tail of the linked list connects to the node at 1st index.



Input: head -> 1 -> 3 -> 7 -> 4, pos = -1

Output(value of the returned node is displayed): null

Explanation: No loop is present in the linked list.



Input: head -> 6 -> 3 -> 7, pos = 0

Output:
6
Constraints:
0 <= number of nodes in the cycle <= 105
0 <= ListNode.val <= 104
pos is -1 or a valid index in the linked list

#Brute
Intuition
The starting point of a loop in a linked list is the first node that we encounter more than once while traversing the list. When we reach this node for the second time, it indicates that we have entered a cycle, meaning we are no longer progressing forward but instead moving in a circular path within the list. This node marks the beginning of the repeated sequence, where the loop begins.


Approach
Initialization: Start by creating a temporary pointer pointing to the head of the linked list and an empty hash map to keep track of visited nodes.

Note: Storing the entire node in the map is essential to distinguish between nodes with identical values but different positions in the list. This ensures accurate loop detection and not just duplicate value checks.

Traversal and Detection: Move through the linked list node by node using the temporary pointer. For each node, check if it is already in the hash map. If not, add it to the map and proceed to the next node. If a node is found in the hash map, it indicates the start of the loop and should be returned. If the pointer reaches the end of the list (null) without finding any repeated nodes, return null, indicating there is no loop.

# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findStartingPoint(self, head):
        # Use temp to traverse the linked list
        temp = head
        
        # Dictionary to store all visited nodes
        visited = {}
        
        # Traverse the list using temp
        while temp is not None:
            # Check if temp has been encountered again
            if temp in visited:
                # A loop is detected hence return temp
                return temp
            # Store temp as visited
            visited[temp] = True
            # Move to the next node
            temp = temp.next
        
        # If no loop is detected, return None
        return None

# Create a sample linked list with a loop
node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(3)
node2.next = node3
node4 = ListNode(4)
node3.next = node4
node5 = ListNode(5)
node4.next = node5

# Make a loop from node5 to node2
node5.next = node2

# Set the head of the linked list
head = node1

# Create an instance of the Solution class
solution = Solution()

# Detect the loop in the linked list
loopStartNode = solution.findStartingPoint(head)

if loopStartNode:
    print("Loop detected. Starting node of the loop is:", loopStartNode.val)
else:
    print("No loop detected in the linked list.")

Time Complexity: O(N) The algorithm goes through the entire linked list once, with 'N' representing the total number of nodes. As a result, the time complexity is linear, or O(N).

Space Complexity: O(N) The algorithm utilizes a hash map to store the nodes it encounters. This hash map can store up to 'N' nodes, where 'N' is the total number of nodes in the list. Therefore, the space complexity is O(N) because of the additional space used by the hash map.


#Optimal
Intuition
The previous method utilizes O(N) additional memory, which can be of concern when dealing with longer linked lists. To improve efficiency, we can use the Tortoise and Hare Algorithm, which is an optimized approach that reduces memory usage. This algorithm uses two pointers moving at different speeds to detect loops more efficiently.

Approach
Initialization: Initialize two pointers, slow and fast, to the head of the linked list. The slow pointer will advance one step at a time, while the fast pointer will advance two steps at a time. These pointers will move simultaneously through the list.

Traversal: As the traversal progresses, move the slow pointer one step and the fast pointer two steps at a time. This continues until one of two conditions is met: if fast or fast.next reaches the end of the linked list (i.e., becomes null), it means there is no loop in the linked list, and the algorithm terminates by returning null. Alternatively, if the fast and slow pointers meet at the same node, it indicates the presence of a loop in the linked list.

Finding the Loop's Start: Once a loop is detected, reset the slow pointer to the head of the linked list. Then, move both the fast and slow pointers one step at a time. The point where they meet again is identified as the starting point of the loop. This method ensures efficient detection and pinpointing of the loop's starting location in the linked list.


Proof of the Approach
You might wonder how this algorithm works, and it all comes down to the concept that the meeting point of the slow and fast pointers can be used to find the start of the loop.

In the "tortoise and hare" method for detecting loops in a linked list, when the slow pointer (tortoise) reaches the start of the loop, the fast pointer (hare) is at a position that is twice the distance traveled by the slow pointer. This happens because the hare moves twice as fast as the tortoise.

Image 1
Image 2

1/2


If the slow pointer has traveled a distance of L1, then the fast pointer has traveled 2 * L1. Now, both pointers are inside the loop, and the distance the fast pointer needs to cover to catch up with the slow pointer is the total length of the loop minus L1. Let's call this distance d.

Distance traveled by slow = L1
Distance traveled by fast = 2 * L1
Total length of loop = L1 + d
In this setup, the fast pointer moves two steps forward while the slow pointer moves one step forward in each iteration. This reduces the gap between them by one step each time. Given that the initial gap is d, it will take exactly d steps for the fast pointer to catch up with the slow pointer.

Total length of loop = L1 + d
Distance between slow and fast = d
During these d steps, the slow pointer will move d steps from the start of the loop, and the fast pointer will move 2 * d steps to meet the slow pointer. According to our calculations, the total length of the loop is L1 + d. Since the slow pointer covers a distance of d inside the loop, the remaining distance in the loop equals L1.

Thus, we can see that the distance from the start of the loop to the meeting point is equal to the distance from the start of the linked list to the start of the loop. This proves that the point where the two pointers meet is indeed the start of the loop in the linked list.

# Definition of singly linked list:
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def findStartingPoint(self, head):
        # Initialize a slow and fast 
        # pointers to the head of the list
        slow = head
        fast = head

        # Phase 1: Detect the loop
        while fast is not None and fast.next is not None:
            
            # Move slow one step
            slow = slow.next
            
            # Move fast two steps
            fast = fast.next.next

            # If slow and fast meet,
            # a loop is detected
            if slow == fast:
                
                # Reset the slow pointer
                # to the head of the list
                slow = head

                # Phase 2: Find the first node of the loop
                while slow != fast:
                    
                    # Move slow and fast one step
                    # at a time
                    slow = slow.next
                    fast = fast.next

                    # When slow and fast meet again,
                    # it's the first node of the loop
                return slow
        
        # If no loop is found, return None
        return None

# Function to create a sample linked list with a loop and detect the loop
if __name__ == "__main__":
    # Create a sample linked list with a loop
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(3)
    node2.next = node3
    node4 = ListNode(4)
    node3.next = node4
    node5 = ListNode(5)
    node4.next = node5

    # Make a loop from node5 to node2
    node5.next = node2

    # Set the head of the linked list
    head = node1

    # Detect the loop in the linked list
    sol = Solution()
    loop_start_node = sol.findStartingPoint(head)

    if loop_start_node:
        print(f"Loop detected. Starting node of the loop is: {loop_start_node.val}")
    else:
        print("No loop detected in the linked list.")

Time Complexity: O(N) The code examines each node in the linked list exactly once, where 'N' is the total number of nodes. This results in a linear time complexity, O(N), as the traversal through the list is direct and sequential.

Space Complexity: O(1) The code uses a fixed amount of extra space, regardless of the size of the linked list. This is accomplished by employing two pointers, slow and fast, to detect the loop. Since no additional data structures are used that depend on the size of the list, the space complexity remains constant, O(1).

'''
# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findStartingPoint(self, head):
        temp = head
        visited = {}
        while temp is not None:
            if temp in visited:
                return temp
            # Store temp as visited
            visited[temp] = True
            temp = temp.next
        return None