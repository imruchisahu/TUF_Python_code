'''
Design a stack that supports the following operations in constant time: push, pop, top, and retrieving the minimum element.



Implement the MinStack class:



MinStack(): Initializes the stack object.

void push(int val): Pushes the element val onto the stack.

void pop(): removes the element on the top of the stack.

int top(): gets the top element of the stack.

int getMin(): retrieves the minimum element in the stack.


Examples:
Input:

["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]

[ [], [-2], [0], [-3], [ ], [ ], [ ], [ ] ]



Output:

[null, null, null, null, -3, null, 0, -2]



Explanation:

MinStack minStack = new MinStack();

minStack.push(-2);

minStack.push(0);

minStack.push(-3);

minStack.getMin(); // returns -3

minStack.pop();

minStack.top();  // returns 0

minStack.getMin(); // returns -2

Input:

["MinStack", "push", "push", "getMin", "push", "pop", "getMin", "top"]

[ [ ], [5], [1], [ ], [3], [ ], [ ], [ ] ]



Output:

[null, null, null, 1, null, null, 1, 1]



Explanation:

MinStack minStack = new MinStack();

minStack.push(5);

minStack.push(1);

minStack.getMin(); // returns 1

minStack.push(3);

minStack.pop();

minStack.getMin(); // returns 1

minStack.top();  // returns 1

Input:

["MinStack", "push", "push", "push", "top", "getMin", "pop", "getMin"]

[[], [10], [15], [5], [], [], [], []]

Output:
[null, null, null, null, 5, 5, null, 10]
Constraints:
-105 <= val <=105
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 5*104 calls will be made to push, pop, top, and getMin.


#
# Brute
# Intuition:
In a usual stack data structure, there is no method to get the minimum element present in the stack in constant time. This can be overcome, if all the numbers are stored in pairs with their current minimum element. This way, the stack will not only able to perform the previous methods in constant time, but also perform the getMin() method in constant time.

Note: The stack will store the following pair: {element, current minimum}

Approach:
A stack of pairs is used. Each pair contains the element itself and the minimum element at the time the element was pushed onto the stack. The MinStack class is initialized with an empty stack.
Push Operation: When a new element is pushed, it is compared with the current minimum. The new element and the updated minimum are stored as a pair and pushed onto the stack.
Pop Operation: The top element (which is a pair) is removed from the stack.
Top Operation: The top element of the stack is accessed to get the actual value (first component) stored.
GetMin Operation: The second value of the pair at the top of the stack, which represents the minimum element at that point, is accessed.

class MinStack:
    # Empty Constructor
    def __init__(self):
        # Initialize a stack
        self.st = []

    # Method to push a value in stack
    def push(self, value):
        # If stack is empty
        if not self.st:
            # Push current value as minimum
            self.st.append((value, value))
            return

        # Update the current minimum
        mini = min(self.getMin(), value)

        # Add the pair to the stack
        self.st.append((value, mini))

    # Method to pop a value from stack
    def pop(self):
        # Using in-built pop method
        self.st.pop()

    # Method to get the top of stack
    def top(self):
        # Return the top value
        return self.st[-1][0]

    # Method to get the minimum in stack
    def getMin(self):
        # Return the minimum
        return self.st[-1][1]

if __name__ == "__main__":
    s = MinStack()
    
    # Function calls
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin(), end=" ")
    s.pop()
    print(s.top(), end=" ")
    s.pop()
    print(s.getMin())

Complexity Analysis:
Time Complexity: O(1) All the operations take constant time.

Space Complexity: O(2*N) (where N is the total number of calls made for push operation)
All the numbers are stored in pairs leading to a stack space of O(2*N).

#Optimal
Intuition:
To efficiently keep track of the minimum element in the stack at all times while maintaining constant time complexity for each operation, a clever approach is needed. This can be achieved by modifying the values stored in the stack when a new minimum is encountered. Instead of storing pairs or auxiliary stacks, we store a specially calculated value that allows us to track the minimum.

Approach:
Use a stack to store elements. Maintain a variable to keep track of the current minimum value.
Push Operation:
If the stack is empty, push the value and set it as the current minimum.
If the value is greater than or equal to the current minimum, push the value.
If the value is less than the current minimum, push a modified value calculated using the new value and update the current minimum.
Pop Operation:
If the stack is empty, do nothing. Otherwise, Retrieve and pop the top value.
If the popped value indicates it was used to store a new minimum, update the current minimum using the retrieved value.
Top Operation:
If the stack is empty, return -1 indicating the stack is empty.
Retrieve the top value. If the top value is greater than or equal to the current minimum, return it.
If the top value indicates it was used to store a new minimum, return the current minimum.
GetMin Operation: Simply return the current minimum.

class MinStack:
    def __init__(self):
        # Initialize a stack
        self.st = []
        # To store the minimum value
        self.mini = None

    # Method to push a value in stack
    def push(self, value):
        # If stack is empty
        if not self.st:
            # Update the minimum value
            self.mini = value

            # Push current value as minimum
            self.st.append(value)
            return

        # If the value is greater than the minimum
        if value > self.mini:
            self.st.append(value)
        else:
            # Add the modified value to stack
            self.st.append(2 * value - self.mini)
            # Update the minimum
            self.mini = value

    # Method to pop a value from stack
    def pop(self):
        # Base case
        if not self.st:
            return

        # Get the top
        x = self.st.pop()

        # If the modified value was added to stack
        if x < self.mini:
            # Update the minimum
            self.mini = 2 * self.mini - x

    # Method to get the top of stack
    def top(self):
        # Base case
        if not self.st:
            return -1

        # Get the top
        x = self.st[-1]

        # Return top if minimum is less than the top
        if self.mini < x:
            return x

        # Otherwise return mini
        return self.mini

    # Method to get the minimum in stack
    def getMin(self):
        # Return the minimum
        return self.mini


if __name__ == "__main__":
    s = MinStack()

    # Function calls
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin(), end=" ")
    s.pop()
    print(s.top(), end=" ")
    s.pop()
    print(s.getMin())

Complexity Analysis:
Time Complexity: O(1) All the operations take constant time.

Space Complexity: O(N) (where N is the total number of calls made for push operation)
As only one value per element is stored in the stack.

'''
class MinStack:
    def __init__(self):
      self.st = []

    def push(self, val: int) -> None:
      if not self.st:
        self.st.append((val, val))
        return
      mini = min(self.getMin(), val)
      self.st.append((val, mini))

    def pop(self) -> None:
      self.st.pop()

    def top(self) -> int:
       return self.st[-1][0]

    def getMin(self) -> int:
       return self.st[-1][1]
    
    