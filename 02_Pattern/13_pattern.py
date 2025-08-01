'''Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



1 

2 3 

4 5 6 

7 8 9 10 

11 12 13 14 15



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
Iterate from 1 to N, where N is the number of rows.
Inside this loop, take another loop to define the number of columns needed in each row. Now print the numbers strating from 1 and a space. Then increment the number by 1 every time.
After completion of a row, make sure to give a line break to print the next rows as well.


Complexity Analysis: 
Time Complexity : O(N2). Where N is the number of rows provided as a input.

Space Complexity :O(1). As no extra space is being used to print the patterns.

class Solution:
    # Function to print pattern13
    def pattern13(self, n):
        # starting the number
        num = 1

        # Outer loop for the number of rows.
        for i in range(1, n + 1):
            
            """ Inner loop will loop for i times and
            print numbers increasing by 1 each time"""
            for j in range(1, i + 1):
                print(num, end=" ")
                num += 1
                
            """ As soon as the numbers for each iteration
            are printed, we move to the next row and give
            a line break otherwise all numbers would get
            printed in 1 line"""
            print()

if __name__ == "__main__":
    N = 5

    # Create an instance of Solution class
    sol = Solution()

    sol.pattern13(N)



'''
class Solution:
    def pattern13(self, n):
        num=1
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(num, end=" ")
                num += 1
            print()