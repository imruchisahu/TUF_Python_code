'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Examples:
Input : s = "anagram" , t = "nagaram"

Output : true

Explanation : We can rearrange the characters of string s to get string t as frequency of all characters from both strings is same.

Input : s = "dog" , t = "cat"

Output : false

Explanation : We cannot rearrange the characters of string s to get string t as frequency of all characters from both strings is not same.

Input : s = "eat" , t = "tea"

Output:
true
Constraints:
1 <= s.length , t.length <= 5*104
s and t consist of only lowercase English letters
Intuition
The letters of an anagram should form identically sequences if alphabetically sorted. By furthering this thought process a method to check for anagrams would be sorting both strings. By sorting both strings and then comparing them, we can easily determine if they contain the same characters in the same frequencies.

Approach
Sort the characters of both strings using an inbuilt sort function, so that if they are anagrams, the sorted strings will be identical.

Compare the sorted versions of both strings. If they match, the original strings are anagrams; otherwise, they are not.

Return true if the sorted strings are identical, otherwise return false.


Complexity Analysis
Time Complexity: O(N log N) due to sorting each string.

Space Complexity: O(1) as no additional data structures are used. Note that for Java, the space complexity will be O(N) due to the creation of additional character arrays. And for Python, the space complexity will be O(N) due to the use of sorted() function, which creates a new string to hold the sorted string.





class Solution:
    def anagramStrings(self, s, t):
        # If lengths are not equal, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Sort both strings and compare
        return sorted(s) == sorted(t)

if __name__ == "__main__":
    solution = Solution()
    str1 = "INTEGER"
    str2 = "TEGERNI"
    result = solution.anagramStrings(str1, str2)
    print("True" if result else "False")

'''
class Solution:    
    def anagramStrings(self, s, t):
        #your code goes here
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)