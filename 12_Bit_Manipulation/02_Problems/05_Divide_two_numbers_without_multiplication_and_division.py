'''
Given the two integers, dividend and divisor. Divide without using the mod, division, or multiplication operators and return the quotient.



The fractional portion of the integer division should be lost as it truncates toward zero.

As an illustration, 8.345 and -2.7335 would be reduced to 8 and -2 respectively.



Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.


Examples:
Input : Dividend = 10 , Divisor = 3

Output : 3

Explanation : 10/3 = 3.33 , truncated to 3.

Input : Dividend = 7 , Divisor = -3

Output : -2

Explanation : 7/-3 = -2.33 , truncated to -2.

Input : Dividend = 7 , Divisor = 2

Output:
3
Constraints:
-231 <= dividend , divisor <= 231 - 1
divisor != 0

#Brute
Intuition:
The brute force way to solve this problem is to repeatedly add the divisor until the sum is smaller than the dividend.
Approach:
Check the signs of the dividend and the divisor to determine if the result should be positive or negative. If one is positive and the other is negative, the result is negative. Otherwise, it is positive.
Work with the absolute values of the dividend and the divisor to simplify the calculations.
Use a loop to repeatedly add the divisor to the sum until the sum does not become greater than the dividend.
Within the loop, increment the result storing the quotient and update the sum.
If the result exceeds the maximum or minimum values for an integer, clamp it to the respective limit, handling the overflow cases.
Adjust the sign of the result based on the initial sign determination and return it.
Edge Cases:
What if the divisor and dividend are identical?
To save the computation, directly 1 can be returned.
What if the dividend is INT_MIN and divisor is -1?
This may lead to overflow as the result is outside the range of int. Hence, we can return INT_MAX in such a case.
What if the divisor is 1?
The result is the dividend itself.

class Solution:
    #Function to divide two numbers without multiplication and division 
    def divide(self, dividend, divisor):
        
        # Base case
        if dividend == divisor:
            return 1
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if divisor == 1:
            return dividend
        
        # Variable to store the sign of result
        isPositive = True
        
        # Updating the sign of quotient
        if dividend >= 0 and divisor < 0:
            isPositive = False
        elif dividend < 0 and divisor > 0:
            isPositive = False
            
        # Storing absolute dividend & divisor
        n = abs(dividend)
        d = abs(divisor)
        
        # Variable to store the answer and sum
        ans = 0
        sum_ = 0
        
        #Looping while sum added to divisor is less than or equal to divisor 
        while sum_ + d <= n:
            
            # Increment the count
            ans += 1
            # Update the sum
            sum_ += d
        
        # Handling overflowing condition
        if ans > 2**31 - 1 and isPositive:
            return 2**31 - 1
        if ans > 2**31 - 1 and not isPositive:
            return -2**31
        
        #Returning the quotient with proper sign 
        return ans if isPositive else -1 * ans

# Driver code
if __name__ == "__main__":
    dividend = 10
    divisor = 3
    
    #Creating an instance of Solution class 
    sol = Solution()
    
    #Function call to divide two numbers without multiplication and division 
    ans = sol.divide(dividend, divisor)
    
    print(f"The result of dividing {dividend} and {divisor} is {ans}")
Complexity Analysis:
Time Complexity: O(dividend)
In the worst case when the divisor is 1, the number of iterations taken will be O(dividend).

Space Complexity: O(1) Using a couple of variables i.e., constant space.



#optimal
Intuition:
The key idea is to repeatedly subtract the divisor from the dividend until the dividend is smaller than the divisor. However, doing this one step at a time can be very slow, so we use a method that speeds up the process by leveraging bit manipulation.

An important concept to know is that the quotient can be expressed as the sum of powers of 2.

Example: Dividend = 10, Divisor = 3.
Quotient = 10/3 = 3 which can be represented as 21 + 20.

Now, instead of subtracting the divisor from the dividend one unit at a time, we use powers of 2 (using bit shifting) to subtract larger multiples of the divisors in each step. This makes the process faster.

Approach:
Check the signs of the dividend and the divisor to determine if the result should be positive or negative. If one is positive and the other is negative, the result is negative. Otherwise, it is positive.
Work with the absolute values of the dividend and the divisor to simplify the calculations.
Use a loop to repeatedly subtract the divisor from the dividend. Instead of subtracting the divisor one at a time, shift the divisor left (equivalent to multiplying by powers of 2) to subtract larger chunks, making the process faster.
Within the loop, find the maximum power of two such that the shifted divisor is still less than or equal to the remaining part of the dividend. Subtract this value from the dividend and add the corresponding power of two to the result.
If the result exceeds the maximum or minimum values for an integer, clamp it to the respective limit, handling the overflow cases
Adjust the sign of the result based on the initial sign determination and return it.
Edge Cases:
What if the divisor and dividend are identical?
To save the computation, directly 1 can be returned.
What if the dividend is INT_MIN and divisor is -1?
This may lead to overflow as the result is outside the range of int. Hence, we can return INT_MAX in such a case.
What if the divisor is 1?
The result is the dividend itself.



class Solution:
    #Function to divide two numbers without multiplication and division 
    def divide(self, dividend, divisor):
        
        # Edge cases
        if dividend == divisor:
            return 1
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if divisor == 1:
            return dividend
        
        # Variable to store the sign of result
        isPositive = True
        
        # Updating the sign of quotient
        if dividend >= 0 and divisor < 0:
            isPositive = False
        elif dividend <= 0 and divisor > 0:
            isPositive = False
            
        # Storing absolute dividend & divisor
        n = abs(dividend)
        d = abs(divisor)
        
        # Variable to store the answer
        ans = 0
        
        #Looping while dividend is greater than equal to divisor 
        while n >= d:
            count = 0
            
            #Finding the required largest power of 2 
            while n >= (d << (count + 1)):
                count += 1
            
            # Updating the answer & dividend
            ans += (1 << count)
            n -= (d << count)
        
        # Handling overflowing condition
        if ans == (1 << 31) and isPositive:
            return 2**31 - 1
        if ans == (1 << 31) and not isPositive:
            return -2**31
        
        # Returning the quotient with proper sign 
        return ans if isPositive else -1 * ans

# Driver code
if __name__ == "__main__":
    dividend = 10
    divisor = 3
    
    #Creating an instance of Solution class
    sol = Solution()
    
    #Function call to divide two numbers without multiplication and division
    ans = sol.divide(dividend, divisor)
    
    print(f"The result of dividing {dividend} and {divisor} is {ans}")
Complexity Analysis:
Time Complexity: O((logN)2) – (where N is the absolute value of dividend)

The outer loop runs for O(logN) times.
The inner loop runs for O(logN) (approx.) times as well.
Space Complexity: O(1) – Using a couple of variables i.e., constant space.


'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if divisor == 1:
            return dividend
    
        isPositive = True
        if dividend >= 0 and divisor < 0:
            isPositive = False
        elif dividend <= 0 and divisor > 0:
            isPositive = False
        n = abs(dividend)
        d = abs(divisor)
        
        ans = 0
        while n >= d:
            count = 0
            while n >= (d << (count + 1)):
                count += 1
            ans += (1 << count)
            n -= (d << count)

        if ans == (1 << 31) and isPositive:
            return 2**31 - 1
        if ans == (1 << 31) and not isPositive:
            return -2**31
        return ans if isPositive else -1 * ans