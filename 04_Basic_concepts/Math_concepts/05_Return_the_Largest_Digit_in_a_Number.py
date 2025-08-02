'''You are given an integer n. Return the largest digit present in the number.


Examples:
Input: n = 25

Output: 5

Explanation: The largest digit in 25 is 5.

Input: n = 99

Output: 9

Explanation: The largest digit in 99 is 9.

Input: n = 1

Output:
1
Constraints:
0 <= n <= 5000
n will contain no leading zeroes except when it is 0 itself.

Similar Problems
Intuition:
Given a number, all the digits can be extracted from the back (right) successively and the maximum of all the digits can be found by comparing every digit.

Approach:
Initialize a variable largest digit with zero that will store the largest digit in the given number.
The last digit of the original number can be found by using the modulus operator (used to find the remainder for any division) with the number 10.
Iterate on the original number till there are digits left. In every iteration, extract the last (rightmost) digit and check if it is greater than the largest digit. If found greater, update the largest digit with the current digit.
Once the iterations are over, the largest digit in the given number is returned as answer.
Dry Run:
Image 1
Image 2
Image 3
Image 4
Image 5

1/5



Complexity Analysis:
Time Complexity: O(log10(N)) – In every iteration, N is divided by 10 (equivalent to the number of digits in N.)

Space Complexity: O(1) – Using a couple of variables i.e., constant space.

class Solution:
    # Function to find the largest
    # digit in a given number
    def largestDigit(self, n):
        # Variable to store the largest digit
        largestDigit = 0

        # Keep on iterating while there
        # are digits left to extract
        while n > 0:
            lastDigit = n % 10

            # If the current digit is greater than 
            # largest digit, update largest digit
            if lastDigit > largestDigit:
                largestDigit = lastDigit

            n = n // 10

        # Return the largest digit
        return largestDigit

if __name__ == "__main__":
    n = 348

    # Creating an instance of 
    # Solution class
    sol = Solution()

    # Function call to find the largest digit in n
    ans = sol.largestDigit(n)

    print("The largest digit in the number is:", ans)




'''
class Solution:
    # Function to find the largest
    # digit in a given number
    def largestDigit(self, n):
        # Variable to store the largest digit
        largestDigit = 0

        # Keep on iterating while there
        # are digits left to extract
        while n > 0:
            lastDigit = n % 10

            # If the current digit is greater than 
            # largest digit, update largest digit
            if lastDigit > largestDigit:
                largestDigit = lastDigit

            n = n // 10

        # Return the largest digit
        return largestDigit

if __name__ == "__main__":
    n = 348

    # Creating an instance of 
    # Solution class
    sol = Solution()

    # Function call to find the largest digit in n
    ans = sol.largestDigit(n)

    print("The largest digit in the number is:", ans)
