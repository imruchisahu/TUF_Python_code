'''Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



*

**

***

****

*****

****

***

**

*



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
Use nested for loops to print the pattern. First, figure out what is the total number of rows for which the pattern needs to be printed.
Then, print the asterisks incrementally till half the total number of rows and after that decrease the asterisks according to the row number.


Complexity Analysis: 
Time Complexity : O(N2). Where N is the input provided. This quadratic complexity arises due to the nested loops iterating over N rows and printing a number of stars that sums up to approximately N2 stars in total.

Space Complexity :O(1). As no extra space is being used to print the patterns.

class Solution:
    #Function to print pattern10
    def pattern10(self, n):
        # Outer loop for number of rows.
        for i in range(1, 2 * n):
            
            """ stars would be equal to the
            row no. uptill first half"""
            stars = i if i <= n else 2 * n - i
            
            # for printing the stars in each row.
            for j in range(1, stars + 1):
                print("*", end="")
            
            """ As soon as the stars for each iteration are 
            printed, we move to the next row and give a line break"""
            print()

if __name__ == "__main__":
    N = 5
    
    # Create an instance of Solution class
    sol = Solution()
    
    sol.pattern10(N)


'''

class Solution:
    def pattern10(self, n):
        self.pattern2(n)
        self.pattern5(n)
    def pattern2(self, n):
        for i in range(n):
            for j in range(i+1):
                print("*", end="")
            print()

    def pattern5(self, n):
        for i in range(1, n-1+1):
            for j in range(1, (n-i+1)):
                print("*", end="")
            print()

