'''
Implement a Last-In-First-Out (LIFO) stack using a single queue. The implemented stack should support the following operations: push, pop, top, and isEmpty.



Implement the QueueStack class:



void push(int x): Pushes element x onto the stack.

int pop(): Removes and returns the top element of the stack.

int top(): Returns the top element of the stack without removing it.

boolean isEmpty(): Returns true if the stack is empty, false otherwise.


Examples:
Input:

["QueueStack", "push", "push", "pop", "top", "isEmpty"]

[[], [4], [8], [], [], []]

Output: [null, null, null, 8, 4, false]

Explanation:

QueueStack stack = new QueueStack();

stack.push(4);

stack.push(8);

stack.pop(); // returns 8

stack.top(); // returns 4

stack.isEmpty(); // returns false

Input:

["QueueStack", "isEmpty"]

[[]]

Output:[null, true]

Explanation:

 QueueStack stack = new QueueStack();

stack.isEmpty(); // returns true

Input:

["QueueStack", "push", "pop", "isEmpty"]

[[], [6], [], []]

Output:
[null, null, 6, true]
Constraints:
1 <= numbers of calls made <= 100
1 <= x <= 100


Intuition:
Imagine you have a box (queue) that can only be accessed from one side. You want to use this box to simulate a stack, where the last item you put in is the first one you take out. This is like stacking plates: you put a plate on top and when you need a plate, you take the top one. Here's how we can achieve this with our box:

Pushing Items: When you want to push an item onto the stack, you put it in the box (queue) and then move all the other items in the box (queue) to the back of the new item. This way, the new item is always at the front, simulating the top of the stack. For example, if the box currently has plates A, B, C, and you want to add D, you put D in the box and then rearrange so that D is at the front followed by A, B, C.

Popping Items: To pop an item, you simply take out the item at the front of the box (queue). This is like taking the top plate off the stack. In our example, popping would remove D, leaving A, B, C in the box.

Top Item: To see the top item without removing it, you look at the item at the front of the box (queue). In our example, peeking would show D.

Checking if Stack is Empty: To check if the stack is empty, you just check if the box (queue) is empty.

Approach:
Data Structure Used: A single queue will be used to store the elements.
Push(x): Insert the element x into the queue. Rearrange the elements in the queue to maintain the stack order by:
Running a loop that iterates size() - 1 times, where size() is the current number of elements in the queue.
In each iteration, remove the front element and add it back to the rear of the queue. This ensures that the most recently added element is always at the front of the queue.
Pop(): Remove and return the front element of the queue, which corresponds to the top of the stack.
isEmpty(): Return true if the queue is empty, and false otherwise.

from queue import Queue

# Stack implementation using Queue
class QueueStack:
    def __init__(self):
        # Queue
        self.q = Queue()

    # Method to push element in the stack
    def push(self, x):
        # Get size
        s = self.q.qsize()
        # Add element
        self.q.put(x)

        # Move elements before new element to back
        for _ in range(s):
            self.q.put(self.q.get())

    # Method to pop element from stack
    def pop(self):
        # Get front element
        n = self.q.queue[0]
        # Remove front element
        self.q.get()
        # Return removed element
        return n

    # Method to return the top of stack
    def top(self):
        # Return front element
        return self.q.queue[0]

    # Method to check if the stack is empty
    def isEmpty(self):
        return self.q.empty()

if __name__ == "__main__":
    st = QueueStack()

    # List of commands
    commands = ["QueueStack", "push", "push", "pop", "top", "isEmpty"]
    inputs = [[], [4], [8], [], [], []]

    for i in range(len(commands)):
        if commands[i] == "push":
            st.push(inputs[i][0])
            print("null", end=" ")
        elif commands[i] == "pop":
            print(st.pop(), end=" ")
        elif commands[i] == "top":
            print(st.top(), end=" ")
        elif commands[i] == "isEmpty":
            print("true" if st.isEmpty() else "false", end=" ")
        elif commands[i] == "QueueStack":
            print("null", end=" ")
            
Complexity Analysis:
Time Complexity:
Push operation: O(n) (where n is the number of elements in the queue at that time) because every time an element is pushed, all the elements in the queue are popped from front and pushed in the back again.
Pop operation: O(1) as constant operations are performed.
Top operation: O(1) as constant operations are performed.
IsEmpty operation: O(1) as constant operations are performed.


Space Complexity: O(k) for storing k elements in the queue.


'''
from queue import Queue
class QueueStack:
    def __init__(self):
        self.q = Queue()

    def push(self, x):
        s=self.q.qsize()
        self.q.put(x)
        for _ in range(s):
            self.q.put(self.q.get())

    def pop(self):
        n=self.q.queue[0]
        self.q.get()
        return n

    def top(self):
        return self.q.queue[0]

    def isEmpty(self):
        return self.q.empty()
