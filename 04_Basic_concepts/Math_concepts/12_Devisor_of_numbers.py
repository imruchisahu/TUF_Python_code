'''You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.



A number which completely divides another number is called it's divisor.


Examples:
Input: n = 6

Output = [1, 2, 3, 6]

Explanation: The divisors of 6 are 1, 2, 3, 6.

Input: n = 8

Output: [1, 2, 4, 8]

Explanation: The divisors of 8 are 1, 2, 4, 8.

Input: n = 7

Output:
[1, 7]
Constraints:
1 <= n <= 1000

Similar Problems

Intuition:
Given a number n, a brute force approach would be to iterate from 1 to n checking each value if it divides n without leaving a remainder. For each divisor found, store it in a list and return the result.

Approach:
Initialize an array/list to store the divisors.
Iterate from 1 to n, and check if the current value is a divisor of n or not. Add the value to the array/list if it is a divisor.
The array/list stores all the divisors of n.
Dry Run:
Image 1
Image 2
Image 3
Image 4
Image 5
Image 6

1/6



Complexity Analysis:
Time Complexity: O(N) – Iterating N times, and performing constant time operations in each pass.

Space Complexity: O(sqrt(N)) – A number N can have at max 2*sqrt(N) divisors, which are stored in the array.

class Solution:
    # Function to find all
    # divisors of n
    def divisors(self, n):
        
        # To store the divisors
        ans = []
        
        # Iterate from 1 to n
        for i in range(1, n + 1):
            
            # If a divisor is found
            if n % i == 0:
                # Add it to the answer
                ans.append(i)
        
        # Return the result
        return ans

# Input number
n = 6

# Creating an instance of 
# Solution class
sol = Solution()

# Function call to find 
# all divisors of n
ans = sol.divisors(n)

print(f"The divisors of {n} are: ", end="")
for i in range(len(ans)):
    print(ans[i], end=" ")

'''

class Solution:
    def divisors(self, n):
        res = []
        for i in range(1, n+1):
            if n%i == 0 :
                res.append(i)
        return res