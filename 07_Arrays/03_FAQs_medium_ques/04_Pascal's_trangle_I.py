'''Given two integers r and c, return the value at the rth row and cth column (1-indexed) in a Pascal's Triangle.



In Pascal's triangle:

The first row contains a single element 1.
Each row has one more element than the previous row.
Every row starts and ends with 1.


For all interior elements (i.e., not at the ends), the value at position (r, c) is computed as the sum of the two elements directly above it from the previous row:

Pascal[r][c]=Pascal[r−1][c−1]+Pascal[r−1][c]
where indexing is 1-based

Examples:
Input: r = 4, c = 2

Output: 3

Explanation: The Pascal's Triangle is as follows:

1

1 1

1 2 1

1 3 3 1

....

Thus, value at row 4 and column 2 = 3

Input: r = 5, c = 3

Output: 6

Explanation: The Pascal's Triangle is as follows:

1

1 1

1 2 1

1 3 3 1

1 4 6 4 1

....

Thus, value at row 5 and column 3 = 6

Input: r = 6, c = 2

Output:
5
Constraints:
1 <= r, c <= 30
c <= r
All values will fit inside a 32-bit integer.

Similar Problems

Intuition:
A brute force way to solve this will be to generate the entire Pascal's Triangle up to the given row number and then return the element at the given position. However, this approach is not efficient as it involves generating the entire triangle even if we only need a single element.

We can optimize this by calculating the value of the element directly using the formula for combinations (nCr) and avoiding the generation of the entire triangle. The element in the rth row and cth column will be r-1Cc-1.

The formula for combinations (nCr) is given by:
nCr = n! / (r! * (n-r)!), where n! denotes the factorial of n.

To calculate nCr, we can use the following iterative formula to avoid overflow:
nCr = (n * (n-1) * ... * (n-r+1)) / (r * (r-1) * ... * 1)

Note
We have the following properties of combinations: nCr = nCn-r
As we are iterating for r number of times, we can choose the smaller value between r and (n-r) to minimize the number of iterations. This will help in optimizing the calculation.
Approach:
Identify the given row and column position in Pascal's Triangle.
Compute the binomial coefficient nCr using the formula nCr = n! / (r! * (n-r)!).
Optimize the calculation by selecting the smaller value between r and (n-r) to minimize iterations.
Initialize the result as 1. Iterate through the range, updating the result using multiplication and division to prevent overflow.
Return the computed nCr, which represents the value at the specified position in Pascal's Triangle.
Solution:

Complexity Analysis:
Time Complexity: O(C), where C is the column number. This is because the loop in the nCr function runs for a total of C times, where C can be as large as N/2.

Space Complexity: O(1), as no extra space is used.

# Create a class to replicate the structure
class Solution:
    # Function to print the element in rth row and cth column 
    def pascalTriangleI(self, r, c):
        return self.nCr(r - 1, c - 1)
    
    # Function to calculate nCr
    def nCr(self, n, r):
        # Choose the smaller value for lesser iterations
        if r > n - r:
            r = n - r
        
        # base case
        if r == 1:
            return n
        
        res = 1  # to store the result 
        
        # Calculate nCr using iterative method avoiding overflow 
        for i in range(r):
            res = res * (n - i)
            res = res // (i + 1)
        
        return res  # return the result 

# row number
r = 5 
# col number
c = 3

# Create an instance of the Solution class
sol = Solution()

# Function call to print the element in rth row and cth column 
ans = sol.pascalTriangleI(r, c)

print("The element in the rth row and cth column in pascal's triangle is:", ans)

'''
class Solution:
    def pascalTriangleI(self, r, c):
        return self.nCr(r - 1, c - 1)

    def nCr(self, n, r):
        res = 1
        for i in range(r):
            res = res * (n-i)
            res = res // (i + 1)
        return res