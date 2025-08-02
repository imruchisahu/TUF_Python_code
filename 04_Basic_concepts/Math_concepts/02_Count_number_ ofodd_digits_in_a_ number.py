'''Count number of odd digits in a number


68

100
Easy
You are given an integer n. You need to return the number of odd digits present in the number.



The number will have no leading zeroes, except when the number is 0 itself.


Examples:
Input: n = 5

Output: 1

Explanation: 5 is an odd digit.

Input: n = 25

Output: 1

Explanation: The only odd digit in 25 is 5.

Input: n = 15

Output:
2
Constraints:
0 <= n <= 5000
n will contain no leading zeroes except when it is 0 itself.

Similar Problems

Intuition:
Given a number, all the digits in the number can be extracted one by one from right to left which can be checked for even and odd.

Approach:
The last digit of the given number can be found by using the modulus operator (used to find the remainder for any division) with the number 10.
Iterate on the original number till there are digits left, extract the last (rightmost) digit, and check whether the digit is odd or not. In every iteration, divide the original number by 10 so that the remaining digits can be extracted in the next iterations.
Keep a counter to count the number of odd digits found in the number and every time an odd digit is encountered, increment the counter.
Dry Run:
Image 1
Image 2
Image 3
Image 4
Image 5

1/5

Complexity Analysis:
Time Complexity: O(log10(N)) – In every iteration we are dividing N by 10 (equivalent to the number of digits in N).

Space Complexity: O(1) – Using only couple of variables i.e., constant space.


class Solution:
    # Function to count number
    # of odd digits in N
    def countOddDigit(self, n):
        # Counter to store the 
        # number of odd digits
        oddDigits = 0

        # Iterate till there are digits left
        while n > 0:
            # Extract last digit
            lastDigit = n % 10
            
            # Check if digit is odd
            if lastDigit % 2 != 0:
                # Increment counter
                oddDigits = oddDigits + 1
            n = n // 10

        return oddDigits

# Input number
n = 6678

# Creating an instance of 
# Solution class
sol = Solution()

# Function call to get count of odd digits in n
ans = sol.countOddDigit(n)
print("The count of odd digits in the given number is:", ans)


'''
class Solution:
    def countOddDigit(self, n):
        Odddigit=0
        while n>0:
            ldigit = n%10
        
            if ldigit % 2 != 0:
                Odddigit += 1
            n=n//10
        return Odddigit 
