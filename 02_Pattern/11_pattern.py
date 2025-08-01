'''Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



1 

0 1 

1 0 1 

0 1 0 1 

1 0 1 0 1



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
Iterate from 1 to N using a for loop, it will basically define the number of rows needed.
Now, if the row is even then start from 1, else from 0. Alternatively print 0's and 1's throughout the the current row.
Finally, print a next line at the end of a row, it ensures to print the next row as well.


Complexity Analysis: 
Time Complexity : O(N2). Where, N is the number of rows provided as an input.

Space Complexity :O(1). As no extra space is being used to print the patterns.

class Solution:
    # Function to print pattern11
    def pattern11(self, n):
        # First row starts by printing a single 1.
        start = 1

        # Outer loop for the number of rows
        for i in range(n):
            """ If the row index is even, start 
            with 1; if odd, start with 0"""
            if i % 2 == 0:
                start = 1
                
            else:
                start = 0

            """ Alternatively print 1's and 0's 
            in each row by using inner for loop"""
            for j in range(i + 1):
                print(start, end=" ")
                start = 1 - start

            # Move to the next row and give a line break
            print()

if __name__ == "__main__":
    N = 5

    # Create an instance of Solution class
    sol = Solution()

    sol.pattern11(N)


'''

class Solution:
    def pattern11(self, n):
        start = 1
        for i in range(n):
            if (i % 2 == 0):
                start = 1
            else:
                start = 0
            for j in range(i+1):
                print(start, end=" ")
                start = 1 - start
            print()