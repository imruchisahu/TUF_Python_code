'''You are given two integers n1 and n2. You need find the Lowest Common Multiple (LCM) of the two given numbers. Return the LCM of the two numbers.



The Lowest Common Multiple (LCM) of two integers is the lowest positive integer that is divisible by both the integers.


Examples:
Input: n1 = 4, n2 = 6

Output: 12

Explanation: 4 * 3 = 12, 6 * 2 = 12.

12 is the lowest integer that is divisible both 4 and 6.

Input: n1 = 3, n2 = 5

Output: 15

Explanation: 3 * 5 = 15, 5 * 3 = 15.

15 is the lowest integer that is divisible both 3 and 5.

Input: n1 = 4, n2 = 12

Output:
12
Constraints:
1 <= n1, n2 <= 1000

Similar Problems

class Solution:
    # Function to find LCM of n1 and n2
    def LCM(self, n1, n2):
        # Variable to store lcm
        lcm = 0
        
        # Variable to store max of n1 & n2
        n = max(n1, n2)
        i = 1
        
        while True:
            # Variable to store multiple
            mul = n * i
            
            # Checking if multiple is common
            # common for both n1 and n2
            if mul % n1 == 0 and mul % n2 == 0:
                lcm = mul
                break
            i += 1
        
        # Return the stored LCM
        return lcm

# Input values
n1 = 4
n2 = 12

# Creating an instance of Solution class
sol = Solution()

# Function call to get LCM of n1 and n2
ans = sol.LCM(n1, n2)
print("The LCM of", n1, "and", n2, "is:", ans)

'''

class Solution:
    def LCM(self, n1, n2):
        if n1>n2:
            greater = n1
        else:
            greater = n2
        while(True):
            if ((greater % n1 == 0) and (greater % n2 == 0)):
                lcm = greater
                break
            greater += 1
        return lcm