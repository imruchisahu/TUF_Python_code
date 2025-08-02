'''Palindrome Number



You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.



A palindrome number is a number which reads the same both left to right and right to left.


Examples:
Input: n = 121

Output: true

Explanation: When read from left to right : 121.

When read from right to left : 121.

Input: n = 123

Output: false

Explanation: When read from left to right : 123.

When read from right to left : 321.

Input: 101

Output:
true
Constraints:
0 <= n <= 5000
n will contain no leading zeroes except when it is 0 itself.

Similar Problems
Intuition:
Given a number, it is a palindrome if it remains the same when its digits are reversed.

Approach:
Initialize a reversed number with zero, which will store the reversed number. Store a copy of the original number which can be used to compare the original number and reversed number.
To push any digit at the end of the reversed number, the following mathematical operation can be used: revNum = (revNum * 10) + digit.
The last digit of the original number can be found by using the modulus operator (used to find the remainder for any division) with the number 10.
Iterate on the original number till there are digits left. In every iteration, extract the last (rightmost) digit and push it at the back of the reversed number. Also, divide the original number by 10 so that the remaining digits can be extracted in the next iterations.
Once the iterations are over, the reversed number will be stored in the reverse of the original number. Check if the stored copy of the original number is the same as the reversed number. If yes, the number is palindrome else it is not a palindrome.
Dry Run:
Image 1
Image 2
Image 3
Image 4
Image 5


Complexity Analysis:
Time Complexity: O(log10(N)) – In every iteration, N is divided by 10 (equivalent to the number of digits in N.)

Space Complexity: O(1) – Using a couple of variables i.e., constant space.

class Solution:
    # Function to check if a 
    # number is palindrome or not
    def isPalindrome(self, n):
        # Create a copy of original number
        copy = n
        
        # After the code, revNum will
        # contain the reversed number
        revNum = 0

        # Keep on iterating while there
        # are digits left to extract
        while n > 0:
            lastDigit = n % 10

            # Pushing last digit at the
            # back of reversed number
            revNum = (revNum * 10) + lastDigit
            n = n // 10
        
        # Return true if the reversed and 
        # copy of original number is same
        return revNum == copy

# Input number
n = 12321

# Creating an instance of Solution class
sol = Solution()

# Function call to check if n is a palindrome
ans = sol.isPalindrome(n)

if ans:
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")




'''
class Solution:
    def isPalindrome(self, n):
        c = n
        revnum=0
        while n>0:
            lastDigit = n%10
            revnum = (revnum * 10) + lastDigit
            n= n //10
        return revnum == c
    