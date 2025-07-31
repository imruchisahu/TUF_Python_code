
'''
Given marks of a student, print on the screen:

Grade A if marks >= 90
Grade B if marks >= 70
Grade C if marks >= 50
Grade D if marks >= 35
Fail, otherwise.


For printing use:-

for C++ : cout << variable_name;
for Java : System.out.print();
for Python : print()
for Javascript : console.log()
for C# : Console.WriteLine();
for Go : fmt.Println()

Examples:
Input: marks = 95

Output: Grade A

Explanation: marks are greater than or equal to 90.

Input: marks = 14

Output: Fail

Explanation: marks are less than 35.

Input: marks = 70

Output:
Grade B
Constraints:
0 <= marks <= 100

Similar Problems

//code:
class Solution:
    //Function to check if the person is an adult or a teen 
    def isAdult(self, age):
        
        # If age is greater than or equal to 18
        if age >= 18:
            # The person is an adult
            print("Adult")
        
        # Otherwise
        else:
            # The person is a teen
            print("Teen")

if __name__ == "__main__":
    # Creating an instance of Solution class
    solution = Solution()

    # Take age as input
    age = int(input("Enter your age: "))

    // Function call to check if the person is an adult or a teen
    solution.isAdult(age)

'''
class Solution:
    def isAdult(self, age):
        # Your code goes here
        if age >= 18:
            print("Adult")
        else:
            print("Teen")
Solution()

'''class Solution:
    def studentGrade(self, marks):
        if marks >= 90:
            print("Grade A")
        elif ( marks >= 70):
            print("Grade B")
        elif (marks >= 50):
            print("Grade C")
        elif (marks >= 35):
            print("Grade D")
        else:
            print("Fail")
Solution()'''