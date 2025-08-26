'''
Given the head of a special linked list of n nodes where each node contains an additional pointer called 'random' which can point to any node in the list or null.



Construct a deep copy of the linked list where,

n new nodes are created with corresponding values as original linked list.
The random pointers point to the corresponding new nodes as per their arrangement in the original list.
Return the head of the newly constructed linked list.


Note: For custom input, a n x 2 matrix is taken with each row having 2 values:[ val, random_index] where,

val: an integer representing ListNode.val
random_index: index of the node (0 - n-1) that the random pointer points to, otherwise -1.

Examples:
Input: [[1, -1], [2, 0], [3, 4], [4, 1], [5, 2]]

Output: 1 2 3 4 5, true

Explanation: All the nodes in the new list have same corresponding values as original nodes.

All the random pointers point to their corresponding nodes in the new list.

'true' represents that the nodes and references were created new.

Input: [[5, -1], [3, -1], [2, 1], [1, 1]]

Output: 5 3 2 1, true

Explanation: All the nodes in the new list have same corresponding values as original nodes.

All the random pointers point to their corresponding nodes in the new list.

'true' represents that the nodes and references were created new.

[[5, -1], [3, -1], [2, -1], [1, -1]] will be incorrect, although it has the same values.

Input: [[-1, -1], [-2, -1], [-3, -1], [10, -1]]

Output:
-1 -2 -3 10, true
Constraints:
n == number of nodes in the linked list.
1 <= n <= 105
-104 <= ListNode.val <= 104
0 <= random_index < n or random_index == -1.

#BRute
# Intuition
Create a deep copy of the original linked list and use a map to establish a relationship between the original nodes and their copied nodes.
We traverse the list first to create a copied node for each original node then traverse and establish the correct connections between the copied nodes similar to the arrangement of the next and random pointers of the original pointers.
Approach
Begin by setting up a pointer to traverse the original linked list. Use an empty map to associate each original node with its copied counterpart.
As you traverse the original linked list, create a new node for each original node, copying its data. Store each new node in the map, linking it to the corresponding original node.
Traverse the original list again to set up the connections for the copied nodes. Use the map to find the copied nodes and establish their next and random pointers, ensuring they mimic the original structure.
Finally, retrieve the head of the copied list from the map by looking up the copied node corresponding to the original list's head. This gives you a deep copy of the entire linked list with the same structure and connections as the original.

class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    # Function to clone linked list with random pointers
    def copyRandomList(self, head):
        # If the head is null, return null
        if not head:
            return None

        # Create a dictionary to map original nodes to their corresponding copied nodes
        mpp = {}
        temp = head

        # Create copies of each node
        while temp:
            # Create new node with same value as original
            newNode = ListNode(temp.val)
            # Map to original node
            mpp[temp] = newNode
            # Move to next node
            temp = temp.next

        # Reset temp
        temp = head

        # Connect the next and random pointers of the copied nodes using the map
        while temp:
            # Get copied node from the map
            copyNode = mpp[temp]
            # Set next pointer of copied node to the copied node of the next original node
            copyNode.next = mpp.get(temp.next)
            # Set the random pointer of the copied node to the copied node of the random original node
            copyNode.random = mpp.get(temp.random)
            temp = temp.next

        # Return the head
        return mpp[head]

# Function to print the linked list
def printClonedLinkedList(head):
    while head:
        # Print the data of the current node
        print(f"Data: {head.val}", end="")
        # Print the data of the random pointer, if it exists
        if head.random:
            print(f", Random: {head.random.val}", end="")
        else:
            print(", Random: None", end="")
        print()
        # Move to the next node
        head = head.next

# Main function
if __name__ == "__main__":
    # Example linked list: 7 -> 14 -> 21 -> 28
    head = ListNode(7)
    head.next = ListNode(14)
    head.next.next = ListNode(21)
    head.next.next.next = ListNode(28)

    # Assigning random pointers
    head.random = head.next.next  # 7 -> 21
    head.next.random = head  # 14 -> 7
    head.next.next.random = head.next.next.next  # 21 -> 28
    head.next.next.next.random = head.next  # 28 -> 14

    # Print the original linked list
    print("Original Linked List with Random Pointers:")
    printClonedLinkedList(head)

    # Clone the linked list
    solution = Solution()
    clonedList = solution.copyRandomList(head)

    # Print the cloned linked list
    print("\nCloned Linked List with Random Pointers:")
    printClonedLinkedList(clonedList)

Complexity Analysis
Time Complexity: O(2N) because the linked list is traversed twice, once for creating copies of each node and for the second time to set the next and random pointers for each copied node. The time to access the nodes in the map is O(1) due to hashing. Here N is the length of the Linked List.

Space Complexity: O(N)+O(N) where N is the number of nodes in the linked list as all nodes are stored in the map to maintain mappings and the copied linked list takes O(N) space as well.

#Optimal
Intuition
To avoid using extra space for mappings, insert each copied node right after its original node in the list. This allows quick access without additional storage.
Traverse the list to create a copy of each node and place it immediately after the original node. Then, set the random pointers for the copied nodes by using the copied nodes directly following the originals. Finally, separate the original and copied nodes by detaching alternate nodes, resulting in two lists: one with the original nodes and one with the copied nodes, both maintaining the original structure and random pointers.
Approach
Traverse the original list and create a copy of each node, inserting it immediately after the original node. This way, each original node is followed by its copy.
Traverse the modified list and set the random pointers for the copied nodes to match the corresponding original nodes. If an original node’s random pointer is null, set the copied node’s random pointer to null as well.
Traverse the modified list again to separate the copied nodes from the original nodes. Break the links between the original and copied nodes, and restore the original list to its initial state by fixing the next pointers.
Return the head of the deep copy obtained after extracting the copied nodes from the modified list.

class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    # Insert a copy of each node in between the original nodes
    def insertCopyInBetween(self, head):
        temp = head
        while temp:
            nextElement = temp.next
            # Create a new node with the same data
            copy = ListNode(temp.val)
            
            copy.next = nextElement
            
            temp.next = copy
            
            temp = nextElement

    # Function to connect random pointers of the copied nodes
    def connectRandomPointers(self, head):
        temp = head
        while temp:
            # Access the copied node
            copyNode = temp.next
            
            #If the original node has a random pointer point the copied node's random to the corresponding copied random node
            #set the copied node's random to null 
            #if the original random is null
            if temp.random:
                copyNode.random = temp.random.next
            else:
                copyNode.random = None
            
            # Move to next original node
            temp = temp.next.next

    # Function to retrieve the deep copy of the linked list
    def getDeepCopyList(self, head):
        temp = head
        # Create a dummy node
        dummyNode = ListNode(-1)
        # Initialize a result pointer
        res = dummyNode

        while temp:
            #Creating a new List by pointing to copied nodes
            res.next = temp.next
            res = res.next

            #Disconnect and revert back to the initial state of the original linked list
            temp.next = temp.next.next
            temp = temp.next
        
        #Return the deep copy of the list starting from the dummy node
        return dummyNode.next

    # Function to clone the linked list
    def copyRandomList(self, head):
        # If the original list is empty, return null
        if not head:
            return None

        # Insert nodes in between
        self.insertCopyInBetween(head)
        # Connect random pointers
        self.connectRandomPointers(head)
        # Retrieve deep copy of linked list
        return self.getDeepCopyList(head)

# Function to print the cloned linked list
def printClonedLinkedList(head):
    while head:
        print(f"Data: {head.val}", end="")
        if head.random:
            print(f", Random: {head.random.val}", end="")
        else:
            print(", Random: null", end="")
        print()
        # Move to the next node
        head = head.next

if __name__ == "__main__":
    # Example linked list: 7 -> 14 -> 21 -> 28
    head = ListNode(7)
    head.next = ListNode(14)
    head.next.next = ListNode(21)
    head.next.next.next = ListNode(28)

    # Assigning random pointers
    head.random = head.next.next  # 7 -> 21
    head.next.random = head  # 14 -> 7
    head.next.next.random = head.next.next.next  # 21 -> 28
    head.next.next.next.random = head.next  # 28 -> 14

    # Print the original linked list
    print("Original Linked List with Random Pointers:")
    printClonedLinkedList(head)

    # Clone the linked list
    solution = Solution()
    clonedList = solution.copyRandomList(head)

    # Print the cloned linked list
    print("\nCloned Linked List with Random Pointers:")
    printClonedLinkedList(clonedList)

    
Complexity Analysis
Time Complexity: O(3N) where N is the number of nodes in the linked list:
First traversal to create copies of the nodes and insert them between the original nodes.
Second traversal to set the random pointers of the copied nodes to their corresponding copied nodes.
Third traversal to separate the copied nodes from the original nodes.
Space Complexity: O(N) where N is the number of nodes in the linked list as the only extra space allocated is to create the copied list without creating any other additional data structures.

'''
# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        mpp = {}
        temp = head
        while temp:
            newNode = ListNode(temp.val)
            mpp[temp] = newNode
            temp = temp.next
        temp = head
        while temp:
            copyNode = mpp[temp]
            copyNode.next = mpp.get(temp.next)
            copyNode.random = mpp.get(temp.random)
            temp = temp.next
        return mpp[head]