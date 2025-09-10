'''
Given a m x n binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.


Examples:
Input: matrix = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]

Output: 6

Explanation: The highlighted part depicts the rectangle with the largest area i.e. 6.



Input : matrix = [[1]] 

Output: 1 

Explanation: In this case, there is only one rectangle with area 1.

Input: matrix = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1]]

Output:
3
Constraints:
  1<=n,m<=1000
  0<=matrix[i][j]<=1
  
  Intuition:
A clever way to approach this problem is by breaking the problem into smaller subproblems using the concept discussed in the problem Largest rectangle in a histogram. The given matrix can be seen from different ground levels. Each ground can be treated as a histogram, and the columns of 1s attached from the ground represent the heights of the bars for the current histogram. This way the problem boils down to finding the largest rectangle in all the histograms.

Now, to find the height of bars for a particular ground level (histogram), traversing the matrix again and again will be inefficient. Instead, the heights of bars can be determined by traversing the matrix only once by using the concept of Prefix Sum.

Understanding:
Since the heights of the bars are the main concern, the prefix sum must be calculated column-wise. This will make sure that while traversing in a column-order fashion, the heights are added up. But if in any place, a zero is found, the height of 1s above it will not be considered as there is no contact of continuous 1s with the ground for that particular histogram.
Approach:
Convert the binary matrix into a matrix of histogram heights using the prefix sum technique. Each cell in the histogram matrix represents the height of consecutive 1s ending at that cell.
For each column, compute the height of consecutive 1's for each row. If a cell contains a 0, reset the height to 0.
For each row in the histogram matrix, treat it as a histogram and compute the largest rectangle area that can be formed using that row. This is achieved using a stack-based approach to find the largest rectangle in a histogram.
Track the maximum rectangle area found across all rows and return it as the result.

class Solution:
    # Function to find the largest rectangle area
    def largestRectangleArea(self, heights):
        
        n = len(heights) # Size of array
        
        # Stack 
        st = []
        
        # To store largest area
        largestArea = 0
        
        # To store current area
        area = 0
        
        # To store the indices of next 
        # and previous smaller elements 
        nse, pse = 0, 0
        
        # Traverse on the array
        for i in range(n):
            
            # Pop the elements in the stack until 
            # the stack is not empty and the top 
            # elements is not the smaller element 
            while st and heights[st[-1]] >= heights[i]:
                      
                # Get the index of top of stack
                ind = st.pop()
                
                # Update the index of 
                # previous smaller element 
                pse = st[-1] if st else -1
                
                # Next smaller element index for 
                # the popped element is current index 
                nse = i
                
                # Calculate the area of the popped element
                area = heights[ind] * (nse - pse - 1)
                
                # Update the maximum area
                largestArea = max(largestArea, area)
            
            # Push the current index in stack
            st.append(i)
        
        # For elements that are not popped from stack
        while st:
            
            # NSE for such elements is size of array
            nse = n
            
            # Get the index of top of stack
            ind = st.pop()
            
            # Update the previous smaller element
            pse = st[-1] if st else -1
            
            # Calculate the area of the popped element
            area = heights[ind] * (nse - pse - 1)
            
            # Update the maximum area
            largestArea = max(largestArea, area)
        
        # Return largest area found
        return largestArea
    
    # Function to find the largest 
    # rectangle area containing all 1s 
    def maximalAreaOfSubMatrixOfAll1(self, matrix):
        
        # Determine the size of matrix
        n = len(matrix)
        m = len(matrix[0])
        
        # Prefix sum matric to store heights 
        # for different ground levels 
        prefixSum = [[0] * m for _ in range(n)]
        
        # Fill up the prefix sum matrix column wise
        for j in range(m):
            sum = 0
            
            for i in range(n):
                sum += matrix[i][j]
                
                # If there is no base present
                if matrix[i][j] == 0:
                    prefixSum[i][j] = 0
                    sum = 0
                else:
                    # Store the height
                    prefixSum[i][j] = sum
        
        # To store the maximum area
        maxArea = 0
        
        # Traverse for different levels of ground
        for i in range(n):
            
            # Get the largest area for current level
            area = self.largestRectangleArea(prefixSum[i])
            
            # Update the maximum area
            maxArea = max(area, maxArea)
        
        # Return the maximum area
        return maxArea

# Main code
if __name__ == "__main__":
    matrix = [
        [1, 0, 1, 0, 0], 
        [1, 0, 1, 1, 1], 
        [1, 1, 1, 1, 1], 
        [1, 0, 0, 1, 0]
    ]
    
    # Creating an instance of Solution class
    sol = Solution() 
    
    # Function call to find the largest rectangle area containing all 1s
    ans = sol.maximalAreaOfSubMatrixOfAll1(matrix)
    
    print("The largest rectangle area containing all 1s is:", ans)

Complexity Analysis:
Time Complexity: O(N*M) (where N and M are the dimensions of the given matrix)
Filling the prefix sum matrix takes O(N*M) time.
Every row (of length M) is treated as a histogram for which the largest histogram is found in linear(O(2*M)) time taking overall O(N*M) time.
Space Complexity: O(N*M)

The prefix sum array takes up O(N*M) space.
Finding the largest rectangle in each histogram (of length M) takes O(M) space due to stack.

'''
class Solution:
  def largestRectangleArea(self, heights):
    n = len(heights)
    st = []
    largestArea = 0
    area = 0
    nse, pse = 0, 0
    for i in range(n):    
      while st and heights[st[-1]] >= heights[i]:
        ind = st.pop()
        pse = st[-1] if st else -1  
        nse = i
        area = heights[ind] * (nse - pse - 1)     
        largestArea = max(largestArea, area)
      st.append(i)     
    while st:
      nse = n   
      ind = st.pop()    
      pse = st[-1] if st else -1  
      area = heights[ind] * (nse - pse - 1)
      largestArea = max(largestArea, area)
    return largestArea
  def maximalAreaOfSubMatrixOfAll1(self, matrix):
    n = len(matrix)
    m = len(matrix[0])         
    prefixSum = [[0] * m for _ in range(n)]
    for j in range(m):
      sum = 0
      for i in range(n):
        sum += matrix[i][j]            
        if matrix[i][j] == 0:
            prefixSum[i][j] = 0
            sum = 0
        else:
            prefixSum[i][j] = sum
    maxArea = 0
    for i in range(n):
        area = self.largestRectangleArea(prefixSum[i])
        maxArea = max(area, maxArea)
    return maxArea
