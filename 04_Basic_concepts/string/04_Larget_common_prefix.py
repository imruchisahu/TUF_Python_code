'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Examples:
Input : str = ["flowers" , "flow" , "fly", "flight" ]

Output : "fl"

Explanation : All strings given in array contains common prefix "fl".

Input : str = ["dog" , "cat" , "animal", "monkey" ]

Output : ""

Explanation : There is no common prefix among the given strings in array.

Input : str = ["lady" , "lazy"]

Output:
"la"
Constraints:
1 <= str.length <= 200
1 <= str[i].length <= 200
str[i] contains only lowercase English letters.

Intuition
To determine the longest common prefix among a set of strings, consider the following approach: when a list of strings is sorted lexicographically, the first string and the last string in this sorted list will differ the most. The common prefix of these two strings is guaranteed to be the longest common prefix across all strings in the array. For example, if the sorted list is ["flight", "flow", "flowers", "fly"], comparing the first and last string in the sorted order gives the longest common prefix shared by all strings in the list.

Approach
Sort the array of strings.
Select the first and the last string from the sorted array. These two strings will have the maximum possible common prefix.
Initialize an index variable to zero. This index will track the length of the common prefix.
Compare characters at the current index of both selected strings. Continue moving the index forward as long as the characters at the current index are equal and the index is within the bounds of both strings.
Once characters differ or the end of one of the strings is reached, the index will indicate the length of the common prefix.
Return the substring of the first string from the start to the index, which represents the longest common prefix.
Dry Run


Complexity Analysis
Time Complexity: O(N * M * log N + M), where N is the number of strings and M is the maximum length of a string. The sorting operation takes O(N * M * log N) time, and the comparison of characters in the first and last strings takes O(M) time.

Space Complexity: O(M), as the ans variable can store the length of the prefix which in the worst case will be O(M).


class Solution:
    # Method to find the longest common prefix in a list of strings
    def longestCommonPrefix(self, strs):
        # Edge case: empty list
        if not strs:
            return ""
        
        # Sort the list to get the lexicographically smallest and largest strings
        strs.sort()
        # First string (smallest in sorted order)
        first = strs[0]  
        # Last string (largest in sorted order)
        last = strs[-1]  
        
        # Compare characters of the first and last strings
        ans = []
        for i in range(min(len(first), len(last))):
            # If characters don't match, return the current prefix
            if first[i] != last[i]:
                return ''.join(ans)
            # Append the matching character to the result
            ans.append(first[i])
        
        # Return the longest common prefix found
        return ''.join(ans)

# Test the longestCommonPrefix method
if __name__ == "__main__":
    solution = Solution()
    input_strs = ["flower", "flow", "flight"]
    result = solution.longestCommonPrefix(input_strs)
    print("Longest Common Prefix:", result)  # Output: "fl"


'''
class Solution:  
    def longestCommonPrefix(self, st):
        #your code goes here
        if not st:
            return ""
        st.sort()
        first=st[0]
        last=st[-1]
        ans=[]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ''.join(ans)
            ans.append(first[i])
        return ''.join(ans)