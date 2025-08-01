'''Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



1        1
12      21
123    321
1234  4321
1234554321


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
This pattern can be divided into three parts: first print the numbers, then spaces and at last numbers again.
Find out the numbers of spaces needs to printed in the first row and store it in a variable spaces.
Then iterate from 1 to N to define the number of rows. Using nested for loop print the numbers as required , then in separate loop print the spaces and finally, the numbers in third loop.
After completion of a row, decrease the number of spaces and give a line break to print next row.


Complexity Analysis: 
Time Complexity : O(N2). Where, N is the number of rows provided as an input.

Space Complexity :O(1). As no extra space is being used to print the patterns.
class Solution:
    # Function to print pattern12
    def pattern12(self, n):
        # Initial no. of spaces in row 1.
        spaces = 2 * (n - 1)

        # Outer loop for the number of rows.
        for i in range(1, n + 1):
            # For printing numbers in each row
            for j in range(1, i + 1):
                print(j, end="")

            # For printing spaces in each row
            for j in range(1, spaces + 1):
                print(" ", end="")

            # For printing numbers in each row
            for j in range(i, 0, -1):
                print(j, end="")

            """ As soon as the numbers for each iteration
            are printed, we move to the next row and give
            a line break otherwise all numbers would get 
            printed in 1 line"""
            print()

            """ After each iteration nos. increase by 
            2, thus spaces will decrement by 2"""
            spaces -= 2

if __name__ == "__main__":
    N = 5

    # Create an instance of Solution class
    sol = Solution()

    sol.pattern12(N)

'''
class Solution:
    def pattern12(self, n):
        for i in range(1, n+1):
            for j in range(1, (i+1)):
                print(j, end="")
            for j in range(2*n-2*i):
                print(" ", end="")
            for j in range(i, 0 , -1):
                print(j, end="")
            print()
