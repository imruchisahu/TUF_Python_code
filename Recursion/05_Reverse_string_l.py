'''Given an input string as an array of characters, write a function that reverses the string.


Examples:
Input : s = ["h", "e", "l", "l", "o"]

Output : ["o", "l", "l", "e", "h"]

Explanation : The given string is s = "hello" and after reversing it becomes s = "olleh".

Input : s = ["b", "y", "e" ]

Output : ["e", "y", "b"]

Explanation : The given string is s = "bye" and after reversing it becomes s = "eyb".

Input : s = ["h", "a", "n", "n", "a", "h"]

Output:
["h", "a", "n", "n", "a", "h"]
Constraints:
1 <= s.length <= 103
s consist of only lowercase and uppercase English characters.

Intuition
Reversing a string through recursion involves conceptualizing the problem in smaller segments. The process identifies a base case where the left index surpasses or equals the right index, signaling completion. Characters at the left and right indices are swapped, and a recursive call is initiated with updated indices (left incremented, right decremented). This sequence of swaps ensures the entire string is reversed.

Approach
Identify the Base Case: Determine the condition under which the recursion should stop. For reversing a string, the recursion stops when the left index is greater than or equal to the right index. This indicates that we have reached the middle of the string and all necessary character swaps have been made.
Swap Characters at Indices: Perform the swap operation between the characters at the current left and right indices. This action exchanges the characters at the ends of the string segment being processed, which moves towards reversing the string.
Make Recursive Calls: After swapping, call the recursive function again with updated indices: increment the left index and decrement the right index. This step processes the next pair of characters moving inward until the base case is met.
Dry Run


Complexity Analysis
Time Complexity: O(N) - Each character in the string is processed exactly once, resulting in a linear time complexity relative to the length of the string.

Space Complexity: O(N) - This is due to the recursion stack used in the process. In the worst case, the depth of the recursion is equal to the length of the string, leading to linear space complexity.

class Solution:
    
    # Function to reverse the given string
    def reverseString(self, s):
        
        # Recursive function to reverse the 
        # string character by character 
        def reverse(s, left, right):
            # Base case
            if left >= right:
                return 
            
            # Swap characters at left and right positions
            s[left], s[right] = s[right], s[left]
            
            # Recursive call with updated indices
            reverse(s, left + 1, right - 1)
        
        reverse(s, 0, len(s) - 1)
        return s

# Main function to test the solution
if __name__ == "__main__":
    solution = Solution()
    s = ['h', 'e', 'l', 'l', 'o']
    
    # Function call to reverse the given string
    reversed_s = solution.reverseString(s)
    print(reversed_s)


'''
class Solution:
    def reverseString(self, s):
        def reverse(s, left, right):
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            reverse(s, left + 1, right - 1)
        reverse(s, 0, len(s) - 1)
        return s

res=Solution()
s = ['h', 'e', 'l', 'l', 'o']
print(res.reverseString(s))


