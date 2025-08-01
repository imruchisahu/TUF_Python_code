'''Approach: 
Use a for loop to iterate from 0 to N-1, where N is the number of rows. This loop will ensure to print each row of the pattern.
The inner loop will run for i times and print alphabets from 'A' to 'A' + (N-row number-1).
After completing a row give a line break, to make sure next row gets printed as well.


Complexity Analysis: 
Time Complexity : O(N2). The overall complexity will be O(N2), where N is the number of rows.

Space Complexity :O(1). As no extra space is being used to print the patterns.
class Solution:
    # Function to print pattern15
    def pattern15(self, n):
        # Outer loop for the number of rows.
        for i in range(n):
            
            """Inner loop will loop for i times and
            print alphabets from A to A + (n - i - 1)."""
            for ch in range(ord('A'), ord('A') + n - i):
                print(chr(ch), end="")
                
            """As soon as the letters for each iteration
            are printed, we move to the next row and give
            a line break otherwise all letters would get
            printed in 1 line."""
            print()

if __name__ == "__main__":
    N = 5

    # Create an instance of Solution class
    sol = Solution()

    sol.pattern15(N)


'''
class Solution:
    def pattern15(self, n):
        for i in range(n):
            for ch in range(ord('A'), (ord('A') + (n-1-i)+1)):
                print(chr(ch), end="")
            print()