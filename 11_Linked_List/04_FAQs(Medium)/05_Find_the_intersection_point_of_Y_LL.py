'''
Given the heads of two linked lists A and B, containing positive integers. Find the node at which the two linked lists intersect. If they do intersect, return the node at which the intersection begins, otherwise return null.



The Linked List will not contain any cycles. The linked lists must retain their original structure, given as per the input, after the function returns.



Note: for custom input, the following parameters are required(your program is not provided with these parameters):

intersectVal - The value of the node where the intersection occurs. This is -1 if there is no intersected node.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node(-1 if no intersection).
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node(-1 if no intersection).
listA - The first linked list.
listB - The second linked list.

Examples:
Input: listA: intersectVal = 4, skipA = 3, skipB = 2, head -> 1 -> 2 -> 3 -> 4 -> 5, listB: head -> 7 -> 8 -> 4 -> 5



Output(value at returned node is displayed): 4

Explanation: The two lists have nodes with values 4 and 5 as their tails.

Input: listA: intersectVal = -1, skipA = -1, skipB = -1, head -> 1 -> 2 -> 3, listB: head -> 8 -> 9



Output(value at returned node is displayed): null

Explanation: The two lists do not intersect.

Input: listA: intersectVal = 4, skipA = 0, skipB = 0, head -> 4 -> 5 -> 6, listB: head -> 4 -> 5 -> 6



Output:
4
Constraints:
m == number of nodes in listA.
n == number of nodes in listB.
1 <= m, n <= 5 * 104
0 <= ListNode.val <= 104
0 <= skipA < m
0 <= skipB < n
intersectVal, skipA, skipB is -1 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

#Brute
Intuition:
To find where two linked lists intersect, we can use a hash set to remember all the nodes from the first list. Then, as we go through the second list, we check if any node is already in the hash set. The first node that is found in the set is where the lists intersect.

Approach:
A hash map is used which provides an efficient way to search in constant time, O(1). The steps are as follows:

Hashing List 1 Nodes:
Traverse through the first linked list and hash the addresses of its nodes. This allows us to store each node's address in a hash set, providing a quick way to reference these nodes later.

Searching in List 2: Traverse through the second linked list and check if any node's address is already present in the hash set. If a node from the second list is found in the hash set, it means that this node is the intersection point, and we return it. This efficiently identifies the intersection without the need for nested iterations.

# Definition of singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to find the intersection node of two linked lists
    def getIntersectionNode(self, headA, headB):
        # Create a hash set to store the nodes
        # Of the first list
        nodes_set = set()

        # Traverse the first linked list
        # And add all its nodes to the set
        while headA is not None:
            nodes_set.add(headA)
            headA = headA.next

        # Traverse the second linked list
        # And check for intersection
        while headB is not None:
            # If a node from the second list is found in the set,
            # It means there is an intersection
            if headB in nodes_set:
                return headB
            headB = headB.next

        # No intersection found, return None
        return None

# Utility function to insert a node at the end of the linked list
def insertNode(head, val):
    # Create a new node with the given value
    newNode = ListNode(val)
    
    # If the list is empty, set the new node as the head
    if head is None:
        head = newNode
        return head
    
    # Otherwise, traverse to the end of the list
    temp = head
    while temp.next is not None:
        temp = temp.next
    
    # Insert the new node at the end of the list
    temp.next = newNode
    return head

# Utility function to print the linked list
def printList(head):
    # Traverse the list
    while head.next is not None:
        # Print the value of each node followed by an arrow
        print(head.val, end="->")
        head = head.next
    # Print the value of the last node
    print(head.val)

if __name__ == "__main__":
    # Creation of the first list
    head1 = ListNode()
    head1 = insertNode(head1, 1)
    head1 = insertNode(head1, 3)
    head1 = insertNode(head1, 1)
    head1 = insertNode(head1, 2)
    head1 = insertNode(head1, 4)

    # Create an intersection
    intersection = head1.next.next.next

    # Creation of the second list
    head2 = ListNode()
    head2 = insertNode(head2, 3)
    head2.next = intersection

    # Printing the lists
    print("List1: ", end="")
    printList(head1)
    print("List2: ", end="")
    printList(head2)

    # Checking if an intersection is present
    sol = Solution()
    answerNode = sol.getIntersectionNode(head1, head2)
    if answerNode is None:
        print("No intersection")
    else:
        print("The intersection point is", answerNode.val)

        
Complexity Analysis:
Time Complexity: O(N + M), where N and M are the lengths of the first and second linked list respectively.

Traversing the first list and adding the nodes to the hashset takes O(N) time assuming the hashset takes O(1) time for operations. Iterating through all nodes in the second list takes O(M) time. Therefore, the total time complexity is O(N + M).
Note: If the hashset takes logarithmic time for operations, the time complexity get a multiple of logN.

Space Complexity: O(N)
Using an hashset to store the addresses of all nodes in the first list takes O(N) space.


#Better
Intuition:
To find the intersection of two linked lists, we use the difference in their lengths to align their starting points and then traverse both lists simultaneously until we find the intersection node.

Approach:
Calculate the lengths of both linked lists.
Determine the positive difference between these lengths.
Advance the pointer of the longer list by this difference, thereby aligning both lists to the same remaining length.
Traverse both lists simultaneously from these aligned points. The first node where the pointers meet is the intersection node.

# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        temp1 = headA
        temp2 = headB
        n1, n2 = 0, 0

        # Get the length of first linked list
        while temp1:
            n1 += 1
            temp1 = temp1.next

        # Get the length of second linked list
        while temp2:
            n2 += 1
            temp2 = temp2.next

        # Traverse the longer list and bring the pointers to same level
        if n1 < n2:
            return self.collisionPoint(headA, headB, n2 - n1)

        return self.collisionPoint(headB, headA, n1 - n2)

    def collisionPoint(self, smallerListHead, longerListHead, lengthDiff):
        temp1, temp2 = smallerListHead, longerListHead

        # Adjust the pointers to same level
        for _ in range(lengthDiff):
            temp2 = temp2.next

        while temp1 != temp2:
            temp1 = temp1.next
            temp2 = temp2.next

        return temp1

# Utility function to insert a node at the end of the linked list
def insertNode(head, val):
    newNode = ListNode(val)
    if head is None:
        return newNode
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = newNode
    return head

# Utility function to print the linked list
def printList(head):
    while head.next:
        print(head.val, end="->")
        head = head.next
    print(head.val)

if __name__ == "__main__":
    # Creation of the first list
    head1 = None
    head1 = insertNode(head1, 1)
    head1 = insertNode(head1, 3)
    head1 = insertNode(head1, 1)
    head1 = insertNode(head1, 2)
    head1 = insertNode(head1, 4)

    # Create an intersection
    intersection = head1.next.next.next

    # Creation of the second list
    head2 = None
    head2 = insertNode(head2, 3)
    head2.next = intersection

    # Printing the lists
    print("List1: ", end="")
    printList(head1)
    print("List2: ", end="")
    printList(head2)

    # Checking if an intersection is present
    sol = Solution()
    answerNode = sol.getIntersectionNode(head1, head2)
    if answerNode is None:
        print("No intersection")
    else:
        print("The intersection point is", answerNode.val)

Complexity Analysis:
Time Complexity: O(N + M), where N and M are the lengths of first and second linked list respectively.

Calculating the lengths of the two linked list takes O(N) and O(M) time. Another O(|N-M|) time is needed for aligning the nodes. The final traversal of the aligned lists takes O(min(N,M)) time in the worst case. Thus, the overall time complexity is O(N + 2M) or O(N + M).

Space Complexity: O(1), because only a couple of pointers are used.

#Optimal
Intuition:
The simple intuition behind the optimal approach is to use two pointers to traverse the lists and traverse the same total distance by the time the pointers reach the intersection node. If one list ends, the pointer is placed at the front of the other list. The two pointers will meet at the intersection node if the lists have an intersection, otherwise, they will reach the end of the lists at the same time.

Edge Cases:
These are the edge cases that must be taken care of while implementing the optimal approach:
There is no intersection between the two linked lists.
The two linked lists intersect at the head.
Either of the two linked lists is empty.
Approach:
If either of the two linked lists is empty, there is no intersection, so return NULL.
Start one pointer at the head of the first linked list and another at the head of the second linked list.
Move each pointer one step at a time.
When a pointer reaches the end of its list, it is reassigned to the head of the other list. This ensures both pointers traverse the same total distance.
If the pointers meet, return the intersection node. If both pointers reach NULL, return NULL (no intersection).

# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to find the intersection node of two linked lists
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Edge case
        if headA is None or headB is None:
            return None

        # Initialize two pointers to traverse the lists
        d1, d2 = headA, headB

        # Traverse both lists until the pointers meet
        while d1 != d2:
            # Move both the pointers by one place
            d1 = d1.next
            d2 = d2.next

            # If intersection is found
            if d1 == d2:
                return d1

            # If either of the two pointers reaches end, place at the front of next linked list 
            if d1 is None:
                d1 = headB
            if d2 is None:
                d2 = headA

        # Return the intersection node
        return d1

# Utility function to insert a node at the end of the linked list
def insertNode(head, val):
    newNode = ListNode(val)
    if head is None:
        return newNode
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = newNode
    return head

# Utility function to print the linked list
def printList(head):
    temp = head
    while temp:
        print(temp.val, end="->" if temp.next else "")
        temp = temp.next
    print()

if __name__ == "__main__":
    # Creation of the first list
    head1 = None
    head1 = insertNode(head1, 1)
    head1 = insertNode(head1, 3)
    head1 = insertNode(head1, 1)
    head1 = insertNode(head1, 2)
    head1 = insertNode(head1, 4)

    # Create an intersection
    intersection = head1.next.next.next

    # Creation of the second list
    head2 = None
    head2 = insertNode(head2, 3)
    head2.next = intersection

    # Printing the lists
    print("List1: ", end="")
    printList(head1)
    print("List2: ", end="")
    printList(head2)

    # Checking if an intersection is present
    sol = Solution()
    answerNode = sol.getIntersectionNode(head1, head2)
    if answerNode is None:
        print("No intersection")
    else:
        print("The intersection point is", answerNode.val)

Complexity Analysis:
Time Complexity: O(N + M), where N and M are the lengths of first and second linked list respectively.

In the worst case (when the last node in a linked list is the intersection node), both the pointers will traverse the total length of the two linked lists before meeting at the intersection node. Hence, the time complexity is O(N + M).


Space Complexity: O(1), as no extra space was used.

'''

# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        # Initialize two pointers to traverse the lists
        d1, d2 = headA, headB

        # Traverse both lists until the pointers meet
        while d1 != d2:
            # Move both the pointers by one place
            d1 = d1.next
            d2 = d2.next

            # If intersection is found
            if d1 == d2:
                return d1

            # If either of the two pointers reaches end, place at the front of next linked list 
            if d1 is None:
                d1 = headB
            if d2 is None:
                d2 = headA

        # Return the intersection node
        return d1
