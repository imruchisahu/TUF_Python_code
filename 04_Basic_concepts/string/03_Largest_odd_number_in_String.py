'''Given a string s, representing a large integer, the task is to return the largest-valued odd integer (as a string) that is a substring of the given string s.



The number returned should not have leading zero's. But the given input string may have leading zero. (If no odd number is found, then return empty string.)


Examples:
Input : s = "5347"

Output : "5347"

Explanation : The odd numbers formed by given strings are --> 5, 3, 53, 347, 5347.

So the largest among all the possible odd numbers for given string is 5347.

Input : s = "0214638"

Output : "21463"

Explanation : The different odd numbers that can be formed by the given string are --> 1, 3, 21, 63, 463, 1463, 21463.

We cannot include 021463 as the number contains leading zero.

So largest odd number in given string is 21463.

Input : s = "0032579"

Output:
"32579"
Constraints:
1 <= s.length <= 103
'0' <= s[i] <= '9'
Intuition
To determine the largest substring ending with an odd digit, start by iterating backward from the end of the number. This approach efficiently finds the rightmost odd digit by examining each character in reverse order. Once an odd digit is encountered, the substring from the beginning of the number up to and including this digit represents the largest possible odd-ending substring. This process leverages the fact that finding the last occurrence of an odd digit directly provides the longest valid substring.

Approach
1. Start by iterating through the string from the end towards the beginning to find the first odd digit. This digit marks the potential end of the largest odd number substring.

2. Once an odd digit is found, skip any leading zeroes from the beginning of the string up to this odd digit.

3. Extract and return the substring starting after the leading zeroes and ending at the identified odd digit. This substring represents the largest odd integer without leading zeroes.

Dry Run
Image 1
Image 2
Image 3
Image 4

1/4



Complexity Analysis
Time Complexity: O(N), The loop runs once through the string of length N.

Space Complexity: O(N), The auxiliary space used is O(1) but if the space for returned string is considered (which will be O(N) in the worst case), the overall space complexity comes out to be O(N).

class Solution:
    # Function to find the largest odd number 
    # that is a substring of given string 
    def largeOddNum(self, s: str) -> str:
        ind = -1
        
        # Iterate through the string from the end to beginning
        i = 0
        for i in range(len(s) - 1, -1, -1):
            # Break if an odd digit is found
            if (int(s[i]) % 2) == 1:
                ind = i
                break
        
        # Skipping any leading zeroes
        i = 0
        while i <= ind and s[i] == '0':
            i += 1
        
        # Return the largest odd number substring
        return s[i:ind + 1]

# Driver code
solution = Solution()
num = "504"
result = solution.largeOddNum(num)
print("Largest odd number:", result)

'''
class Solution:  
    def largeOddNum(self, s):
        #your code goes here
        for i in range(len(s) - 1, -1, -1):
            if int(s[i]) % 2 == 1:
                result = s[:i+1].lstrip('0')
                return result if result else ""
        return ""