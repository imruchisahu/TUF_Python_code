'''You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.



The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.


Examples:
Input: n1 = 4, n2 = 6

Output: 2

Explanation: Divisors of n1 = 1, 2, 4, Divisors of n2 = 1, 2, 3, 6

Greatest Common divisor = 2.

Input: n1 = 9, n2 = 8

Output: 1

Explanation: Divisors of n1 = 1, 3, 9 Divisors of n2 = 1, 2, 4, 8.

Greatest Common divisor = 1.

Input: n1 = 6, n2 = 12

Output:
6
Constraints:
1 <= n1, n2 <= 1000

Similar Problems
Intuition:
The GCD (Greatest Common Divisor), also known as HCF (Highest Common Factor), of two numbers is the largest number that divides both without leaving a remainder. To find the GCD, check all numbers from 1 up to the smaller of the two input numbers for common factors. The largest of these common factors is the GCD.

Approach:
Initialize a variable gcd with 1 that will store the greatest common divisor of the two given numbers.
Iterate from 1 to the minimum of the two numbers using a loop variable. Update the gcd if both the given numbers are divisible by the current value of the loop variable.
After the iterations are over, the greatest common divisor will be stored in the gcd variable.
Dry Run:
Image 1
Image 2
Image 3
Image 4
Image 5

1/5



Complexity Analysis:
Time Complexity: O(min(N1, N2)) – where N1 and N2 are given numbers. Iterating from 1 to min(N1, N2) and performing constant time operations in each iteration.

Space Complexity: O(1) – Using a couple of variables i.e., constant space.


class Solution:
    # Function to find the
    # GCD of two numbers
    def GCD(self, n1, n2):
        
        # Variable to store the gcd
        gcd = 1
        
        # Iterate from 1 to min(n1, n2)
        for i in range(1, min(n1, n2) + 1):
            
            # Check if i is a common
            # divisor of both n1 and n2
            if n1 % i == 0 and n2 % i == 0:
                
                # Update gcd
                gcd = i
        
        # Return stored GCD.
        return gcd

# Input numbers
n1 = 4
n2 = 6

# Creating an instance of 
# Solution class
sol = Solution()

# Function call to find the
# gcd of two numbers
ans = sol.GCD(n1, n2)

print(f"GCD of {n1} and {n2} is: {ans}")

'''
class Solution:
    def GCD(self, n1, n2):
        gcd = 1
        for i in range(1, min(n1, n2) + 1):
            if n1 % i == 0 and n2 % i == 0:
                gcd = i
        return gcd