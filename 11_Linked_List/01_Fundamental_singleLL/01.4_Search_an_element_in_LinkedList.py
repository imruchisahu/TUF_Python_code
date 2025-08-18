class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to print the linked list
def printLinkedList(head):
    current = head
    while current is not None:
        print(f"{current.data} -> ", end="")
        current = current.next
    print("None")

# To search for an element in the linked list
def searchElement(head, target):
    current = head

    # Traverse the linked list
    while current is not None:
        if current.data == target:
            return True
        current = current.next

    return False

if __name__ == "__main__":
    # Create a linked list manually
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # Print the linked list
    printLinkedList(head)

    # Search for an element in the linked list
    target = 3
    if searchElement(head, target):
        print(f"Element {target} found in the linked list.")
    else:
        print(f"Element {target} not found in the linked list.")
