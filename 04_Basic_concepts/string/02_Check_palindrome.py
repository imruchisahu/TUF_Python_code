'''You are given a string s. Return true if the string is palindrome, otherwise false. A string is called palindrome if it reads the same forward and backward.


Examples:
Input : s = "hannah"

Output : true

Explanation : The given string when read backward is -> "hannah", which is same as when read forward.

Hence answer is true.

Input : s = "aabbaaa"

Output : false

Explanation : The given string when read backward is -> "aaabbaa", which is not same as when read forward.

Hence answer is false.

Input : s = "aabbccbbaa"

Output:
true
Constraints:
1 <= s.length <= 105
s consist of only uppercase and lowercase English characters.

Similar Problems
Intuition:
To determine if a string is a palindrome, that is, reads the same backwards as forwards, begin by comparing the first and last characters. If they match, proceed by moving inward from both ends and comparing the subsequent pairs of characters. This process is repeated, gradually converging towards the center of the string. If all character pairs match throughout this process, the string is confirmed to be a palindrome. This method effectively checks for symmetry by comparing characters from both ends toward the center.

Approach:
Initialize two pointers: one at the beginning (`left`) and one at the end (`right`) of the string.
Run a for loop till half the length of the string to compare the first and last characters. If they are not equal, return false.
Move both pointers inward (increment `left` and decrement `right`) and continue the comparison. If the loop completes without finding unequal characters, the string is a palindrome and returns true.

Note: This problem can also be solved by a Recursive Approach
In the recursive approach, the letters at the two ends of the string are compared. If they match, the function is called recursively for the next pair of elements (start+1, end-1) until the start index is greater than or equal to the end index. If at any point the characters differ, return false. If the base condition is reached (start >= end), the string is a palindrome and true is returned.

Complexity Analysis
Time Complexity: O(N), where n is the length of the string.

Space Complexity: O(1), as no extra space is required.


class Solution:
    # Function to check if a given string is a palindrome
    def palindromeCheck(self, s):
        left = 0               
        right = len(s) - 1     

        # Iterate while  start pointer is less than end pointer
        while left < right:
            # If characters  don't match, it's not a palindrome
            if s[left] != s[right]:
                return False
            left += 1  
            right -= 1  
        return True 

if __name__ == "__main__":
    solution = Solution()
    str = "racecar"  

    if solution.palindromeCheck(str):
        print(f"{str} is a palindrome.")
    else:
        print(f"{str} is not a palindrome.")

'''

class Solution:    
    def palindromeCheck(self, s):
        #your code goes here
        if s == s[::-1]:
            return True
        else:
            return False