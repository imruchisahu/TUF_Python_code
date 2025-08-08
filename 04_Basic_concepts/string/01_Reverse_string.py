'''Given a string, the task is to reverse it. The string is represented by an array of characters s. Perform the reversal in place with O(1) extra memory.



Note: no need to return anything, modify the given list.


Examples:
Input : s = ["h", "e" ,"l" ,"l" ,"o"]

Output : ["o", "l", "l", "e", "h"]

Explanation : The given string is s = "hello" and after reversing it becomes s = "olleh".

Input : s = ["b", "y" ,"e" ]

Output : ["e", "y", "b"]

Explanation : The given string is s = "bye" and after reversing it becomes s = "eyb".

Input : s = ["h", "a" ,"n" ,"n" ,"a", "h"]

Output:
["h", "a" ,"n" ,"n" ,"a", "h"]
Constraints:
1 <= s.length <= 105
s consist of only lowercase and uppercase English characters.
Intuition
To reverse a string, the stack data structure is particularly useful due to its Last-In-First-Out (LIFO) principle. The thought process involves pushing each character of the string onto the stack, which naturally reverses their order. When characters are then popped off the stack, they are retrieved in the reverse sequence from their original arrangement. This approach efficiently leverages the stack's properties to achieve the desired reversal of the string.

Approach
Create an empty stack to store characters. Iterate over the given string from the first character to the last.
During each iteration, push the current character onto the stack. After completing the iteration, initialize a while loop to extract characters from the stack.
In each iteration of the while loop, pop the top character from the stack and append it to a new string or directly modify the original string to reverse its content.

Complexity Analysis
Time Complexity O(N) - Linear time complexity, where N is the length of the string. The algorithm iterates over the string once to push characters onto the stack and then iterates again to pop characters from the stack.

Space Complexity O(N) - Linear space complexity. This is due to the usage of the extra data structure of stack, which grows linearly with the size of the input string.

class Solution:
    # Function to reverse a string
    def reverseString(self, s):
        stack = []

        # Push characters onto the stack
        for c in s:
            stack.append(c)

        # Pop characters from the stack to reverse the string
        for i in range(len(s)):
            s[i] = stack.pop()

        return

# Main function
if __name__ == "__main__":
    str_list = ['h', 'e', 'l', 'l', 'o']

    # Creating an instance of Solution class
    sol = Solution()

    # Function call to reverse the string
    sol.reverseString(str_list)

    print("".join(str_list))




'''
# class Solution: 
#     def reverseString(self, s):
#         #your code goes here
#         l=[]
#         for char in s:
#             l.append(char)
#         for i in range(len(s)):
#             s[i] = l.pop()
#         return


class Solution:
    def reverseString(self, s):
        #use O(1) space
        left, right = 0, len(s) - 1
        while left < right:
            # Swap the elements
            s[left], s[right] = s[right], s[left]
            # Move the pointers
            left += 1
            right -= 1
        return s
s1=Solution()
s=['h', 'e', 'l', 'l', 'o']
print(s1.reverseString(s))
