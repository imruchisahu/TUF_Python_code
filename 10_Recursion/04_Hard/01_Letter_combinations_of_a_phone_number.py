'''
Given a string consisting of digits from 2 to 9 (inclusive). Return all possible letter combinations that the number can represent.



Mapping of digits to letters is given in first example.


Examples:
Input : digits = "34"

Output : [ "dg", "dh", "di", "eg", "eh", "ei", "fg", "fh", "fi" ]

Explanation : The 3 is mapped with "def" and 4 is mapped with "ghi".

So all possible combination by replacing the digits with characters are shown in output.



Input : digits = "3"

Output : [ "d", "e", "f" ]

Explanation : The 3 is mapped with "def".

Input : digits = "8"

Output:
[ "t", "u", "v" ]
Constraints:
0 <= digits.length <= 4
digts[i] contains digitd from [2,9].

Intuition
Imagine needing to create all possible words using the letters associated with each digit on a telephone keypad. Start with an empty word and choose a letter from the set of letters corresponding to the first digit, then move to the next digit, and continue until there are no more digits. This process is repeated for each combination of letters, resulting in all possible words.

Begin by thinking of the problem as constructing words step by step. Start with an empty string and at each step, append a letter corresponding to the current digit. Progress to the next digit and repeat the process. When the end of the digit string is reached, a complete word has been formed. This recursive approach mimics a systematic way of exploring all possible combinations by building words character by character, moving through each digit's letters in turn, and backtracking when necessary to explore new combinations.

Approach
Initialize a mapping of digits to their corresponding letters, and an empty list to store results.
Define a recursive helper function that takes the current digit index, the current string combination, and the result list as arguments.
In the base case, when the index equals the length of the digits string, add the current combination to the result list.
For the current digit, iterate over its corresponding letters and recursively call the helper function with the next index and the updated combination string.


class Solution:
    def __init__(self):
        # Mapping digits to corresponding characters
        self.map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    # Recursive helper function to generate combinations
    def helper(self, digits, ans, index, current):
        # Base case: if index reaches the end of digits
        if index == len(digits):
            # Add the current combination to the answer
            ans.append(current)
            return
        # Get characters corresponding to the current digit
        s = self.map[int(digits[index])]
        # Loop through the corresponding characters
        for char in s:
            # Recursively call function with next index
            # Add current character to the string
            self.helper(digits, ans, index + 1, current + char)

    # Function to get all letter combinations for a given digit string
    def letterCombinations(self, digits):
        ans = []  # List to store results
        # Return empty list if digits string is empty
        if not digits:
            return ans
        # Initiate recursive function
        self.helper(digits, ans, 0, "")
        return ans  # Return the result

# Main section to demonstrate the usage of the Solution class
if __name__ == "__main__":
    solution = Solution()
    digits = "23"  # Input digits
    result = solution.letterCombinations(digits)  # Get combinations

    # Print the results
    print(result)
Complexity Analysis
Time Complexity O(4^N * N), where n is the length of the input digits. This is because each digit can map to up to 4 letters and there are n digits.

Space Complexity: O(N), where n is the length of the input digits. This is due to the recursion stack depth.
'''
class Solution:
    def __init__(self):
        self.map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    def helper(self, digits, ans, index, current):
        if index == len(digits):
            ans.append(current)
            return
        s = self.map[int(digits[index])]
        for char in s:
            self.helper(digits, ans, index + 1, current + char)
    def letterCombinations(self, digits):
        ans = [] 
        if not digits:
            return ans
        self.helper(digits, ans, 0, "")
        return ans  
    