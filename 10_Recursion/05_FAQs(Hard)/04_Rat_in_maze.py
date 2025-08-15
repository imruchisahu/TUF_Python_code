'''Given a grid of dimensions n x n. A rat is placed at coordinates (0, 0) and wants to reach at coordinates (n-1, n-1).

Find all possible paths that rat can take to travel from (0, 0) to (n-1, n-1). The directions in which rat can move are 'U' (up) , 'D' (down) , 'L' (left) , 'R' (right).

The value 0 in grid denotes that the cell is blocked and rat cannot use that cell for travelling, whereas value 1 represents that rat can travel through the cell. If the cell (0, 0) has 0 value, then mouse cannot move to any other cell.

Note :

In a path no cell can be visited more than once.
If there is no possible path then return empty vector.

Examples:
Input : n = 4 , grid = [ [1, 0, 0, 0] , [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1] ]

Output : [ "DDRDRR" , "DRDDRR" ]

Explanation : The rat has two different path to reach (3, 3).

The first path is (0, 0) => (1, 0) => (2, 0) => (2, 1) => (3, 1) => (3, 2) => (3, 3).

The second path is (0,0) => (1,0) => (1,1) => (2,1) => (3,1) => (3,2) => (3,3).

Input : n = 2 , grid = [ [1, 0] , [1, 0] ]

Output : -1

Explanation : There is no path that rat can choose to travel from (0,0) to (1,1).

Input : n = 3 , grid = [ [1, 0, 0] , [1, 1, 0], [0, 1, 1] ]

Output:
[ 'DDRR' ]
[ 'DRRD' ]
[ 'RRDD' ]
[ 'DRDR']

Submit
Constraints:
2 <= n <= 5
0 <= grid[i][j] <= 1

Real-life Problem Solving
Imagine being in a maze with walls and open paths, starting at the top-left corner and needing to reach the bottom-right corner. The task involves finding all possible paths from the start to the destination. Each step taken must be carefully considered to avoid walls and ensure a valid route to the end. If a path is blocked, the process involves backtracking and trying another direction, keeping track of each step to ensure no part of the maze is visited twice unnecessarily.

Intuition Behind Recursion Process
This maze-solving process can be translated into a recursive function. The starting position in the maze is equivalent to the initial call of the recursive function. Each possible direction (up, down, left, right) corresponds to a recursive call exploring that direction. Upon finding a valid move (an open path), the current path is updated and the function proceeds to the next step. When a dead end is encountered (a blocked path), the function backtracks to the previous step and explores alternative directions. This recursive exploration continues until the destination is reached, recording all possible paths.

Approach
Start from the initial position (0,0) in the grid.
Check if the current position is the destination. If so, add the current path to the results.
If the current cell is blocked (value is 0), return.
Mark the current cell as visited by setting its value to 0.
Explore all possible directions (up, down, left, right) from the current cell:
Move up if the current cell is not in the topmost row.
Move left if the current cell is not in the leftmost column.
Move down if the current cell is not in the bottommost row.
Move right if the current cell is not in the rightmost column.
After exploring all directions, unmark the current cell by resetting its value to 1 to allow other paths to pass through it.
Repeat the above steps recursively until all possible paths are explored.
Sort the resulting paths alphabetically.

class Solution:
    def __init__(self):
        self.result = []

    # Recursive function to find paths
    def path(self, m, x, y, dir, n):
        # If destination is reached, add path to result
        if x == n - 1 and y == n - 1:
            self.result.append(dir)
            return

        # If cell is blocked, return
        if m[x][y] == 0:
            return

        # Mark cell as visited by setting it to 0
        m[x][y] = 0

        # Move up if possible
        if x > 0:
            self.path(m, x - 1, y, dir + 'U', n)
        # Move left if possible
        if y > 0:
            self.path(m, x, y - 1, dir + 'L', n)
        # Move down if possible
        if x < n - 1:
            self.path(m, x + 1, y, dir + 'D', n)
        # Move right if possible
        if y < n - 1:
            self.path(m, x, y + 1, dir + 'R', n)

        # Unmark cell as visited by setting it to 1
        m[x][y] = 1

    def findPath(self, grid):
        n = len(grid)
        self.result = []

        # If starting or ending cell is blocked, return empty result
        if grid[0][0] == 0 or grid[n - 1][n - 1] == 0:
            return self.result

        # Start finding paths from (0, 0)
        self.path(grid, 0, 0, "", n)

        # Sort the result paths
        self.result.sort()

        return self.result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    grid = [
        [1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1],
        [0, 1, 0, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1]
    ]

    paths = sol.findPath(grid)

    for path in paths:
        print(path)
Complexity Analysis
Time Complexity : The time complexity is O(4^(N^2)) due to recursion exploring all paths in the grid.

Space Complexity :The space complexity is O(N^2) for the recursion stack and result storage.
'''
class Solution:
    def __init__(self):
        self.result = []
    def path(self, m, x, y, dir, n):
        if x == n - 1 and y == n - 1:
            self.result.append(dir)
            return

        # If cell is blocked, return
        if m[x][y] == 0:
            return

        # Mark cell as visited by setting it to 0
        m[x][y] = 0

        # Move up if possible
        if x > 0:
            self.path(m, x - 1, y, dir + 'U', n)
        # Move left if possible
        if y > 0:
            self.path(m, x, y - 1, dir + 'L', n)
        # Move down if possible
        if x < n - 1:
            self.path(m, x + 1, y, dir + 'D', n)
        # Move right if possible
        if y < n - 1:
            self.path(m, x, y + 1, dir + 'R', n)

        # Unmark cell as visited by setting it to 1
        m[x][y] = 1

    def findPath(self, grid):
        n = len(grid)
        self.result = []

        # If starting or ending cell is blocked, return empty result
        if grid[0][0] == 0 or grid[n - 1][n - 1] == 0:
            return self.result

        # Start finding paths from (0, 0)
        self.path(grid, 0, 0, "", n)
        self.result.sort()
        return self.result