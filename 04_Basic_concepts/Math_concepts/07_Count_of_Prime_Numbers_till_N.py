'''You are given an integer n. You need to find out the number of prime numbers in the range [1, n] (inclusive). Return the number of prime numbers in the range.



A prime number is a number which has no divisors except, 1 and itself.


Examples:
Input: n = 6

Output: 3

Explanation: Prime numbers in the range [1, 6] are 2, 3, 5.

Input: n = 10

Output: 4

Explanation: Prime numbers in the range [1, 10] are 2, 3, 5, 7.

Input: n = 20

Output:
8
Constraints:
2 <= n <= 1000

Similar Problems

Intuition:
A naive approach to count prime numbers till N, is to check every number starting from 1 till N for prime. Keep a counter to store the count. If the number is prime, increment the counter. Once all the numbers are checked, the counter stores the required count.

Approach:
Initialize a counter to store the count of prime numbers.
Iterate from 2 to n, and check the current value for prime (using the brute way). If found prime, increment the counter by 1.
After the iterations are over, the counter stores the required result.
Dry Run:
Image 1
Image 2
Image 3
Image 4
Image 5
Image 6

1/6



Complexity Analysis:
Time Complexity: O(N2) – Checking all numbers from 1 to n for prime and checking if a number is prime or not will take O(n) TC.

Space Complexity: O(1) – Using a couple of variables i.e., constant space.

class Solution:
    # Function to find whether the
    # number is prime or not
    def isPrime(self, n):
        
        # Variable to store the 
        # count of divisors of n
        count = 0
        
        # Loop from 1 to n
        for i in range(1, n + 1):
            
            # Check if i is a divisor
            if n % i == 0:
                # Increment count
                count = count + 1
        
        # If count is 2, n is prime
        if count == 2:
            return True
        # Else not prime
        return False
    
    # Function to find count
    # of primes till n
    def primeUptoN(self, n):
        
        # Variable to store count
        count = 0
        
        # Iterate from 1 to n
        for i in range(2, n + 1):
            
            # Check if i is prime
            if self.isPrime(i):
                count += 1
        
        # Return the count
        return count

# Input number
n = 6

# Creating an instance of Solution class
sol = Solution()

# Function call to get count of all primes till n
ans = sol.primeUptoN(n)

print("The count of primes till", n, "is:", ans)



'''
class Solution:
    def primeUptoN(self, n):
        if n < 2:
            return 0

        count = 0
        for num in range(2, n + 1):
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                count += 1
        return count