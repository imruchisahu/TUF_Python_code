'''
Given a string s. Return the last character of the given string s.


Examples:
Input : s = "takeuforward"

Output : d

Explanation : The last character of given string is "d".

Input : s = "goodforyou"

Output : u

Explanation : The last character of given string is "u".

Input : s = "lovecoding"

Output:
g
Constraints:
1 <= s.length <= 100
s consist of only lowercase English letters

Approach:
Identify the last character of the string. Since strings are zero-indexed, the last character can be accessed using the index len(s) - 1, where len is the length of the string.
Return or print the last character.

'''

'''
class Solution:
    # Function to return the last character of the string
    def lastChar(self, s):
        
        # Return last character of string
        return s[-1]

# Creating an instance of Solution class
sol = Solution()
s = "example"

# Function call to get the last character of the string
ans = sol.lastChar(s)
print("The last character is:", ans)
'''


class Solution:
    def lastChar(self, s):
        #your code goes here
        return (s[-1])
