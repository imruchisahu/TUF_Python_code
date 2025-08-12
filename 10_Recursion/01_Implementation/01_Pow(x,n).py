'''
mplement the power function pow(x, n) , which calculates the x raised to n i.e. xn.


Examples:
Input : x = 2.0000 , n = 10

Output : 1024.0000

Explanation : Answer = 2^10 => 1024.

Input : x = 2.0000 , n = -2

Output : 0.2500

Explanation : Answer = 2^(-2) = 1/4 => 0.25.

Input : x = 2.5000 , n = 2

Output:
6.25
Constraints:
-100.0 <= x <= 100.0
-231 <= n <= 231 - 1
-104 <= xn <= 104
Either x is not zero or n>0.
n is an integer.

#Brute
Initial Approach: Using Inbuilt Function
The simplest way to calculate the power of a number is to use the inbuilt function provided by the programming language. For example, in Python, the pow(x, n) function or the ** operator can be used to compute x raised to the power of n directly. These functions are optimized and handle various edge cases internally, making them a convenient choice for most applications.

Intuition
The goal is to implement a function that computes the power of a number, x raised to n . The core idea involves repeated multiplication of x for n times. To handle both positive and negative exponents, a check for the sign of n is essential. If n is negative, the problem can be transformed by inverting x and making n positive. This approach simplifies the calculation and ensures that the function handles all possible input scenarios effectively.

Approach
Initialize the result variable, ans, to 1. This serves as the base case where any number raised to the power of 0 is 1.
Check if the exponent, n, is less than 0. If true, invert x by setting x to 1/x and make n positive by setting n to -n. This transformation allows the handling of negative exponents.
Use a loop to iterate from 0 to n (converted to an integer). In each iteration, multiply ans by x. This effectively computes x raised to the power of n.
Return the result stored in ans, which now contains the value of x^n.

class Solution:
    def myPow(self, x, n):
        # Base case: any number to the power of 0 is 1
        if n == 0 or x == 1.0:
            return 1
        
        temp = n  # to avoid integer overflow
        
        # Handle negative exponents
        if n < 0:
            x = 1 / x
            temp = -1 * n

        ans = 1

        for i in range(temp):
            # Multiply ans by x for n times
            ans *= x 
        return ans

def main():
    sol = Solution()
    # Output: 1024.0000
    print(f"{sol.myPow(2.0000, 10):.4f}")
    # Output: 0.2500 
    print(f"{sol.myPow(2.0000, -2):.4f}")

if __name__ == "__main__":
    main()
Complexity Analysis
Time Complexity: O(n), where n is the exponent. The loop runs n times to compute the power.

Space Complexity: O(1), as the algorithm uses a constant amount of extra space regardless of the input size.



#Optimal
Real-life Analogy for the Recursive Approach
To understand the recursive approach of solving this problem let us imagine having to measure a large distance by using a single step repeatedly. If the number of steps is even, the task can be split into two equal parts, each requiring half the total steps. If the number of steps is odd, one extra step is needed after completing the even division. This analogy helps in understanding the process of breaking down the problem of computing the power of a number recursively.

Dry Run

Recursive Approach: Step-by-Step Breakdown
Define a helper function that handles the recursive calculation of the power.
Base case: If the exponent n is 0, return 1. This is because any number raised to the power of 0 is 1.
Base case: If the exponent n is 1, return the base x. This is because any number raised to the power of 1 is itself.
Check if the exponent n is even:
If true, recursively calculate the power by squaring the base and halving the exponent.
Example: power(x, n) = power(x * x, n / 2)
Check if the exponent n is odd:
If true, recursively calculate the power by multiplying the base with the result of the power function for n - 1.
Example: power(x, n) = x * power(x, n - 1)
Handle negative exponents by calculating the power for the positive exponent and taking the reciprocal.
Combine these steps in a main function that checks if the exponent is negative and calls the helper function accordingly.


class Solution:
    def power(self, x, n):
        # Base case: anything raised to 0 is 1
        if n == 0:
            return 1.0
        
        # Base case: anything raised to 1 is itself
        if n == 1:
            return x
        
        # If 'n' is even
        if n % 2 == 0:
            # Recursive call: x * x, n // 2
            return self.power(x * x, n // 2)
        
        # If 'n' is odd
        # Recursive call: x * power(x, n - 1)
        return x * self.power(x, n - 1)

    def myPow(self, x, n):
        # If 'n' is negative
        if n < 0:
            # Calculate the power of -n and take reciprocal
            return 1.0 / self.power(x, -n)
        
        # If 'n' is non-negative
        return self.power(x, n)

# Example usage
sol = Solution()
x = 2.0
n = 10

# Calculate x raised to n
result = sol.myPow(x, n)

# Print the result
print(f"{x}^{n} = {result}")
Complexity Analysis
Time Complexity : The time complexity is O(log N) due to the halving of n in the even case and linear reduction in the odd case.

Space Complexity :The space complexity is O(log n) because of the recursive call stack depth.

'''
class Solution:    
    def power(self, x, n):
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n % 2 == 0:
            return self.power(x * x, n // 2)
        return x * self.power(x, n - 1)

    def myPow(self, x, n):
        if n < 0:
            return 1.0 / self.power(x, -n)
        return self.power(x, n)
