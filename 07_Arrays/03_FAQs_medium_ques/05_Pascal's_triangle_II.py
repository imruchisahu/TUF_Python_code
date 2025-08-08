'''Given an integer r, return all the values in the rth row (1-indexed) in Pascal's Triangle in correct order.



In Pascal's triangle:

The first row has one element with a value of 1.
Each row has one more element in it than its previous row.
The value of each element is equal to the sum of the elements directly above it when arranged in a triangle format.

Examples:
Input: r = 4

Output: [1, 3, 3, 1]

Explanation: The Pascal's Triangle is as follows:

1

1 1

1 2 1

1 3 3 1

....

Thus the 4th row is [1, 3, 3, 1]

Input: r = 5

Output: [1, 4, 6, 4, 1]

Explanation: The Pascal's Triangle is as follows:

1

1 1

1 2 1

1 3 3 1

1 4 6 4 1

....

Thus the 5th row is [1, 4, 6, 4, 1]

Input: r = 6

Output:
[1, 5, 10, 10, 5, 1]
Constraints:
1 <= r <= 30
All values will fit inside a 32-bit integer.

Similar Problems

ntuition:
A naive approach to solve this problem will be to use the formula for the element of rth row and cth column of Pascal's triangle repetitively to find each element in the rth row. The time complexity of this approach will be O(n2) as we need to calculate the value of each element in the nth row.

A better way to solve this is by identifying a pattern in the rows of the Pascal's triangle. The rth row of Pascal's triangle is generated as shown in the figure:

It can be seen that any element in the rth row is of the form:
curr = (prev * (r-i))/(i)
where prev is the previous element in the row and i is the index of the element in the row.

Using this formula, we can generate the rth row of Pascal's triangle in O(n) time complexity.

Approach:
Initialize the list with a size equal to the given row number.
Set the first element of the row to 1, as the first element in every row of Pascal's Triangle is always 1.
Iterate through the row to compute each value using the above formula.
Return the computed row as the final result.
Solution:

Complexity Analysis:
Time Complexity: O(R), where R is the given row number.
A simple loop is used that runs R times and performs constant time oprations in each iteration resulting in a linear time complexity.

Space Complexity: O(1), as no extra space is used.

Note that if the space used to return the row is considered, the space complexity will be O(R) as the space used to store the row is proportional to the row number.

'''
class Solution:
    def pascalTriangleII(self, r):
        ans = [0] * r
        ans[0] = 1
        for i in range(1, r):
            ans[i] = (ans[i - 1] * (r - i)) // i
        return ans
           