'''
Implement a First-In-First-Out (FIFO) queue using an array. The implemented queue should support the following operations: push, dequeue, pop, and isEmpty.



Implement the ArrayQueue class:



void push(int x): Adds element x to the end of the queue.

int pop(): Removes and returns the front element of the queue.

int peek(): Returns the front element of the queue without removing it.

boolean isEmpty(): Returns true if the queue is empty, false otherwise.


Examples:
Input:

["ArrayQueue", "push", "push", "peek", "pop", "isEmpty"]

[[], [5], [10], [], [], []]

Output: [null, null, null, 5, 5, false]

Explanation:

ArrayQueue queue = new ArrayQueue();

queue.push(5);

queue.push(10);

queue.peek(); // returns 5

queue.pop(); // returns 5

queue.isEmpty(); // returns false

Input:

["ArrayQueue", "isEmpty"]

[[]]

Output:[null, true]

Explanation:

ArrayQueue queue = new ArrayQueue();

queue.isEmpty(); // returns true

Input:

["ArrayQueue", "push", "pop", "isEmpty"]

[[], [1], [], []]

Output:
[null, null, 1, true]
Constraints:
1 <= numbers of calls made <= 100
1 <= x <= 100


Intuition :
Imagine you're managing a ticket counter at a busy theater. You have a limited number of tickets to sell, and you want to ensure the process is efficient and fair. To do this, you use a special system to keep track of which tickets have been sold and which are available, without having to rearrange them constantly. This system operates like a circular queue.

The Ticket Counter (Queue): You have a counter with a fixed number of ticket slots, say 5 slots, arranged in a circle. Each slot can hold one ticket.

Selling a Ticket (Enqueue Operation): When a customer arrives to buy a ticket, you place the ticket in the next available slot. Keep track of the position where the next ticket should be placed using a variable called rear. For example, if you have sold tickets to 3 customers, your counter might look like this: [T1, T2, T3, _, _], where T1, T2, and T3 represent sold tickets, and the next ticket will be placed in the fourth slot.

Customer Leaving with a Ticket (Dequeue Operation): When a customer takes a ticket, you remove it from the slot at the front of the queue. Instead of shifting all the tickets forward, you just move the front pointer to the next slot. Continuing with our example, if the first customer takes their ticket, your counter now looks like this: [_, T2, T3, _, _], with the front pointing to the second slot.

Handling Wrap-Around (Circular Array): When the rear or front reaches the end of the array, it wraps around to the beginning. This ensures that you make efficient use of the available slots without needing to shift tickets around. If you sell more tickets and the rear reaches the end, it wraps around like this: [T4, T5, T3, _, T1] with the rear and front properly adjusted using modular arithmetic.

Checking Availability (IsEmpty and IsFull Operations): You need to check if there are any tickets left or if your counter is full. These checks ensure you manage the tickets efficiently.

Approach :
Declare an Array of a Particular Size: Declare an array to store the elements of the queue. The size of this array is determined when the queue is initialized.
Define Variables:
start: Tracks the index of the front element.
end: Tracks the index of the last element.
size: Keeps the current number of elements in the queue.
capacity: The maximum number of elements the queue can hold.
Push Operation (push(int x)): Check if the queue is full by comparing size and capacity. If not full, increment the rear using modular arithmetic to wrap around if necessary, then insert the element at the rear index. Increment the size.
Pop Operation (pop()): Check if the queue is empty by comparing the size with 0. If not empty, return the element at the front index, then increment the front using modular arithmetic to wrap around if necessary. Decrement the size.
Peek Operation (peek()): Check if the queue is empty. If not empty, return the element at the front index.
IsEmpty Operation (isEmpty()): Check if the size is 0 to determine if the queue is empty.

# Class implementing Queue using Arrays
class ArrayQueue:
    # Constructor
    def __init__(self):
        # Array to store queue elements
        self.arr = [0] * 10
        # Indices for start and end of the queue
        self.start = -1
        self.end = -1
        # Current size and maximum size of the queue
        self.currSize = 0
        self.maxSize = 10

    # Method to push an element into the queue
    def push(self, x):
        # Check if the queue is full
        if self.currSize == self.maxSize:
            print("Queue is full\nExiting...")
            exit(1)

        # If the queue is empty, initialize start and end
        if self.end == -1:
            self.start = 0
            self.end = 0
        else:
            # Circular increment of end
            self.end = (self.end + 1) % self.maxSize

        self.arr[self.end] = x
        self.currSize += 1

    # Method to pop an element from the queue
    def pop(self):
        # Check if the queue is empty
        if self.start == -1:
            print("Queue Empty\nExiting...")
            exit(1)
        popped = self.arr[self.start]

        # If the queue has only one element, reset start and end
        if self.currSize == 1:
            self.start = -1
            self.end = -1
        else:
            # Circular increment of start
            self.start = (self.start + 1) % self.maxSize

        self.currSize -= 1
        return popped

    # Method to get the front element of the queue
    def peek(self):
        # Check if the queue is empty
        if self.start == -1:
            print("Queue is Empty")
            exit(1)
        return self.arr[self.start]

    # Method to determine whether the queue is empty
    def isEmpty(self):
        return self.currSize == 0


if __name__ == "__main__":
    queue = ArrayQueue()
    commands = ["ArrayQueue", "push", "push", "peek", "pop", "isEmpty"]
    inputs = [[], [5], [10], [], [], []]

    for i in range(len(commands)):
        if commands[i] == "push":
            queue.push(inputs[i][0])
            print("null", end=" ")
        elif commands[i] == "pop":
            print(queue.pop(), end=" ")
        elif commands[i] == "peek":
            print(queue.peek(), end=" ")
        elif commands[i] == "isEmpty":
            print("true" if queue.isEmpty() else "false", end=" ")
        elif commands[i] == "ArrayQueue":
            print("null", end=" ")
            
Complexity Analysis:
Time Complexity: O(1) as all individual queue operations are taking constant time.

Space Complexity: O(1) as the implementation uses a fixed size array.


'''
class ArrayQueue:
    def __init__(self):
        self.arr = [0] * 10
        self.start = -1
        self.end = -1
        self.currSize = 0
        self.maxSize = 10


    def push(self, x):
        if self.currSize == self.maxSize:
            print("Queue is full\nExiting...")
            exit(1)
        if self.end == -1:
            self.start = 0
            self.end = 0
        else:
            self.end = (self.end + 1) % self.maxSize

        self.arr[self.end] = x
        self.currSize += 1
 

    def pop(self):
        if self.start == -1:
            print("Queue Empty\nExiting...")
            exit(1)
        popped = self.arr[self.start]

        if self.currSize == 1:
            self.start = -1
            self.end = -1
        else:
            self.start = (self.start + 1) % self.maxSize

        self.currSize -= 1
        return popped

    def peek(self):
        if self.start == -1:
            print("Queue is Empty")
            exit(1)
        return self.arr[self.start]

    def isEmpty(self):
        return self.currSize == 0