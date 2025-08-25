'''
Given the head of a singly linked list. Group all the nodes with odd indices followed by all the nodes with even indices and return the reordered list.



Consider the 1st node to have index 1 and so on. The relative order of the elements inside the odd and even group must remain the same as the given input.


Examples:
Input: head -> 1 -> 2 -> 3 -> 4 -> 5

Output: head -> 1 -> 3 -> 5 -> 2 -> 4

Explanation: The nodes with odd indices are 1, 3, 5 and the ones with even indices are 2, 4.

Input: head -> 4 -> 3 -> 2 -> 1

Output: head -> 4 -> 2 -> 3 -> 1

Explanation: The nodes with odd indices are 4, 2 and the ones with even indices are 3, 1.

Input: head -> 1

Output:
head -> 1
Constraints:
0 <= number of nodes in the Linked List <= 105
0 <= ListNode.val <= 104

#Brute Approach

Intuition
The simplest way to approach this problem is to traverse the linked list, gather the elements at odd and even indices into separate lists, and then create a new linked list from these lists.
Approach
Initialize a temporary pointer to the head of the linked list for traversal. Create a list to store the grouped odd-indexed and even-indexed elements. Traverse the linked list, adding the data from each odd-indexed node to the list, then reset the pointer to the second node and repeat the process for even-indexed nodes.
Traverse the linked list again, replacing each node’s value with the values stored in the list in order.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to segregate odd and even indices nodes
    def oddEvenList(self, head):
        # Check if list is empty or has only one node
        if not head or not head.next:
            return head

        # To store values
        array = []
        temp = head

        #Traverse the list, skipping one node, and store values in the vector
        while temp and temp.next:
            array.append(temp.val)
            temp = temp.next.next

        #If the traversal ends on a valid odd-indexed node, include its value as well
        if temp:
            array.append(temp.val)

        # Reset temp 
        temp = head.next

        #Traverse the list again, skipping one node , and store values in the vector
        while temp and temp.next:
            array.append(temp.val)
            temp = temp.next.next

        #If the traversal ends on a valid even-indexed node, include its value as well
        if temp:
            array.append(temp.val)

        # Reset temp 
        temp = head
        i = 0

        # Update node values 
        while temp:
            temp.val = array[i]
            temp = temp.next
            i += 1

        return head

# Function to print the linked list
def printLL(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# Main function
if __name__ == "__main__":
    # Create a linked list with given values
    arr = [1, 3, 4, 2, 5, 6]
    head = ListNode(arr[0])
    head.next = ListNode(arr[1])
    head.next.next = ListNode(arr[2])
    head.next.next.next = ListNode(arr[3])
    head.next.next.next.next = ListNode(arr[4])
    head.next.next.next.next.next = ListNode(arr[5])

    # Rearrange the list and print it
    solution = Solution()
    head = solution.oddEvenList(head)
    printLL(head)

Complexity Analysis
Time Complexity: O(2xN) for the following reasons:-
Traversing the odd-indexed elements takes O(N/2) time.
Traversing the even-indexed elements takes O(N/2) time.
Updating the linked list with the values from the array takes O(N) time.
Here N is the size of the linked list.

Space Complexity: O(N) because an additional list is used to store the grouped elements from the linked list.

#Optimal Approach
Intuition
The brute force approach utilizes additional space. To make it more effective, we can create links between all the odd-indexed and even-indexed elements while traversing the linked list and finally point the last odd-indexed element to the first even-indexed element to get the desired linked list without the help of an additional data structure.
Approach
Start by setting two pointers: one for the odd-indexed elements and one for the even-indexed elements. The odd pointer will start at the first node, and the even pointer will start at the second node. Also, keep track of the first even-indexed node.
Traverse the linked list, linking all the odd-indexed nodes together and all the even-indexed nodes together.
Depending on whether the list length is odd or even, ensure the traversal continues appropriately. For an even-length list, make sure the loop runs until the node after the even pointer is not NULL. For an odd-length list, make sure the loop runs until the even pointer itself is not NULL.
Once all nodes are grouped, link the last odd-indexed node to the first even-indexed node to form the desired linked list without using extra space.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to rearrange nodes
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

    #Initialize pointers for odd and even nodes and keep 
        track of the first even node
        odd = head
        even = head.next
        firstEven = head.next

        # Rearranging nodes
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        #Connect the last odd node to the first even node
        odd.next = firstEven

        return head

# Function to print the linked list
def printLL(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# Main function
if __name__ == "__main__":
    # Create a linked list with given values
    arr = [1, 3, 4, 2, 5, 6]
    head = ListNode(arr[0])
    head.next = ListNode(arr[1])
    head.next.next = ListNode(arr[2])
    head.next.next.next = ListNode(arr[3])
    head.next.next.next.next = ListNode(arr[4])
    head.next.next.next.next.next = ListNode(arr[5])

    # Print the original linked list
    print("Original Linked List: ", end="")
    printLL(head)

    # Rearrange the list and print it
    solution = Solution()
    head = solution.oddEvenList(head)
    print("New Linked List: ", end="")
    printLL(head)

Complexity Analysis
Time Complexity: O(N/2)x2 ~ O(N) because we are iterating over the odd-indexed as well as the even-indexed elements. Here N is the size of the given linked list.

Space Complexity: O(1) because we have not used any extra space.

'''
# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        firstEven = head.next

        # Rearranging nodes
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = firstEven

        return head
