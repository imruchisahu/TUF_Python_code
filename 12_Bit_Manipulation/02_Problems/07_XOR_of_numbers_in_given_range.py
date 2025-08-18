'''Given two integers L and R. Find the XOR of the elements in the range [L , R].


Examples:
Input : L = 3 , R = 5

Output : 2

Explanation : answer = (3 ^ 4 ^ 5) = 2.

Input : L = 1, R = 3

Output : 0

Explanation : answer = (1 ^ 2 ^ 3) = 0.

Input : L = 4, R = 10

Output:
11
Constraints:
1 <= L <= R <= 109

Intuition:
A naive approach to solving this will be XOR for every number in the given range.

Approach:
A variable can be initiated with 0 that will store the XOR of numbers in given range.
Traverse all the numbers in the given range and XOR each number with the variable.
Once the traversal is over, the variable stores the result.
Dry Run:

class Solution:
    
    # Function to find the XOR 
    # of numbers from L to R
    def findRangeXOR(self, l, r):
        
        # To store the XOR of numbers
        ans = 0
        
        # XOR all the numbers
        for i in range(l, r + 1):
            ans ^= i
        
        # Return the result
        return ans

if __name__ == "__main__":
    l, r = 3, 5
    
    # Creating an instance of 
    # Solution class
    sol = Solution()
    
    # Function call to get the
    # XOR of numbers from L to R
    ans = sol.findRangeXOR(l, r)
    
    print(f"The XOR of numbers from {l} to {r} is: {ans}")

Complexity Analysis:
Time Complexity: O(N) Traversing through all the numbers take O(N) time.

Space Complexity: O(1) Using only a couple of variables, i.e., constant space.

'''
class Solution:      
    def XORtillN(self, n):
        if n % 4 == 1:
            return 1
        if n % 4 == 2:
            return n + 1
        if n % 4 == 3:
            return 0
        return n
    def findRangeXOR(self, l, r):
        return self.XORtillN(l - 1) ^ self.XORtillN(r)