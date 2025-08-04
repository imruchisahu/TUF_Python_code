'''The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,



F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.


Given n, calculate F(n).


Examples:
Input : n = 2

Output : 1

Explanation : F(2) = F(1) + F(0) => 1 + 0 => 1.

Input : n = 3

Output : 2

Explanation : F(3) = F(2) + F(1) => 1 + 1 => 2.

Input : n = 6

Output:
8
Constraints:
0 <= n <= 20

Similar Problems
Intuition
This problem can be broken into smaller problems using recursion by calculating Fibonacci numbers for previous positions and combining these results to find the Fibonacci number for the desired position . To find the Fibonacci number at a certain position, start with two base cases: F(0) = 0 and F(1) = 1. For any position greater than 1, the Fibonacci number can be found by adding the two preceding Fibonacci numbers: F(n) = F(n-1) + F(n-2).

Approach
Define a recursive function that returns 0 if n is 0, and 1 if n is 1 (base cases).
For n > 1, return the sum of the Fibonacci numbers for n-1 and n-2 (recursive case).
Call the function with the desired n to get the Fibonacci number.
Dry Run


Complexity Analysis
Time Complexity O(2^N) — Each function call makes two more calls (for n-1 and n-2), resulting in an exponential growth in the number of calls.

Space Complexity O(N)— The call stack grows with each recursive call, using N stack frames, so the space complexity is proportional to the recursion depth.

class Solution:
    def fib(self, n):
        # Base cases: F(0) = 0, F(1) = 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        # Recursive case: F(n) = F(n-1) + F(n-2)
        return self.fib(n - 1) + self.fib(n - 2)

if __name__ == "__main__":
    solution = Solution()
    n = 5  # Example input
    print(f"Fibonacci number at position {n} is {solution.fibonacci(n)}")


'''
class Solution:
    def fib(self, n):
        #your code goes here
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)