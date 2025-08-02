'''You are given an integer n. Return the value of n! or n factorial.



Factorial of a number is the product of all positive integers less than or equal to that number.


Examples:
Input: n = 2

Output: 2

Explanation: 2! = 1 * 2 = 2.

Input: n = 0

Output: 1

Explanation: 0! is defined as 1.

Input: 3

Output:
6
Constraints:
0 <= n <= 10

Similar Problems
Intuition:
Given a number, its factorial can be found by multiplying all positive integers starting from 1 to the given number.

Approach:
Initialize a variable with 1 that will store the factorial of the given number.
Start iterating from 1 to the given number, and in every pass multiply the variable with the current number.
After the iterations are completed, the variable storing the answer can be returned.
Dry Run:
Image 1
Image 2
Image 3
Image 4

1/4



Complexity Analysis:
Time Complexity: O(N) – Iterating once from 1 to N.

Space Complexity: O(1) – Using a couple of variables i.e., constant space.


class Solution:
    
    # Function to find the
    # factorial of a number
    def factorial(self, n):
        # Variable to store the factorial
        fact = 1

        # Iterate from 1 to n
        for i in range(1, n + 1):
            # Multiply fact with current number
            fact = fact * i
        
        # Return the factorial stored
        return fact

# Input number
n = 4

# Creating an instance of Solution class
sol = Solution()

# Function call to find the factorial of n
ans = sol.factorial(n)

print("The factorial of given number is: ", ans)



'''
class Solution:
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)