'''
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image. Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.



To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same colour as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same colour as the starting pixel), and so on. Replace the colour of all of the aforementioned pixels with the newColor.


Examples:


Input: image = [ [1, 1, 1], [1, 1, 0], [1, 0, 1] ], sr = 1, sc = 1, newColor = 2

Output: [ [2, 2, 2], [2, 2, 0], [2, 0, 1] ]

Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Input: image = [ [0, 1, 0], [1, 1, 0], [0, 0, 1] ], sr = 2, sc = 2, newColor = 3

Output: [ [0, 1, 0], [1, 1, 0], [0, 0, 3] ]

Explanation: Starting from the pixel at position (2, 2) (i.e., the blue pixel), we flood fill all adjacent pixels that have the same color as the starting pixel. In this case, only the pixel at position (2, 2) itself is of the same color. So, only that pixel gets colored with the new color, resulting in the updated image.

Input: image = [ [1, 1, 1], [1, 1, 0], [1, 0, 1] ], sr = 1, sc = 1, newColor = 0

Output:
[ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
[ [0, 0, 0], [0, 0, 0], [1, 0, 1] ]
[ [0, 0, 0], [0, 0, 0], [1, 0, 0] ]
[ [0, 0, 0], [0, 0, 0], [0, 0, 1] ]

Submit
Constraints:
·  n == image.length

·  m == image[i].length

·  1 <= m, n <= 50

·  0 <= image[i][j], color < 216

·  0 <= sr < n

·  0 <= sc < m

Intuition:
How to solve this problem using a graph?
Think of all the pixels in the image as nodes or vertices which are connected through each other via 4 edges.

Given the starting pixel, any traversal algorithm can be used to find all the neighbors having similar pixel value. During the traversal, each pixel value can be changed to the new color value to get the flood filled image.

How to traverse the neighbours efficiently?
The 4 neighbours of the current cell can be shown like this:


For efficient traversal of all neighboring pixels, the delRow and delCol arrays can be used where:

delRow = {-1, 0, 1, 0}
delCol = {0, 1, 0, -1}

Approach:
Initialise a new image to store the image after flood fill. (The given image can be used for the same but it is considered a good practice if the given input is not altered.)
To navigate to the neighboring pixels, direction vectors are defined for moving up, right, down, and left. A helper function checks if a pixel is within the bounds of the image. This ensures that the traversal does not go out of the image boundary.
Starting from the given pixel, a recursive DFS traversal is performed during which all the pixels having same initial color are marked with new color in the new image.
Once the traversal terminates, the new image stores the flood filled image.

class Solution:
    def __init__(self):
        # delRow and delCol for neighbors
        self.delRow = [-1, 0, 1, 0]
        self.delCol = [0, 1, 0, -1]
    
    def isValid(self, i, j, n, m):
        # Return false if pixel is invalid
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= m:
            return False
        # Return true if pixel is valid
        return True
    
    def dfs(self, row, col, ans, image, newColor, iniColor):
        # color with new color
        ans[row][col] = newColor
        
        # Getting the dimensions of image
        n = len(image)
        m = len(image[0])
        
        # Traverse the 4 neighbors
        for i in range(4):
            # Coordinates of new pixel
            nrow = row + self.delRow[i]
            ncol = col + self.delCol[i]
            
            # check for valid, unvisited pixels
            # having same initial color
            if (
                self.isValid(nrow, ncol, n, m) and 
                image[nrow][ncol] == iniColor and
                ans[nrow][ncol] != newColor
            ):
                # Recursively perform DFS
                self.dfs(nrow, ncol, ans, image, newColor, iniColor)
    
    def floodFill(self, image, sr, sc, newColor):
        # Store initial color
        iniColor = image[sr][sc]
        
        # To store the updated image
        ans = [row[:] for row in image]
        
        # Start DFS traversal from start cell
        self.dfs(sr, sc, ans, image, newColor, iniColor)
        
        # Return the answer image
        return ans

# Testing the function
image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
sr, sc = 1, 1
newColor = 2

sol = Solution()
ans = sol.floodFill(image, sr, sc, newColor)

print("Image after performing flood fill algorithm:\n")
for row in ans:
    print(" ".join(map(str, row)))

Complexity Analysis:
Time Complexity: O(N*M) (where N and M are the dimensions of image)

In the worst case, all the pixel will have same color, DFS call will be made for (N*M) nodes.
For every pixel, its four neighbors are traversed, taking O(4*N*M) time.
Space Complexity: O(N*M)

Extra space for new image takes O(N*M) space.
Recusive stack space for DFS calls will take at most O(N*M) space.
'''
class Solution:
    def __init__(self):
        self.delRow = [-1, 0, 1, 0]
        self.delCol = [0, 1, 0, -1]
    
    def isValid(self, i, j, n, m):
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= m:
            return False
        return True
    
    def dfs(self, row, col, ans, image, newColor, iniColor):
        ans[row][col] = newColor
        n = len(image)
        m = len(image[0])
        for i in range(4):
            nrow = row + self.delRow[i]
            ncol = col + self.delCol[i]
            
            # check for valid, unvisited pixels
            # having same initial color
            if (
                self.isValid(nrow, ncol, n, m) and 
                image[nrow][ncol] == iniColor and
                ans[nrow][ncol] != newColor
            ):
                self.dfs(nrow, ncol, ans, image, newColor, iniColor)
    
    def floodFill(self, image, sr, sc, newColor):
        iniColor = image[sr][sc]
        ans = [row[:] for row in image]
        self.dfs(sr, sc, ans, image, newColor, iniColor)
        return ans

      