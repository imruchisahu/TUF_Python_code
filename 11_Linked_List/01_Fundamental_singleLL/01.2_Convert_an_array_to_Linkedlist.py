class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to convert an array to a linked list
def arrayToLinkedList(arr):
    size = len(arr)
    if size == 0:
        return None

    # Create head of the linked list
    head = Node(arr[0])
    current = head

    # Iterate through the array and create linked list nodes
    for i in range(1, size):
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

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]

    # Convert array to linked list
    head = arrayToLinkedList(arr)

    # Print the linked list
    printLinkedList(head)
