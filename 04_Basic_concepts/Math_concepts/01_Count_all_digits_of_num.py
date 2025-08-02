'''You are given an integer n. You need to return the number of digits in the number.



The number will have no leading zeroes, except when the number is 0 itself.


Examples:
Input: n = 4

Output: 1

Explanation: There is only 1 digit in 4.

Input: n = 14

Output: 2

Explanation: There are 2 digits in 14.

Input: n = 234

Output:
3
Constraints:
0 <= n <= 5000
n will contain no leading zeroes except when it is 0 itself.

Similar Problems
Intuition:
Given a number, all the digits in the number can be counted by counting one by one every digit which can be done by extracting the last digit successively from the right until there are no more digits left to extract.

Approach:
Initialise a counter to keep the count of digits in the number. Keep dividing the number by 10 until no more digits are left to extract.
For every digit extracted from the number, increment the counter by 1.
Once the iterations are over, the number of digits is stored in the counter.
Edge Case:
What if the given number is zero?
Return 1, because the number of digits in zero is 1.


Complexity Analysis:
Time Complexity: O(log10(N)) – In every iteration we are dividing N by 10.

Space Complexity: O(1) – Using a couple of variables i.e., constant space.

class Solution:
    # Function to count all digits in n
    def countDigit(self, n):
        # Edge case
        if n == 0:
            return 1

        # Set counter to 0
        cnt = 0

        # Iterate until n is greater than zero
        while n > 0:
            # Increment count of digits
            cnt = cnt + 1
            n = n // 10

        return cnt

# Input number
n = 6678

# Creating an instance of Solution class
sol = Solution()

# Function call to get count of digits in n
ans = sol.countDigit(n)
print(f"The count of digits in the given number is: {ans}")




'''
class Solution:
    def countDigit(self, n):
        if n==0:
            return 1
        count=0
        while(n>0):
            n = n//10
            count=count+1
        return count
    
    