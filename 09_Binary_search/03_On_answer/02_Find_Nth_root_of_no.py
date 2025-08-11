'''
Given two numbers N and M, find the Nth root of M. The Nth root of a number M is defined as a number X such that when X is raised to the power of N, it equals M. If the Nth root is not an integer, return -1.


Examples:
Input: N = 3, M = 27

Output: 3

Explanation: The cube root of 27 is equal to 3.

Input: N = 4, M = 69

Output:-1

Explanation: The 4th root of 69 does not exist. So, the answer is -1.

Input: N = 4, M = 81

Output:
3
Constraints:
  1 <= N <= 30
  1 <= M <= 109

  #Linear Search
  Intuition:
Perform a simple linear search in range [1,M]. Calculate the value of x raised to the power N for every number x in this range. If it is equal to the given number then, x is the Nth root of the number. If no such number(x) exists, return -1 as an answer.

Approach:
Working of nthRoot(N, M):

Iterate from 1 to M(given number) using a for loop. Calculate the value of x raised to the power n as follows:
Start with the result as 1 and keep track of the base value.
If the exponent is odd, multiply the result by the base and reduce the exponent by one.
If the exponent is even, square the base and half the exponent.
Continue the process until the exponent becomes zero, and the final result is returned.
If the result is equal to M, this means x is the Nth root of M. So, return x from this step.
If the calculated value is smaller than M, then continue to next iteration.
If the calculated value is greater than M, this means we have got a bigger number than our answer and until now we have not found any number that can be our answer. In this case, our answer does not exist and break out from this step and return -1.
Code:
Cpp
Java
Python
Javascript
C#
Go


class Solution:
    """ Function to calculate power using
    exponentiation by squaring method"""
    def Pow(self, b, exp):
        ans = 1
        base = b
        
        # Exponentiation by squaring method
        while exp > 0:
            if exp % 2 == 1:
                exp -= 1
                ans *= base
            else:
                exp //= 2
                base *= base
        return ans

    """ Function to find the nth root
    root of m using linear search"""
    def NthRoot(self, N: int, M: int) -> int:
        # Linear search on the answer space
        for i in range(1, M + 1):
            val = self.Pow(i, N)

            """ Check if the computed
            value is equal to M"""
            if val == M:
                # Return the root value
                return i
            elif val > M:
                break
        # Return -1 if no root found
        return -1

# Driver code
if __name__ == "__main__":
    n, m = 3, 27
    
    # Create an object of the Solution class
    sol = Solution()
    
    ans = sol.NthRoot(n, m)
    
    # Print the result
    print(f"The answer is: {ans}")
Complexity Analysis:
Time Complexity: O(N*logN)
The for loop runs takes O(M) time and calculating Pow(x, N) takes O(logN) time. However, since the for loop breaks as soon as the result of Pow(x, N) becomes greater than the M, thus, the for loops actually runs only for N iterations making overall complexity as O(N*logN).

Space Complexity: O(1), as there are only a couple of variables used.



#Binary Search
Intuition:
The idea here is to use binary search to optimize the solution. Although the traditional application of binary search involves a sorted array, upon closer observation, one can notice that the search space for the answer here ranges from 1 to M, which inherently forms a sorted sequence. So, binary search can be applied.

Approach:
Need of a helper function to find the exponent of the number: If the given numbers M and N are big enough, the value of midN can not be stored in a variable. So to resolve this problem, implement a helper function.
Working of nthRoot(N, M):
Place the 2 pointers, low and high: Initially, place the low pointer at 1 and the high will point to M.
Inside the while loop, which run till low is less than or equal to high, calculate the value of ‘mid’ .
Eliminate the halves accordingly:
If helper function returns 1: We can conclude that the number ‘mid’ is our answer. So, return ‘mid’.
If helper function returns 0: It can be concluded that the number ‘mid’ is smaller than our answer. So, eliminate the left half and consider the right half(i.e. low = mid+1).
If helper function returns 2: The value mid is larger than the number we want. This means the numbers greater than ‘mid’ will not be our answers and the right half of ‘mid’ consists of such numbers. So, eliminate the right half and consider the left half(i.e. high = mid-1).
Finally, no answer is found from the loop, this means no answer exists. So, we will return -1.

Working of func(mid, n, m):
First declare a variable ‘ans’ to store the value midn. Now, use Exponentiation by Squaring method to find the result.
Inside the while loop, if at any point ‘ans’ becomes greater than M, return 2.
Once the loop is completed, if the ‘ans’ is equal to M, return 1.
If the value is smaller, return 0.
Dry Run:
Image 1
Image 2
Image 3
Image 4
Image 5

1/5



Code:
Cpp
Java
Python
Javascript
C#
Go


class Solution:
    # Helper function to check mid^N compared to M
    def helperFunc(self, mid, n, m):
        ans, base = 1, mid

        while n > 0:
            if n % 2 == 1:
                ans *= base
                if ans > m:
                    return 2  # Early exit
                n -= 1
            else:
                n //= 2
                base *= base
                if base > m:
                    return 2
        
        if ans == m:
            return 1
        return 0

    # Function to find the Nth root of M using Binary Search
    def NthRoot(self, N, M):
        low, high = 1, M
        
        while low <= high:
            mid = (low + high) // 2
            midN = self.helperFunc(mid, N, M)
            
            if midN == 1:
                return mid  # Found exact root
            elif midN == 0:
                low = mid + 1  # Move right
            else:
                high = mid - 1  # Move left
        
        return -1  # No integer root found

# Test case
n, m = 3, 27
sol = Solution()
ans = sol.NthRoot(n, m)
print("The answer is:", ans)
Complexity Analysis:
Time Complexity: O(logM * logN)
The binary search on the search space (of size M) takes O(logM) and the helper function takes O(logN) taking overall O(logM * logN).

Space Complexity: O(1), as there are only a couple of variables used.

  '''
class Solution:
    def helperFunc(self, mid, n, m):
        ans, base = 1, mid
        while n > 0:
            if n%2 == 1:
                ans *= base
                if ans > m:
                    return 2
                n -= 1
            else:
                n //= 2
                base *= base
                if base > m:
                    return 2
        if ans == m:
            return 1
        return 0

    def NthRoot(self, n, m):
        low, high = 1, m
        while low <= high:
            mid = (low + high) // 2
            midN = self.helperFunc(mid, n, m)
            if midN ==  1:
                return mid
            elif midN == 0:
                low = mid + 1
            else:
                high = mid - 1
        return -1
