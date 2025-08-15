'''
Given a string s partition string s such that every substring of partition is palindrome. Return all possible palindrome partition of string s.


Examples:
Input : s = "aabaa"

Output : [ [ "a", "a", "b", "a", "a"] , [ "a", "a", "b", "aa"] , [ "a", "aba", "a"] , [ "aa", "b", "a", "a"] , [ "aa", "b", "aa" ] , [ "aabaa" ] ]

Explanation : Above all are the possible ways in which the string can be partitioned so that each substring is a palindrome.

Input : s = "baa"

Output : [ [ "b", "a", "a"] , [ "b", "aa" ] ]

Explanation : Above all are the possible ways in which the string can be partitioned so that each substring is a palindrome.

Input : s = "ab"

Output:
[ [ "a"] , [ "b"] ]
Constraints:
1<= s.length <= 16
s contains only lowercase English letters.

Real-life Example
Imagine organizing a long sentence into meaningful phrases. Start at the beginning, find a segment that forms a meaningful phrase, and write it down. Move to the next segment and repeat the process. If reaching the end of the sentence and having a list of meaningful phrases, the job is done. If stuck, erase the last phrase, try a different segment, and continue until all segments are explored and every possible meaningful combination is found.

Recursion Intuition
The process involves breaking down a problem into smaller sub-problems. Begin at the start of a string and identify palindromic substrings. Record a substring and proceed to the next part of the string. Continue this process until the end of the string. If the end is reached, a valid partition is found and stored. If a valid partition is not found, backtrack by removing the last recorded substring and try a different substring, exploring all possible palindromic partitions.

Approach
Initialize an empty result list to store all possible partitions.
Define a recursive function that takes the current index, the string, a temporary path list, and the result list.
In the recursive function, check if the current index has reached the end of the string, if true, add the current path to the result list and return. If false, iterate over the substring starting from the current index.
For each substring, check if it is a palindrome, if true, add the substring to the current path. Call the recursive function with the next index. Backtrack by removing the last added substring to explore other possibilities.
Define a helper function to check if a given substring is a palindrome Compare characters from the start and end of the substring. If all characters match, the substring is a palindrome.
Invoke the recursive function initially with the starting index, the string, an empty path list, and the result list. Return the result list containing all possible palindromic partitions.


class Solution:
    def partition(self, s: str):
        def dfs(index, path):
            # If index reaches the end of the string
            if index == len(s):
                # Add the current partition to the result
                res.append(path[:])
                return
            # Iterate over the substring starting from 'index'
            for i in range(index, len(s)):
                # Check if the substring s[index..i] is a palindrome
                if isPalindrome(index, i):
                    # If true, add it to the current path
                    path.append(s[index:i+1])
                    # Recur for the remaining substring
                    dfs(i+1, path)
                    # Backtrack: remove the last added substring
                    path.pop()

        def isPalindrome(start, end):
            # Check if the substring s[start..end] is a palindrome
            while start <= end:
                # If characters do not match, it's not a palindrome
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True # Otherwise, it's a palindrome

        # Resultant list to store all partitions
        res = []
        # Start the depth-first search from index 0
        dfs(0, [])
        return res

# Main method for testing
if __name__ == "__main__":
    solution = Solution()
    s = "aab"
    result = solution.partition(s)
    for partition in result:
        print(partition)
Complexity Analysis
Time Complexity : The time complexity is O(2^N) due to the exponential number of possible partitions.

Space Complexity : The space complexity is O(N) for the recursion stack and additional space for storing partitions.

'''
class Solution:
    def partition(self, s: str):
        def dfs(index, path):
            if index == len(s):
                res.append(path[:])
                return
            for i in range(index, len(s)):
                if isPalindrome(index, i):
                    path.append(s[index:i+1])
                    dfs(i+1, path)
                    path.pop()

        def isPalindrome(start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True  
        res = []
        dfs(0, [])
        return res