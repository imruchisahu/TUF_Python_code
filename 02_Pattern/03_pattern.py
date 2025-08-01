'''Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



1
12
123
1234
12345



Print the pattern in the function given to you.


Examples:
Input: n = 4

Output:



Input: n = 2

Output:



Constraints:
1 <= n <= 100

Similar Problems

Approach: 
Use a for loop to iterate from 1 to N, where N is the number of rows. This loop will ensure to print each row of the pattern.
Inside this loop, run another loop from 1 to current value of the outer loop variable. It will ensure that the number of rows and columns are equal(1 column in 1st row, 2 columns in 2nd row etc).
Now, print the current value of inner loop variable, as the column number needs to be printed in each column of the current row.
Move to a new line after printing each row to maintain the right-angled triangle shape of the pattern.


Time Complexity : O(N2). As the outer loop runs for N time and the inner loop runs incrementally in each iteration(1+2+3+...+N), which is equal to (N*(N+1)/2). So, overall it is O(N2).

Space Complexity :O(1). As no extra space is being used to print the patterns.

class Solution:
    
    # Function to print pattern3
    def pattern3(self, n):
        
        # Outer loop will run for rows.
        for i in range(1,n+1):
            
            # Inner loop will run for columns.
            for j in range(1,i+1):
                print(j, end="")
                
            """ As soon as n stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = 5

        # Create an instance of the Solution class
        sol = Solution()

        sol.pattern3(N)

if __name__ == "__main__":
    Solution().main()

'''

class Solution:
    def pattern3(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end="")
            print()
s=Solution()
s.pattern3(5)