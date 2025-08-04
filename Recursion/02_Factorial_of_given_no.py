'''Given an integer n, return the factorial of n.



Factorial of a non-negative integer, is the multiplication of all integers smaller than or equal to n (use 64-bits to return answer).


Examples:
Input : n = 3

Output : 6

Explanation : Factorial = 1 * 2 * 3 => 6

Input : n = 5

Output : 120

Explanation : Factorial = 1 * 2 * 3 * 4 * 5 => 120

Input : n = 4

Output:
24
Constraints:
0 <= n <= 15

Similar Problems
Intuition
Finding the factorial of a number N using recursion involves visualizing the process of multiplying the number by each smaller positive integer down to 1. The approach is to repeatedly call the function, reducing the number by 1 each time. This continues until reaching the base case of 1. Imagine the factorial as a series of multiplications: starting with N, then multiplying by N-1, then by N-2, and so on, until multiplying by 1.

Approach
Define a function that calculates the factorial of a number.
In the function, if the number is 0 or 1, return 1 (base case).
Otherwise, return the number multiplied by the factorial of the number minus 1 (recursive case).


Solution

Complexity Analysis
Time Complexity O(N) — The function makes N recursive calls to reach the base case, so the time complexity is proportional to the number of recursive calls

Space Complexity O(N) — The call stack grows with each recursive call, using N stack frames, so the space complexity is proportional to the depth of recursion.

Note : For very large numbers, recursion can lead to a stack overflow due to too many nested function calls.
class Solution:
    def factorial(self, n):
        # Base case: factorial of 0 or 1 is 1
        if n<= 1:
            return 1
        # Recursive case: n * factorial of n-1
        return n* self.factorial(n- 1)

if __name__ == "__main__":
    solution = Solution()
    N = 5 # Example input
    print(f"Factorial of {N} is {solution.factorial(N)}")

'''
class Solution:
    def factorial(self, n):
        #Your code goes here
        if n<=1:
            return 1
        else:
            return n * self.factorial(n-1)