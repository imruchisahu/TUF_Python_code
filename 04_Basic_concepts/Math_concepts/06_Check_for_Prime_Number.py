'''You are given an integer n. You need to check if the number is prime or not. Return true if it is a prime number, otherwise return false.



A prime number is a number which has no divisors except 1 and itself.


Examples:
Input: n = 5

Output: true

Explanation: The only divisors of 5 are 1 and 5 , So the number 5 is prime.

Input: n = 8

Output: false

Explanation: The divisors of 8 are 1, 2, 4, 8, thus it is not a prime number.

Input: n = 9

Output:
false
Constraints:
1 <= n <= 5000

Similar Problems

Intuition:
A prime number is defined as a number that is divisible only by 1 and itself. To determine whether a given number is prime, one can check if it is divisible by any integer between 2 and the number minus one. If it is divisible by any such number, then it is not a prime number.

Approach:
Check if the given number is less than 2; if yes, return false (not prime).
Loop through all numbers from 2 to one less than the given number.
For each number in the loop, check if it divides the given number exactly.
If a divisor is found, return false (not prime).
If no divisor is found after the loop, return true (the number is prime).
Edge Case:
The prime numbers start from 2. Thus, if a number is less than 2, it can be directly said as non-prime.


Complexity Analysis:
Time Complexity: O(N) – Looping N times to find the count of all divisors of N.

Space Complexity: O(1) – Using a couple of variables i.e., constant space.

class Solution:
    # Function to find whether the
    # number is prime or not
    def isPrime(self, n):
        # Edge case
        if n < 2:
            return False

        # Loop from 2 to n-1
        for i in range(2, n):

            # Check if i is a divisor
            if n % i == 0:
                return False

        # Return true as the number is prime
        return True

if __name__ == "__main__":
    n = 5

    # Creating an instance of 
    # Solution class
    sol = Solution()

    # Function call to find whether the
    # given number is prime or not
    ans = sol.isPrime(n)

    if ans:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")



'''
class Solution:
    def isPrime(self, n):
        #your code goes here
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True