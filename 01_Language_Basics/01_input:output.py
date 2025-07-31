'''Complete the function printNumber which takes an integer input from the user and prints it on the screen.



Use:-

for C++ : cout << variable_name;
for Java : System.out.print();
for Python : print()
for Javascript : console.log()

Examples:
Input(user gives value): 7

Output: 7

Input(user gives value): -5

Output: -5

Input(user gives value): 0

Output:
0
Constraints:
-1000 <= User Input <= 1000

Similar Problems


'''

'''
//Code
class Solution:
    # Function to take input and display output 
    def printNumber(self):
        # Take input
        number = int(input())
        
        # Print output
        print(number)

# Driver code
if __name__ == "__main__":
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to take input and display output
    sol.printNumber()
'''
# take input from user
class Solution:
    def printNumber(self):
        n = int(input())
        print(n)
s=Solution()
s.printNumber()