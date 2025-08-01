'''Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



A

BB

CCC

DDDD

EEEEE



Print the pattern in the function given to you.


Examples:
Input: n = 4

Output:



Input: n = 2

Output:



Constraints:
1 <= n <= 26

Similar Problems


'''
class Solution:
    def pattern16(self, n):
        for i in range(n):
            ch=(ord('A') + i)
            for j in range(i+1):
                print(chr(ch), end="")
                
            print()