'''Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA


Print the pattern in the function given to you.


Examples:
Input: n = 4

Output:



Input: n = 2

Output:



Constraints:
1 <= n <= 26

Similar Problems
Approach:
Use a for loop to iterate from 0 to N-1, where N is the number of rows. This loop will ensure each row of the pattern is printed.
First, print the spaces needed before the characters in each row using an inner loop. Then, using another loop, print the alphabet characters. As observed from the pattern, the alphabet characters need to be printed incrementally up to a certain point (breakpoint) in every row, and then they need to be printed in a decreasing manner.
After that, print the spaces that are needed after the characters for each row. Upon completion of a row, give a line break to ensure the next row is printed correctly.
Solution:

Complexity Analysis:
Time Complexity : O(N2). The overall complexity will be O(N2), due to nested loops iterating over each row for spaces and characters to be printed. Where N is the number of rows.

Space Complexity :O(1). As no extra space is being used to print the patterns.

class Solution:
    # Function to print pattern17
    def pattern17(self, n):
        # Outer loop for the number of rows.
        for i in range(n):
            
            # Printing spaces before characters.
            for j in range(n - i - 1):
                print(" ", end="")
            
            # Printing characters.
            ch = 'A'
            breakpoint = (2 * i + 1) // 2
            for j in range(1, 2 * i + 2):
                print(ch, end="")
                if j <= breakpoint:
                    ch = chr(ord(ch) + 1)
                else:
                    ch = chr(ord(ch) - 1)
            
            # Move to the next line for the next row.
            print()

if __name__ == "__main__":
    N = 5
    
    #Create an instance of Solution class
    sol = Solution()
    
    sol.pattern17(N)



'''
class Solution:
    def pattern17(self, n):
        for i in range(n):
            for j in range(1, n-i):
                print(" ", end="")
            ch = 'A'
            p=(2*i+1)//2
            for j in range(1, 2*i+2):
                print(ch, end="")
                if (j<= p):
                    ch = chr(ord(ch)+1)
                else:
                    ch=chr(ord(ch)-1)
            print()
            