'''
Given string str containing just the characters '(', ')', '{', '}', '[' and ']', check if the input string is valid and return true if the string is balanced otherwise return false.


Examples:
Input: str = “()[{}()]”

Output: True

Explanation: As every open bracket has its corresponding close bracket. Match parentheses are in correct order hence they are balanced.

Input: str = “[()”

Output: False

Explanation: As ‘[‘ does not have ‘]’ hence it is not valid and will return false.

Input: str = "{[()]}"

Output:
True
False

Submit
Constraints:
1 <= str.length <= 104

str consists of parentheses only '()[]{}'.

Intuition:
Let us understand first when a string is said to be balanced:

Every opening bracket must have a corresponding closing bracket and vice versa.
Example: "(){}" is valid but "(]{}" is invalid.
The order of opening brackets must follow the order to closing brackets.
Example: "([{}])" is valid but "({[}])" is invalid.

In order to find whether a paranthesis is matching or not, we need to know what was the last opened paranthesis for every closing paranthesis found.
Example: If a ')' (closing paranthesis) is found, the last opened paranthesis must be '(', then only the paranthesis will be matched, otherwise it's a mismatch.

Now, in order to find the last opened paranthesis first, a data structure like stack will be helpful.
The stack will store opening brackets (i.e., '(' or '[' or '{') to maintain them in LIFO order. The following operations will be performed:
For every opening bracket found, it must be pushed on top of the stack.
For every closing bracket found, the last opened bracket (top element of the stack) can be taken out. Now there can be the following cases:
Match: If the opening bracket found matches with the closing bracket.
Mismatch: If the opening bracket found does not match with the closing bracket. This leads to an unbalanced paranthesis.
If all the paranthesis are matched, the given pair of paranthesis is valid otherwise it is not valid.
Edge Cases:
What if there is no top element in stack when a closing bracket is found?
This will happen for strings like "()]", where there is no opening bracket to compare with the ']' bracket. In such cases, the parantheis will be invalid.

Approach:
Initialize a stack that will store character data type (to store the opening brackets).
Start traversing the given string one character at a time. For every opening bracket found, push it on top of the stack.
For every closing bracket, take the top element (last opened bracket) of the stack (if it doesn't exit, return the string as invalid):
If the opening and closing bracket matches, continue matching the string further.
Otherwise, the string is invalid.
Once all the characters are read from the input string, check if the stack is empty. If it is empty, all the paranthesis are balanced, otherwise unbalanced.

class Solution:
    # Function to match the opening 
    # and closing brackets
    def isMatched(self, open, close):
       
        # Match
        if((open == '(' and close == ')') or
           (open == '[' and close == ']') or
           (open == '{' and close == '}')
        ):
            return True
           
        # Mismatch
        return False

    # Function to check if the 
    # string is valid
    def isValid(self, str):
       
        # Initialize a stack
        st = []
       
        # Start iterating on the string
        for i in range(len(str)):
           
            # If an opening bracket is found
            if str[i] == '(' or str[i] == '[' or str[i] == '{':
               
                # Push on top of stack
                st.append(str[i])
           
            # Else if a closing bracket is found
            else:
                # Return false if stack is empty
                if not st:
                    return False
               
                # Get the top element from stack
                ch = st[-1]
                st.pop()
               
                # If the opening and closing brackets 
                # are not matched, return false
                if not self.isMatched(ch, str[i]):
                    return False
       
        # If stack is empty, the 
        # string is valid, else invalid
        return not st

# Creating an instance of 
# Solution class
sol = Solution()

# Function call to check if the 
# string is valid
str = "()[{}()]"
ans = sol.isValid(str)

if ans:
    print("The given string is valid.")
else:
    print("The given string is invalid.")

Complexity Analysis:
Time Complexity: O(N) (where N is the length of the string)
Traversing the string once takes O(N) time.

Space Complexity: O(N)
In the worst case (when the string contains only opening brackets), the stack will store all the characters, taking O(N) space.



'''