'''You are given an integer n. Return the integer formed by placing the digits of n in reverse order.


Examples:
Input: n = 25

Output: 52

Explanation: Reverse of 25 is 52.

Input: n = 123

Output: 321

Explanation: Reverse of 123 is 321.

Input: n = 54

Output:
45
Constraints:
0 <= n <= 5000
n will contain no leading zeroes except when it is 0 itself.

Similar Problems
Intuition:
Given a number, it can be reversed if all the digits are extracted from the end of the original number and pushed at the back of a new reversed number.

Approach:
Initialize a reversed number with zero, which will store the reversed number. To push any digit at the end of the reversed number, the following mathematical operation can be used:
revNum = (revNum * 10) + digit.
The last digit of the original number can be found by using the modulus operator (used to find the remainder for any division) with the number 10.
Iterate on the original number till there are digits left. In every iteration, extract the last (rightmost) digit and push it at the back of the reversed number. Also, divide the original number by 10 so that the remaining digits can be extracted in the next iterations.
Once the iterations are over, the reversed number will be stored in the reverse of the original number.


Complexity Analysis:
Time Complexity: O(log10(N)) – In every iteration, N is divided by 10 (equivalent to the number of digits in N.)

Space Complexity: O(1) – Using a couple of variables i.e., constant space.
class Solution:
    # Function to reverse given number n
    def reverseNumber(self, n):
        """ After the code, revNum will
        contain the reversed number """
        revNum = 0
        
        """ Keep on iterating while there
        are digits left to extract """
        while n > 0:
            lastDigit = n % 10
            
            """ Pushing last digit at the
            back of reversed number """
            revNum = (revNum * 10) + lastDigit
            n = n // 10
        
        return revNum

if __name__ == "__main__":
    n = 6678
    
    """ Creating an instance of 
    Solution class """
    sol = Solution()
    
    # Function call to reverse the digits in n
    ans = sol.reverseNumber(n)
    print("The reverse of given number is:", ans)




'''

class Solution:
    def reverseNumber(self, n):
        n=str(n)
        return (int(n[::-1]))