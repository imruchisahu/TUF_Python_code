'''
Implement a First-In-First-Out (FIFO) queue using a singly linked list. The implemented queue should support the following operations: push, pop, peek, and isEmpty.



Implement the LinkedListQueue class:



void push(int x): Adds element x to the end of the queue.

int pop(): Removes and returns the front element of the queue.

int peek(): Returns the front element of the queue without removing it.

boolean isEmpty(): Returns true if the queue is empty, false otherwise.


Examples:
Input:

["LinkedListQueue", "push", "push", "peek", "pop", "isEmpty"]

[[], [3], [7], [], [], []]

Output:[null, null, null, 3, 3, false]

Explanation:

LinkedListQueue queue = new LinkedListQueue();

queue.push(3);

queue.push(7);

queue.peek(); // returns 3

queue.pop(); // returns 3

queue.isEmpty(); // returns false

Input:

["LinkedListQueue", "push", "pop", "isEmpty"]

[[], [2], [], []]

Output: [null, null, 2, true]

Explanation:

LinkedListQueue queue = new LinkedListQueue();

queue.push(2);

queue.pop(); // returns 2

queue.isEmpty(); // returns true

Input:["LinkedListQueue", "isEmpty"]

[[]]

Output:
[null, true]
Constraints:
1 <= numbers of calls made <= 100
1 <= x <= 100

Real Life Example
Think of a line of cars waiting at a drive-thru. Each car is connected to the one in front of it, forming a chain. The car at the front is served first, and when it leaves, the next car in line becomes the new front. Cars continue to arrive at the end of the line, and each new arrival is connected to the last car. This way, the line can grow or shrink as needed, much like how a linked list dynamically adjusts its size without any fixed limit.

Intuition
Implementing a queue using a linked list leverages the dynamic memory allocation properties of linked lists. This allows the queue to grow and shrink as needed without a predetermined size. Each element in the queue is represented by a node in the linked list, and the queue is managed through pointers to the front and rear nodes, enabling efficient addition and removal of elements.

Approaching the problem of implementing a queue using a linked list can be visualized through the drive-thru line of cars example. Each car represents a node in the linked list, with the front car corresponding to the front node and the last car to the rear node. When a new car arrives (enqueue operation), a new node is created and linked to the rear node, updating the rear pointer to this new node. When the front car is served and leaves (dequeue operation), the front pointer is updated to the next node in line. This dynamic linking allows the queue to efficiently grow and shrink, just as the line of cars adjusts with arrivals and departures.

Approach
Node Structure: Define a node that holds data and a pointer to the next node. This node is the basic building block of the linked list.
Queue Initialization:
Initialize the queue with pointers to both the front and rear of the queue. Set these pointers to null initially, indicating an empty queue.
Maintain a counter to track the number of elements in the queue.
Enqueue Operation (Adding an Element):
Create a new node with the given data.
If the queue is empty, set both the front and rear pointers to this new node.
If the queue is not empty, link the current rear node to the new node and update the rear pointer to point to the new node.
Dequeue Operation (Removing an Element):
Check if the queue is empty. If it is, return an appropriate message or handle the empty condition.
If the queue is not empty, move the front pointer to the next node and delete the old front node.
If the queue becomes empty after removal, set the rear pointer to null.
Peek Operation (Accessing the Front Element):
Check if the queue is empty. If it is, return an appropriate message or handle the empty condition.
If the queue is not empty, return the data of the front node without removing it.
Size Operation:
Return the value of the counter tracking the number of elements in the queue.
IsEmpty Operation:
Check if the front pointer is null. If it is, the queue is empty; otherwise, it is not.

# Node structure
class Node:
    def __init__(self, d):
        self.val = d
        self.next = None

# Structure to represent queue
class LinkedListQueue:
    def __init__(self):
        self.start = self.end = None  # Start and End of the queue
        self.size = 0  # Size of the queue

    # Method to push an element in the queue
    def push(self, x):
        # Creating a node
        element = Node(x)
        
        # If it is the first element being pushed
        if self.start is None:
            # Initialize the pointers
            self.start = self.end = element
        else:
            self.end.next = element  # Updating the pointers
            self.end = element  # Updating the end
        
        # Increment size by 1
        self.size += 1

    # Method to pop an element from the queue
    def pop(self):
        # If the queue is empty
        if self.start is None:
            return -1  # Pop operation cannot be performed
        
        value = self.start.val  # Get the front value
        temp = self.start  # Store the front temporarily
        self.start = self.start.next  # Update front to next node
        del temp  # Delete old front node
        self.size -= 1  # Decrement size
        
        return value  # Return data

    # Method to get the front element in the queue
    def peek(self):
        # If the queue is empty
        if self.start is None:
            return -1  # Front element cannot be accessed
        
        return self.start.val  # Return the front

    # Method to check if the queue is empty
    def isEmpty(self):
        return self.size == 0


# Creating a queue
q = LinkedListQueue()

# List of commands
commands = ["LinkedListQueue", "push", "push", "peek", "pop", "isEmpty"]
# List of inputs
inputs = [[], [3], [7], [], [], []]

for i in range(len(commands)):
    if commands[i] == "push":
        q.push(inputs[i][0])
        print("null", end=" ")
    elif commands[i] == "pop":
        print(q.pop(), end=" ")
    elif commands[i] == "peek":
        print(q.peek(), end=" ")
    elif commands[i] == "isEmpty":
        print("true" if q.is_empty() else "false", end=" ")
    elif commands[i] == "LinkedListQueue":
        print("null", end=" ")
Complexity Analysis
Time Complexity: O(1) because the time complexity for the push, pop, peek, size, and isEmpty operations is O(1).

Space Complexity: O(N) where N is the number of elements of the stack.


'''