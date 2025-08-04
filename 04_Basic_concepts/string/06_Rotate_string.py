'''Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.


Examples:
Input : s = "abcde" , goal = "cdeab"

Output : true

Explanation : After performing 2 shifts we can achieve the goal string from string s.

After first shift the string s is => bcdea

After second shift the string s is => cdeab.

Input : s = "abcde" , goal = "adeac"

Output : false

Explanation : Any number of shift operations cannot convert string s to string goal.

Input : s = "abcde" , goal = "abcde"

Output:
true
Constraints:
1 <= s.length <= 100
1 <= goal.length <= 100
s and goal consist of only lowercase English letters.

Intuition
To address this problem, a solution could be to generate all possible rotations of the string and verify if any of these rotations match the target `goal` string. The approach involves systematically creating each rotation and comparing it against the `goal`, which ensures that if a matching rotation exists, it will be identified.

Approach
First generate all possible rotations of the string by rearranging its character using the substring method.
For each rotation created, check if it is the same as the goal string.
If any rotation matches the goal, return true; otherwise, after testing all rotations, return false.

Complexity Analysis
Time Complexity O(N^2) Generate N rotations and each comparison takes O(N) time.

Space Complexity O(N) for the space needed to store each rotated string.
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
   # Strings must be same length to be rotations of each other
        if len(s) != len(goal):
            return False  
        # Try all possible rotations of s
        for i in range(len(s)):
            rotated = s[i:] + s[:i]  # Create a new rotation
            if rotated == goal:
                return True  
        return False  

# Test cases
sol = Solution()
print(sol.rotateString("abcde", "cdeab"))  # Output: True
print(sol.rotateString("abcde", "abced"))  # Output: False


'''
class Solution:    
    def rotateString(self, s, goal):
        #your code goes here
        if len(s) != len(goal):
            return False
        return goal in (s + s)