'''Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



*****
*   *
*   *
*   *
*****


Print the pattern in the function given to you.


Examples:
Input: n = 4

Output:



Input: n = 2

Output:



Constraints:
1 <= n <= 100

Approach: 
Use a for loop to iterate from 0 to N-1, where N is the number of rows. This loop will ensure to print each row of the pattern.
Inside the outer loop, use another loop to iterate from 0 to n-1. This loop controls the columns in each row. Within the inner loop, check if it's a top row, left column, bottom row, right column, if so, print a asterisk. Otherwise, print a space.
After completing a row give a line break, to make sure next row gets printed as well.


Complexity Analysis: 
Time Complexity : O(N2). The overall complexity will be O(N2), where N is the number of rows.

Space Complexity :O(1). As no extra space is being used to print the patterns.

class Solution:
    # Function to print pattern21
    def pattern21(self, n):
        # Outer loop for the rows.
        for i in range(n):
            
            """ Inner loop for printing 
            the stars at borders only."""
            for j in range(n):
                
                if i == 0 or j == 0 or i == n-1 or j == n-1:
                    print("*", end="")
                else:
                    print(" ", end="")
                    
            # Move to the next row.
            print()

if __name__ == "__main__":
    N = 5
    
    # Create an instance of Solution class
    sol = Solution()
    
    sol.pattern21(N)


'''
class Solution:
    def pattern21(self, n):
        for i in range(n):
            for j in range(n):
                if i==0 or j==0 or i==n-1 or j==n-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()