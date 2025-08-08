'''Given an integer n, return the first n (1-Indexed) rows of Pascal's triangle.



In Pascal's triangle:

The first row has one element with a value of 1.
Each row has one more element in it than its previous row.
The value of each element is equal to the sum of the elements directly above it when arranged in a triangle format.

Examples:
Input: n = 4

Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

Explanation: The Pascal's Triangle is as follows:

1

1 1

1 2 1

1 3 3 1

1st Row has its value set to 1.

All other cells take their value as the sum of the values directly above them

Input: n = 5

Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

Explanation: The Pascal's Triangle is as follows:

1

1 1

1 2 1

1 3 3 1

1 4 6 4 1

1st Row has its value set to 1.

All other cells take their value as the sum of the values directly above them

Input: n = 3

Output:
[[1], [1, 1], [1, 2, 1]]
Constraints:
1 <= n <= 30
All values will fit inside a 32-bit integer.

Hint 1

Hint 2
Intuition:
A naive way to solve this problem will be to calculate the element n and c (where n is the given row number and c is the column number that will vary from 1 to n) for every column from 1 to n and for every row, using the process used in Pascal Triangle-I. However, this will result in an O(N3) time complexity.

A better way to solve this problem will be to generate every row from 1 to n using the method discussed in Pascal Triangle-II and store the entire Pascal's Triangle in a 2D list. Once the entire Pascal's Triangle is generated, we can return the triangle.

Approach:
Create a 2D list to hold the values of Pascal's Triangle.
For each row i from 0 to n-1, create a list to hold the values of the current row.
Generate the row i using the method discussed in Pascal's triangle-II.
Append the current row to the triangle. Once all rows are computed, return the triangle.
Solution:
Time Complexity: O(N2), generating each row takes linear time relative to its size, and there are N rows, leading to a total time complexity of O(N2).

Space Complexity: O(N2), storing the entire Pascal's Triangle requires space proportional to the sum of the first N natural numbers, resulting in O(N2) space complexity.



class Solution:
    # Function to generate a single row of Pascal's Triangle
    def generateRow(self, row):
        ans = 1
        ansRow = []
        
        # Inserting the 1st element
        ansRow.append(1)

        # Calculate the rest of the elements
        for col in range(1, row):
            ans = ans * (row - col)
            ans = ans // col
            ansRow.append(ans)
        
        return ansRow  # Return the computed row

    # Function to generate Pascal's Triangle up to n rows
    def pascalTriangleIII(self, n):
        pascalTriangle = []

        # Compute the entire Pascal's Triangle
        for row in range(1, n + 1):
            pascalTriangle.append(self.generateRow(row))
        
        #return the pascalTriangle
        return pascalTriangle


if __name__ == "__main__":
    n = 5
    sol = Solution()

    # Generate Pascal's Triangle with n rows
    pascalTriangle = sol.pascalTriangleIII(n)

    # Output the Pascal's Triangle
    for row in pascalTriangle:
        for element in row:
            print(element, end=" ")
        print()


'''
class Solution:
    def generateRow(self, n):
        ans=1
        ansRow=[]
        ansRow.append(1)
        for col in range(1, n):
            ans = ans * ( n-col)
            ans = ans // col
            ansRow.append(ans)
        return ansRow

    def pascalTriangleIII(self, n):
        pascalTriangle = []
        for row in range(1, n+1):
            pascalTriangle.append(self.generateRow(row))
        return pascalTriangle