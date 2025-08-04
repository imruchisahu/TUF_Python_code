'''Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.


Examples:
Input : num = 529

Output : 7

Explanation : In first iteration the digits sum will be = 5 + 2 + 9 => 16

In second iteration the digits sum will be 1 + 6 => 7.

Now single digit is remaining , so we return it.

Input : num = 101

Output : 2

Explanation : In first iteration the digits sum will be = 1 + 0 + 1 => 2

Now single digit is remaining , so we return it.

Input : num = 38

Output:
2
Constraints:
0 <= num <= 231 - 1

Similar Problems

Intution
To solve the problem of finding the sum of digits in a given number using recursion, the approach revolves around breaking down the problem into smaller, manageable parts. The key idea is to isolate the last digit of the number and add it to the result of a recursive call with the remaining digits. This process continues until the number reduces to a single digit. At each step, the last digit can be obtained using the modulus operation, and the rest of the number can be obtained using integer division. This recursive approach ensures that each digit is processed individually and accumulated to form the final sum.

Approach
Base Case: If the number is 0, return 0 as there are no more digits to process.
Recursive Case:
Compute the last digit of the number using number % 10.
Compute the remaining number by performing integer division number / 10.
Make a recursive call with the remaining number and add the last digit to the result of this call.
Dry Run


Complexity Analysis
Time Complexity O(log n) – This is because each recursive call processes a number with fewer digits than the previous call, leading to logarithmic time complexity in terms of the number of digits.

SpaceComplexity O(log n) – This space is required for the recursion stack, which grows with the number of digits in the number.

class Solution:

    # Method to compute the sum of digits of given number
    def addDigits(self, num):
        # Base case: if the number is a single digit, return it
        if num < 10:
            return num

        # Recursive case: sum the digits and continue
        sum_digits = self.sumDigits(num)

        return self.addDigits(sum_digits)
    
    # Helper function to add the sum of digits recursively
    def sumDigits(self, num):
        # Base case: If the number is 0, return 0
        if num == 0:
            return 0

        # Recursive case
        return self.sumDigits(num // 10) + (num % 10)


# Driver code
if __name__ == "__main__":
    solution = Solution()

    # Example number
    num = 529

    # Call the addDigits method and print the result
    result = solution.addDigits(num)
    print("Sum of digits:", result)  

'''
class Solution:
    def addDigits(self, num):
        #your code goes here
        if num < 10:
            return num
        
        sum_of_digits = self.sumDigits(num)
        return self.addDigits(sum_of_digits)

    def sumDigits(self, num):
        if num == 0:
            return 0
        return self.sumDigits(num//10) + (num % 10)