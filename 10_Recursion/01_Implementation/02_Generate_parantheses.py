'''
Given an integer n.Generate all possible combinations of well-formed parentheses of length 2 x N.


Examples:
Input : n = 3

Output : [ "((()))" , "(()())" , "(())()" , "()(())" , "()()()" ]

Input : 2

Output : [ "(())" , "()()" ]

Input : 1

Output:
()
Constraints:
1 <= n <= 8

Real-Life Intuition
To understand the problem better visualize arranging a set of opening and closing brackets to form valid sequences. Think of it like scheduling tasks where each scheduled meeting needs a corresponding end time. To solve this, start with an empty schedule (or an opening bracket) and recursively decide whether to add a meeting (an opening bracket if more are allowed) or a not scheduled one (closing bracket if it pairs with an existing opening bracket). Each step ensures that the schedule remains balanced and all meetings are correctly paired. This approach systematically explores all possible valid sequences by following rules similar to ensuring that every start time has an end time, and no end time precedes a start time.

Approach
Begin with zero open and zero close parentheses. Initialize an empty string and a list to store the valid combinations.
At each step, decide to add an open parenthesis if there are more available. Add a close parenthesis if it is valid (i.e., if the number of close parentheses used is less than the number of open parentheses).
Base Case: When the number of open and close parentheses used equals the total number of pairs, the current string is a valid combination. Add this string to the list of results.
Recursive Calls: Use recursion to explore both adding an open parenthesis and adding a close parenthesis, if permissible, to build all possible valid combinations.

class Solution:
    def generateParenthesis(self, n: int):
        """
        Generates all combinations of n pairs of balanced parentheses.
        
        :param n: The number of pairs of parentheses.
        :return: A list containing all valid combinations of parentheses.
        """
        # List to store the result
        ans = []
        # Start the recursive generation with initial values
        self._generate(0, 0, n, "", ans)
        return ans

    def _generate(self, open_count: int, close_count: int, n: int, current: str, ans: list):
        """
        A recursive helper function to generate all combinations
        of balanced parentheses.

        :param open_count: The number of open parentheses used so far.
        :param close_count: The number of close parentheses used so far.
        :param n: The total number of pairs of parentheses.
        :param current: The current string being built.
        :param ans: The list storing all valid combinations.
        """
        # Base case: if the number of open and close parentheses used
        # is equal to the total number of pairs, add the string to the result.
        if open_count == close_count == n:
            ans.append(current)
            return

        # If the number of open parentheses used is less than the total
        # number of pairs, add an open parenthesis and call the function recursively.
        if open_count < n:
            self._generate(open_count + 1, close_count, n, current + '(', ans)

        # If the number of close parentheses used is less than the number
        # of open parentheses, add a close parenthesis and call the function recursively.
        if close_count < open_count:
            self._generate(open_count, close_count + 1, n, current + ')', ans)


# Example usage
if __name__ == "__main__":
    sol = Solution()
    n = 3  # Example input
    result = sol.generateParenthesis(n)

    print(f"All combinations of balanced parentheses for n = {n} are:")
    for combination in result:
        print(combination)

        
Complexity Analysis
Time Complexity: O((4^n / sqrt(n))*n), where n is the number of pairs of parentheses. This complexity arises because each step involves branching into two possibilities, resulting in an exponential number of possibilities, reduced by the Catalan number formula for valid combinations.

Space Complexity: O((4^n / sqrt(n))*n), primarily due to the recursion stack and the storage required for the result list of valid combinations. The space is proportional to the number of valid combinations generated.

'''
class Solution:
    def generateParenthesis(self, n):
        ans = []
        self._generate(0, 0, n, "", ans)
        return ans

    def _generate(self, open_count: int, close_count: int, n: int, current: str, ans: list):
        if open_count == close_count == n:
            ans.append(current)
            return
        if open_count < n:
            self._generate(open_count + 1, close_count, n, current + '(', ans)
        if close_count < open_count:
            self._generate(open_count, close_count + 1, n, current + ')', ans)
