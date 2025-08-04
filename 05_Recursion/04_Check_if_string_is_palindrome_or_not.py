'''Given a string s, return true if the string is palindrome, otherwise false.



A string is called palindrome if it reads the same forward and backward.


Examples:
Input : s = "hannah"

Output : true

Explanation : The string when reversed is --> "hannah", which is same as original string , so we return true.

Input : s = "aabbaaa"

Output : false

Explanation : The string when reversed is --> "aaabbaa", which is not same as original string, So we return false.

Input : s = "aabbcccdbbaa"

Output:
false
Constraints:
1 <= s.length <= 103
s consist of only uppercase and lowercase English characters.
Intuition
Determining whether a string is a palindrome through recursion involves comparing characters from the start and end of the string. If the characters match, the next set of characters is checked recursively, moving inward. This process continues until a mismatch is found, indicating the string is not a palindrome, or until all characters are verified to match, confirming the string reads the same forwards and backwards.

Approach
Start by comparing the first and last characters of the string. If the characters match, move inward by increasing the starting index and decreasing the ending index. Check if the substring between these indices is also a palindrome.
Continue this process until the starting index is greater than or equal to the ending index. If at any point the characters do not match, the string is not a palindrome.
If all the characters are successfully compared and they all match, the string is a palindrome.
Dry Run


Complexity Analysis
Time Complexity : O(N) – A single pass through the string with recursive calls, where n is the length of the string.

Space Complexity: O(N) – Due to the recursion stack that grows with the length of the string.





class Solution:
    def palindromeCheck(self, s: str) -> bool:
        # Call the recursive helper method with initial indices
        return self.isPalindrome(s, 0, len(s) - 1)
    
    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        # Base Case: If the start index is greater than or equal to the end index
        if left >= right:
            return True
        # Check if characters at the current positions are the same
        if s[left] != s[right]:
            return False  # Characters do not match, so it's not a palindrome
        # Recur for the next set of characters
        return self.isPalindrome(s, left + 1, right - 1)
    
# Main method to test the palindromeCheck function
if __name__ == "__main__":
    solution = Solution()
    print(solution.palindromeCheck("hannah"))  # Output: True
    print(solution.palindromeCheck("aabbaaa"))  # Output: False
    print(solution.palindromeCheck("aba"))      # Output: True

'''
class Solution:
    def palindromeCheck(self, s: str) -> bool:
        return self.isPalindrome(s, 0, len(s) - 1)
    
    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return self.isPalindrome(s, left + 1, right -1)
s=Solution()
print(s.palindromeCheck("hananah"))
print(s.palindromeCheck("aabbaaa"))
