'''Check if the Number is Armstrong


90

100
Easy
You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.



An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.


Examples:
Input: n = 153

Output: true

Explanation: Number of digits : 3.

13 + 53 + 33 = 1 + 125 + 27 = 153.

Therefore, it is an Armstrong number.

Input: n = 12

Output: false

Explanation: Number of digits : 2.

12 + 22 = 1 + 4 = 5.

Therefore, it is not an Armstrong number.

Input: n = 370

Output:
true
Constraints:
0 <= n <= 109
Intuition:
Given a number, the number of digits can be found. Once the number of digits is known, all the digits can be extracted one by one from the right which can be used to check whether the number is Armstrong or not.

Approach:
Initialize three variables:
count - to store the count of digits in the given number.
sum - to store the sum of the digits of the number raised to the power of the number of digits.
copy - to store the copy of the original number.
Start iterating on the given number till there are digits left to extract. In each iteration, extract the last digit (using the modulus operator with 10), and add the digit raised to the power of count to sum. Update n by integer division with 10 effectively removing the last digit.
After the iterations are over, check if the copy of the original is the same as the sum stored. If found equal, the original number is an Armstrong number, else it is not.
Dry Run:
Image 1
Image 2
Image 3
Image 4
Image 5

1/5


Complexity Analysis:
Time Complexity: O(log10(N)) – N is being divided by 10 until it becomes zero resulting in log10(N) iterations and in each iteration constant time operations are performed.

Space Complexity: O(1) – Using a couple of variables i.e., constant space, regardless of the size of the input.


import math

class Solution:

    """ Function to count the 
    number of digits in N """
    def countDigit(self, n):
        
        # Base case
        if n == 0:
            return 1

        count = int(math.log10(n)) + 1
        return count
    
    """ Function to find whether the
    number is Armstrong or not """
    def isArmstrong(self, n):
        # Store the count of digits
        count = self.countDigit(n)
        
        # Variable to store the sum
        sum = 0
        
        # Variable to store the copy
        copy = n
        
        # Iterate through each
        # digit of the number
        while n > 0:
            
            # Extract the last digit
            lastDigit = n % 10
            
            # Update sum
            sum += pow(lastDigit, count)
            
            # Remove the last digit
            # from the number
            n = n // 10
        
        # Check if the sum of digits raised to the
        # power of k equals the original number
        if sum == copy:
            return True
        return False
        
# Main function
if __name__ == "__main__":
    n = 153
    
    # Creating an instance of 
    # Solution class
    sol = Solution()
    
    # Function call to find whether the
    # given number is Armstrong or not
    ans = sol.isArmstrong(n)
    
    if ans:
        print(f"{n} is an Armstrong number.")
    else:
        print(f"{n} is not an Armstrong number.")



'''
class Solution:
    def isArmstrong(self, n):
        num_str=str(n)
        num_digit=len(num_str)
        sumofpowers= sum(int(digit) ** num_digit for digit in num_str)
        if n == sumofpowers:
            print("True")
        else:
            print("False")
s=Solution()
s.isArmstrong(153)