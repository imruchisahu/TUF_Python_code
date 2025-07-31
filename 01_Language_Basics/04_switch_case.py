'''
Given the integer day denoting the day number, print on the screen which day of the week it is. Week starts from Monday and for values greater than 7 or less than 1, print Invalid.

Ensure only the 1st letter of the answer is capitalised.

For printing use:-

for C++ : cout << variable_name;
for Java : System.out.print();
for Python : print()
for Javascript : console.log()

Examples:
Input: day = 3

Output: Wednesday

Input: day = 8

Output: Invalid

Input: day = 2

Output:
Tuesday
Constraints:
0 <= day <= 50

Similar Problems

//code
class Solution:
    # Function to determine the day of 
    # the week based on day number
    def whichWeekDay(self, day):
        # Check if the day number is valid
        if day < 1 or day > 7:
            print("Invalid")
            return

        # Using match-case to print the corresponding day
        match day:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case 7:
                print("Sunday")

# Creating an instance of Solution class
sol = Solution()

# Taking user input
day = int(input("Enter the day number: "))

# Function call to determine the day 
# of the week based on day number
sol.whichWeekDay(day)


'''
class Solution:
    
    def whichWeekDay(self, day):
        
        if (day<1  or day > 7):
            print("Invalid")
            return
        match day:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case 7:
                print("Sunday")
Solution()
