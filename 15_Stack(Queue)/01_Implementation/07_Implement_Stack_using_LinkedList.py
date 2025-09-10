'''
Implement a Last-In-First-Out (LIFO) stack using a singly linked list. The implemented stack should support the following operations: push, pop, top, and isEmpty.



Implement the LinkedListStack class:



void push(int x): Pushes element x onto the stack.

int pop(): Removes and returns the top element of the stack.

int top(): Returns the top element of the stack without removing it.

boolean isEmpty(): Returns true if the stack is empty, false otherwise.


Examples:
Input:

["LinkedListStack", "push", "push", "pop", "top", "isEmpty"]

[[], [3], [7], [], [], []]



Output: [null, null, null, 7, 3, false]

Explanation:

LinkedListStack stack = new LinkedListStack();

stack.push(3);

stack.push(7);

stack.pop(); // returns 7

stack.top(); // returns 3

stack.isEmpty(); // returns false

Input:

["LinkedListStack", "isEmpty"]

[[]]



Output: [null, true]

Explanation:

LinkedListStack stack = new LinkedListStack();

stack.isEmpty(); // returns true

Input:

["LinkedListStack", "push", "pop", "isEmpty"]

[[], [2], [], []]

Output:
[null, null, 2, true]
Constraints:
1 <= numbers of calls made <= 100
1 <= x <= 100

Real Life Example
Consider a stack of plates in a cafeteria. Each time a plate is added, it is placed on top of the stack, and when a plate is taken, it is removed from the top. This ensures that the last plate added is the first one to be used. If this stack of plates were managed using a linked list, each plate would be a node in the list, dynamically linked to the one below it. This structure allows adding or removing plates without worrying about a fixed capacity or the need to shuffle plates around, mimicking the behavior of a real-world stack with dynamic flexibility.

Intuition
Implementing a stack using a linked list offers several advantages over using an array. Linked lists provide dynamic size flexibility, allowing the stack to grow and shrink as needed without worrying about predefined capacity or memory wastage. Each node in the linked list contains data and a reference to the next node, enabling efficient constant-time operations for both push and pop. This eliminates the risk of stack overflow and avoids the need for costly resizing operations, making linked lists an ideal choice for managing the dynamic nature of stack operations.

Approaching the problem of implementing a stack using a linked list can be likened to managing the stack of plates in the cafeteria example. Each plate represents a node in the linked list, and the top plate corresponds to the top node. To add a plate (push operation), a new node is created and placed on top of the stack, pointing to the previous top node. To remove a plate (pop operation), the top node is removed, and the next node in line becomes the new top. This dynamic linking and unlinking process allows the stack to grow and shrink efficiently, without any predefined capacity, just as the stack of plates can adjust to the number of plates being added or taken away.

Approach
Node Structure:
Define a node with:
An integer to store data.
A pointer to the next node.
A constructor to initialize data and the next pointer.
Stack Structure:
Define a stack with:
A pointer to the top node.
An integer to keep track of the size.
A constructor to initialize the top pointer and size.
Push Operation:
Create a new node with the given data & set the new node's next pointer to the current top node.
Update the top pointer to the new node. Increment the size.
Pop Operation:
Check if the stack is empty. If it is, return an error value (e.g., -1).
Store the data of the top node & update the top pointer to the next node.
Delete the old top node & decrement the size. Return the stored data.
Peek Operation:
Check if the stack is empty. If it is, return an error value (e.g., -1). Otherwise, return the data of the top node.
Is Empty Operation:
Check if the top pointer is null. Return true if the top pointer is null, otherwise false.
Size Operation:
Return the size of the stack.
Print Stack:
Traverse from the top node and print each node's data until reaching the end of the list.
# Node structure
class Node:
    def __init__(self, d):
        self.val = d
        self.next = None

# Structure to represent stack
class LinkedListStack:
    def __init__(self):
        self.head = None  # Top of Stack
        self.size = 0  # Size

    # Method to push an element onto the stack
    def push(self, x):
        # Creating a node
        element = Node(x)
        
        element.next = self.head  # Updating the pointers
        self.head = element  # Updating the top
        
        # Increment size by 1
        self.size += 1

    # Method to pop an element from the stack
    def pop(self):
        # If the stack is empty
        if self.head is None:
            return -1  # Pop operation cannot be performed
        
        value = self.head.val  # Get the top value
        temp = self.head  # Store the top temporarily
        self.head = self.head.next  # Update top to next node
        del temp  # Delete old top node
        self.size -= 1  # Decrement size
        
        return value  # Return data

    # Method to get the top element of the stack
    def top(self):
        # If the stack is empty
        if self.head is None:
            return -1  # Top element cannot be accessed
        
        return self.head.val  # Return the top

    # Method to check if the stack is empty
    def isEmpty(self):
        return self.size == 0

# Creating a stack
st = LinkedListStack()

# List of commands
commands = ["LinkedListStack", "push", "push", "pop", "top", "isEmpty"]
# List of inputs
inputs = [[], [3], [7], [], [], []]

for i in range(len(commands)):
    if commands[i] == "push":
        st.push(inputs[i][0])
        print("null", end=" ")
    elif commands[i] == "pop":
        print(st.pop(), end=" ")
    elif commands[i] == "top":
        print(st.top(), end=" ")
    elif commands[i] == "isEmpty":
        print("true" if st.is_empty() else "false", end=" ")
    elif commands[i] == "LinkedListStack":
        print("null", end=" ")
        
Complexity Analysis
Time Complexity: O(1) for push, pop, size,isEmpty, peek operations.

Space Complexity: O(N) because the stack requires space proportional to the number of elements it stores.


'''
class Node:
    def __init__(self, d):
        self.val = d
        self.next = None
class LinkedListStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, x):
        element = Node(x)
        element.next = self.head
        self.head = element
        self.size += 1

    def pop(self):
        if self.head is None:
            return -1
        value = self.head.val
        temp = self.head
        self.head = self.head.next
        del temp
        self.size -= 1
        return value


    def top(self):
        if self.head is None:
            return -1
        return self.head.val

    def isEmpty(self):
        return self.size == 0