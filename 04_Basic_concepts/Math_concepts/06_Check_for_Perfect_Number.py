'''You are given an integer n. You need to check if the number is a perfect number or not. Return true if it is a perfect number, otherwise, return false.



A perfect number is a number whose proper divisors (excluding the number itself) add up to the number itself.


Examples:
Input: n = 6

Output: true

Explanation: Proper divisors of 6 are 1, 2, 3.

1 + 2 + 3 = 6.

Input: n = 4

Output: false

Explanation: Proper divisors of 4 are 1, 2.

1 + 2 = 3.

Input: n = 28

Output:
true
Constraints:
1 <= n <= 5000

Intuition:
Given a number, all its proper divisors (divisors that divide the number without leaving any remainder, excluding the number itself) can be found and summed up. Then, the sum can be compared with the number itself. If the sum is the same as the number, then it is a perfect number, otherwise, it is not.

Approach:
Initialize a variable with 0 to store the sum of the proper divisors.
Start iterating from 1 to the given number(excluding) using a loop variable, and check whether the number is divisible completely (leaving the remainder zero) by the loop variable.
If it is divisible completely, the current value of the loop variable is a proper divisor which is added to the sum storing sum of proper divisors.
After the sum is calculated, compare it with the given number. If found equal, the given number is perfect, otherwise, it is not.
Dry Run:
Image 1
Image 2
Image 3
Image 4

1/4



Complexity Analysis:
Time Complexity: O(N) – Running a loop from 1 to N.

Space Complexity: O(1) – Using a couple of variables i.e., constant space, regardless of the size of input.


class Solution:
    # Function to find whether the
    # number is perfect or not
    def isPerfect(self, n):
        
        # Variable to store the sum
        # of all proper divisors
        sum = 0
        
        # Loop from 1 to n
        for i in range(1, n):
            
            # Check if i is a proper divisor
            if n % i == 0:
                # Update sum
                sum = sum + i
        
        # Compare sum and n
        return sum == n

# Input number
n = 6

# Creating an instance of Solution class
sol = Solution()

# Function call to find whether the given number is perfect or not
ans = sol.isPerfect(n)

if ans:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")


'''

class Solution:
    def isPerfect(self, n):
        sum=0
        for i in range(1, n):
            if n % i ==0:
                sum = sum + i
        return sum == n