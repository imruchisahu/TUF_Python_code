'''Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5


Print the pattern in the function given to you.


Examples:
Input: n = 4

Output:



Input: n = 2

Output:



Constraints:
1 <= n <= 100

Similar Problems
Approach
Use a for loop to iterate from 0 to 2*N-2, where N is the number of rows. This loop will ensure to print each row of the pattern.
Inside the outer loop, use another loop to iterate from 0 to 2*N-2. This loop controls the columns of each row.
Assume the pattern as matrix, for each cell in the matrix, calculate how far the cell is from the matrix boundaries: top = distance to the top edge, bottom = distance to the bottom edge, right = distance to the right edge (from reverse index), left = distance to the left edge (from reverse index).
Determine the value for each cell based on the minimum distance from the edges. This calculation ensures that cells closer to the edges have higher values, which decrease towards the center.
After completing a row give a line break, to make sure next row gets printed as well.
Solution

Complexity Analysis
Time Complexity: O(N2)
The time complexity is dominated by the nested loops, which both iterate 2×N-1 times. Therefore, the overall time complexity is O((2×N-1)2), which simplifies to O(N2), where N is the number of rows.

Space Complexity: O(1), as no extra space is being used to print the patterns.

class Solution:
    # Function to print pattern22
    def pattern22(self, n):
        # Outer loop for the rows
        for i in range(2 * n - 1):
            # Inner loop for the columns
            for j in range(2 * n - 1):
                
                """ Initialising the top, down, left
                and right indices of a cell"""
                top = i
                left = j
                right = (2 * n - 2) - j
                bottom = (2 * n - 2) - i
                
                """ Minimum of 4 directions and then we 
                subtract from n because previously we 
                would get a pattern whose border has 0's, 
                but we want with border n's and then
                decreasing inside."""
                print((n - min(min(top, bottom), min(left, right))), end=" ")
                
            # Move to the next row
            print()

# Main function
if __name__ == "__main__":
    N = 5
    
    # Create an instance of Solution class
    sol = Solution()
    
    sol.pattern22(N)

'''

class Solution:
    def pattern22(self, n):
        for i in range(2*n-1):
            for j in range(2*n-1):
                top=i
                bottom=((2*n-2)-i)
                left=j
                right=((2*n-2)-j)
                print(n-min(top, left, right, bottom), end=" ")
            print()