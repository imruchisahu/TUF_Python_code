'''
Given the head of a singly Linked List, return the middle node of the Linked List.



If the Linked List has an even number of nodes, return the second middle one.


Examples:
Input: head -> 3 -> 8 -> 7 -> 1 -> 3

Output(value at returned node): 7

Explanation: There are 5 nodes, so the middle node is the 3rd Node, with value 7.

Input: head -> 2 -> 9 -> 1 -> 4 -> 0 -> 4

Output(value at returned node): 4

Explanation: There are 6 nodes, thus both the 3rd and 4th nodes are middle. So the 2nd middle node (4th Node) is returned with value 4.

Input: head -> 3 -> 8 -> 1 -> 7 -> 0

Output:
1
Constraints:
1 <= number of Nodes in the Linked List <= 105

-104 <= ListNode.val <= 104
#Brute

Intuition:
A naive approach to solve this problem is to count the number of nodes in the linked list and then traverse the list again to find the middle element. If the linked list contains N number of nodes, then the middle node will be at the position: floor(N/2) + 1.

Note that in case of even number of nodes in the linked list, there will be two middle nodes and we need to return the second middle node.

Approach:
The linked list is traversed once to determine its total length.
The middle position is calculated as N/2 + 1.
The linked list is traversed again up to the middle position.
The node at this position is returned as the middle node.

# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to get the middle node of linked list
    def middleOfLinkedList(self, head):
        temp = head
        count = 0
        
        # Traverse the linked list
        while temp is not None:
            count += 1  # Increment the count by one 
            temp = temp.next
        
        mid_position = (count) // 2 + 1
        
        middle_node = head
        for _ in range(1, mid_position):
            middle_node = middle_node.next
        
        return middle_node

# Utility Function to print the linked list
def printLinkedList(head):
    temp = head
    
    # Traverse the linked list and print each node's value
    while temp is not None:
        print(temp.val, end=" ")
        temp = temp.next
    print()

if __name__ == "__main__":
    # Creating a simple linked list
    head = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)
    fifth = ListNode(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    
    # Creating an object of Solution class
    sol = Solution()
    
    # Function call to get the middle node of linked list 
    middle_node = sol.middleOfLinkedList(head)
    
    printLinkedList(head)
    print("The middle node is:", middle_node.val)

Complexity Analysis:
Time Complexity: O(N), where N is the number of nodes in the linked list.
Firstly the size of the linked list is determined which takes O(N) time. Then traversing to the middle nodes takes another O(N/2) time. Thus the overall time complexity is O(N) + O(N/2) or O(3N/2) or O(N).

Space Complexity: O(1), as only a couple of variables are used.

#Optimal
Intuition:
An optimal approach to solve this problem involves the use of two pointer technique using the slow and fast pointers. The slow pointer moves one step at a time while the fast pointer moves two steps at a time. If the fast pointer reaches the end of the list, the slow pointer will be at the middle of the list.

This is because the fast pointer moves twice as fast as the slow pointer, so when the fast pointer reaches the end of the list, the slow pointer will be at the middle of the list.

Approach:
One pointer moves one step at a time, while the other moves two steps at a time.
The faster pointer moves twice as fast as the slower pointer.
When the faster pointer reaches the end, the slower pointer is at the middle node.
The node where the slower pointer stops is returned as the middle node.

# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to get the middle node of linked list
    def middleOfLinkedList(self, head):
        slow = head
        fast = head
        
        # Until the fast pointer reaches None or the last node
        while fast is not None and fast.next is not None:
            # Move slow pointer by one step
            slow = slow.next
            
            # Move fast pointer by two steps
            fast = fast.next.next
        
        return slow

# Utility Function to print the linked list
def printLinkedList(head):
    temp = head
    
    # Traverse the linked list and print each node's value
    while temp is not None:
        print(temp.val, end=" ")
        temp = temp.next
    print()

if __name__ == "__main__":
    # Creating a simple linked list
    head = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)
    fifth = ListNode(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    
    # Creating an object of Solution class
    sol = Solution()
    
    # Function call to get the middle node of linked list 
    middle_node = sol.middleOfLinkedList(head)
    
    printLinkedList(head)
    print("The middle node is:", middle_node.val)

Complexity Analysis:
Time Complexity: O(N/2), where N is the number of nodes in the linked list.
The total iterations taken by the fast pointer to reach the end of the linked list are of the order O(N/2).

Space Complexity: O(1), as only a couple of variables are used.
'''
# Definition for Singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleOfLinkedList(self, head):
        slow=head
        fast= head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow
