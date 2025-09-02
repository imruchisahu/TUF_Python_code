'''
Implement a Last-In-First-Out (LIFO) stack using an array. The implemented stack should support the following operations: push, pop, peek, and isEmpty.



Implement the ArrayStack class:



void push(int x): Pushes element x onto the stack.

int pop(): Removes and returns the top element of the stack.

int top(): Returns the top element of the stack without removing it.

boolean isEmpty(): Returns true if the stack is empty, false otherwise.







Please note that this section might seem a bit difficult without prior knowledge on what stacks is, we will soon try to add basics concepts for your ease! If you know the concepts already please go ahead to give a shot to the problem. Cheers!


Examples:
Input: ["ArrayStack", "push", "push", "top", "pop", "isEmpty"]

[[], [5], [10], [], [], []]

Output: [null, null, null, 10, 10, false]

Explanation:

ArrayStack stack = new ArrayStack();

stack.push(5);

stack.push(10);

stack.top(); // returns 10

stack.pop(); // returns 10

stack.isEmpty(); // returns false

Input: ["ArrayStack","isEmpty", "push", "pop", "isEmpty"]

[[], [], [1], [], []]

Output: [null, true, null, 1, true]

Explanation: 

ArrayStack stack = new ArrayStack();

stack.push(1);

stack.pop(); // returns 1

stack.isEmpty(); // returns true

Input: ["ArrayStack", "isEmpty"]

[[], []]

Output:
[null, true]
Constraints:
1 <= numbers of calls made <= 100
1 <= x <= 100

Intuition
Imagine you're working in a library, and there's a special shelf dedicated to books that are being frequently accessed. This shelf operates on a Last-In-First-Out (LIFO) principle, meaning the last book you put on the shelf is the first one you'll take off. This shelf can be thought of as a stack, and the following operations will help manage the books on this shelf.

Push Operation (push(int x)):
Think of adding a book to the top of the stack. Every time a new book arrives, you place it on the topmost spot available on the shelf. For instance, if the current stack of books is [Book1, Book2], and Book3 arrives, you place Book3 on top. The stack now looks like [Book1, Book2, Book3].

Pop Operation (pop()):
This operation is like removing the topmost book from the stack. The book that was last added (the one on the top) is the one you take off the shelf. Continuing with our example, if you perform a pop() operation, you remove Book3 from the stack. The stack now looks like [Book1, Book2].

Top Operation (top()):
Sometimes you just want to know which book is on top without removing it. The top() operation allows you to peek at the topmost book. If your stack is [Book1, Book2, Book3], calling top() will tell you that Book3 is on the top without removing it from the stack.

IsEmpty Operation (isEmpty()):
Before adding or removing books, you might want to check if the shelf is empty. The isEmpty() operation checks whether there are any books on the shelf. If there are no books, it returns true; otherwise, it returns false.

Approach
Declare an Array of Particular Size:
We need to initialize an array that will hold the elements of the stack. The size of the array is defined when the stack is created.

Define a Variable “Top” and Initialize It as -1:
The top variable keeps track of the index of the last added element in the stack. Initializing it to -1 indicates that the stack is empty.

Push Operation (push(int x)):
To push an element onto the stack, we increment the top index by one and insert the element at this position in the array. If the stack is full (i.e., top is equal to the last index of the array), we throw a stack overflow exception.

Pop Operation (pop()):
To pop an element from the stack, we check if the stack is not empty by ensuring top is not equal to -1. If the stack is empty, we throw a stack underflow exception. If the stack is not empty, we return the element at the top index and then decrement the top index by one.

Top Operation (top()):
To get the top element without removing it, we check if the stack is not empty. If the stack is empty, we throw an exception. If the stack is not empty, we return the element at the top index.

IsEmpty Operation (isEmpty()):
To check if the stack is empty, we simply check if the top index is -1.

Size Operation (size()):
To get the current size of the stack, we return top + 1.

class ArrayStack:
    # Constructor
    def __init__(self, size=1000):
        # Array to hold elements
        self.stackArray = [0] * size
        # Maximum capacity
        self.capacity = size
        # Initialize stack as empty
        self.topIndex = -1

    # Pushes element x
    def push(self, x):
        if self.topIndex >= self.capacity - 1:
            print("Stack overflow")
            return
        self.topIndex += 1
        self.stackArray[self.topIndex] = x

    # Removes and returns top element
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            # Return invalid value
            return -1
        top_element = self.stackArray[self.topIndex]
        self.topIndex -= 1
        return top_element

    # Returns top element
    def top(self):
        if self.isEmpty():
            print("Stack is empty")
            return -1
        return self.stackArray[self.topIndex]

    #Returns true if the stack is empty, false otherwise
    def isEmpty(self):
        return self.topIndex == -1

# Main function
if __name__ == "__main__":
    stack = ArrayStack()
    commands = ["ArrayStack", "push", "push", "top", "pop", "isEmpty"]
    inputs = [[], [5], [10], [], [], []]

    for i in range(len(commands)):
        if commands[i] == "push":
            stack.push(inputs[i][0])
            print("null", end=" ")
        elif commands[i] == "pop":
            print(stack.pop(), end=" ")
        elif commands[i] == "top":
            print(stack.top(), end=" ")
        elif commands[i] == "isEmpty":
            print("true" if stack.isEmpty() else "false", end=" ")
        elif commands[i] == "ArrayStack":
            print("null", end=" ")

Complexity Analysis
Time Complexity: O(1) because the individual stack operations take O(1).

Space Complexity: O(N) for using a stack which is equivalent to the size of the array.



'''