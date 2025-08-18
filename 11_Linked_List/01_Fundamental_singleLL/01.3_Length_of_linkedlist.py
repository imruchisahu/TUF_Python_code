# Define a Node class
class Node:
    # Constructor to initialize a new node
    def __init__(self, val):
        self.data = val
        self.next = None

# Function to convert an array to a linked list
def arrayToLinkedList(arr):
    if len(arr) == 0:
        return None

    # Create head of the linked list
    head = Node(arr[0])
    current = head

    ''' Iterate through the array 
    and create linked list nodes '''
    for i in range(1, len(arr)):
        current.next = Node(arr[i])
        current = current.next

    return head

# Function to print the linked list
def printLinkedList(head):
    current = head
    while current is not None:
        print(f"{current.data} -> ", end="")
        current = current.next
    print("None")

# To calculate length of linked list
def lengthOfLinkedList(head):
    length = 0
    current = head

    # Count the nodes
    while current is not None:
        length += 1
        current = current.next

    return length

# Main code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]

    # Convert array to linked list
    head = arrayToLinkedList(arr)

    # Print the linked list
    printLinkedList(head)

    # Calculate the length of the linked list
    length = lengthOfLinkedList(head)
    print(f"Length of the linked list: {length}")
