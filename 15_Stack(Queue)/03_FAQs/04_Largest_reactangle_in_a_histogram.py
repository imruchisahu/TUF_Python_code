'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1 return the area of the largest rectangle in the histogram.


Examples:
Input: heights = [2, 1, 5, 6, 2, 3]



Output: 10



Explanation: The largest rectangle is highlighted, which has an area of 5*2 = 10 units.

Input: heights = [3, 5, 1, 7, 5, 9]



Output: 15



Explanation: The largest rectangle has an area of 5*3 = 15 units.

Input: heights = [2,4]

Output:
4
Constraints:
  1 <= heights.length <= 105
  0 <= heights[i] <= 104

#Brute
Intuition:
One way to get the maximum rectangle area possible is by considering all the rectangles and then finding the maximum area out of those. To find the area of a rectangle, its height and width must be known. Already given the heights in the question, the only task remaining is to find the width of the rectangle.

The width of a rectangle of current height will depend on the number of rectangles on the left and right having a height greater than or equal to the current height.
Understanding:
Consider the following example:

Hence, the width of the rectangle can be found using the concept of Previous/Next Smaller Elements. The formula for the same is:
       width = nse[ind] - pse[ind] - 1
where, pse[ind] and nse[ind] represent the indices of the previous and next smaller element for the current index.

Thus, the indices of the previous and next smaller elements can be precomputed. This will help in finding the area of possible individual rectangles, out of which the maximum can be returned as the answer.
Approach:
Find the indices of Next smaller elements and Previous smaller elements using Monotonic stack. For elements having no previous smaller element, use -1 as the index. For elements having no next smaller elements, use the size of the array as the index.
Use the precomputed NSE and PSE arrays to determine the width of the rectangle that each bar can form.
For each bar, calculate the area using its height and the distance between the NSE and PSE indices.
Keep track of the maximum area encountered during this process.

class Solution:
    # Function to find the indices of 
    # next smaller elements
    def findNSE(self, arr):
        
        # Size of array
        n = len(arr)
        
        # To store the answer
        ans = [0] * n
        
        # Stack 
        st = []
        
        # Start traversing from the back
        for i in range(n - 1, -1, -1):
            
            # Get the current element
            currEle = arr[i]
            
            # Pop the elements in the stack until 
            # the stack is not empty and the top 
            # element is not the smaller element
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            
            # Update the answer
            ans[i] = st[-1] if st else n
            
            # Push the index of current 
            # element in the stack
            st.append(i)
        
        # Return the answer
        return ans
    
    # Function to find the indices of 
    # previous smaller elements
    def findPSE(self, arr):
        
        # Size of array
        n = len(arr)
        
        # To store the answer
        ans = [0] * n
        
        # Stack 
        st = []
        
        # Traverse on the array
        for i in range(n):
            
            # Get the current element
            currEle = arr[i]
            
            # Pop the elements in the stack until 
            # the stack is not empty and the top 
            # elements is not the smaller element
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            
            # Update the answer
            ans[i] = st[-1] if st else -1
            
            # Push the index of current 
            # element in the stack
            st.append(i)
        
        # Return the answer
        return ans
    
    # Function to find the largest rectangle area
    def largestRectangleArea(self, heights):
        
        # Determine the next and 
        # previous smaller elements
        nse = self.findNSE(heights)
        pse = self.findPSE(heights)
        
        # To store largest area
        largestArea = 0
        
        # To store current area
        area = 0
        
        # Traverse on the array
        for i in range(len(heights)):
            
            # Calculate current area
            area = heights[i] * (nse[i]-pse[i]-1)
            
            # Update largest area
            largestArea = max(largestArea, area)
        
        # Return largest area found
        return largestArea

# Example usage
if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to find the largest rectangle area
    ans = sol.largestRectangleArea(heights)
    
    print("The largest rectangle area is:", ans)

Complexity Analysis:
Time Complexity: O(N) (where N is the size of the given array)

Precomputing PSE and NSE arrays take O(2N) time each.
Traversing the given histogram once to find the maximum area takes O(N) time.
Space Complexity: O(N)
Finding the PSE and NSE arrays uses stack that takes O(N) space each.
Storing the PSE and NSE arrays take O(N) space each.


#optimal
Intuition:
In the earlier solution, precomputing the PSE and NSE arrays was contributing to multiple traversals. This can be avoided by finding the PSE on the go. But the question of finding the NSE still remains.

Understanding:
Consider the following dry run for finding the indices of previous smaller elements using Stack:

Hence, the index of NSE is known while popping the elements from the stack, serving as a backward traversal. Hence, knowing the PSE and NSE, the width of the rectangle can be determined using the formula:
       width = nse[ind] - pse[ind] - 1
where, pse[ind] and nse[ind] represent the indices of the previous and next smaller element for the current index.

Handling remaining bars:
Since the areas of only those rectangles are considered that are popped from the stack, to ensure all the possible heights are considered for areas, all the elements must be popped from the stack even after the traversal of the array is complete. For such elements (that remain in the stack after traversal), the index of the next smaller element will be set to the size of the array, as there is no next smaller element.
Approach:
Initialize an empty stack to store indices of the histogram bars. For each height in the histogram, maintain a stack of indices where the heights are in increasing order.
If the current height is shorter than the height at the top of the stack, it means the rectangle with the height at the top of the stack ends at the current bar.
For each popped bar from the stack, calculate the width using the current index as the next smaller element (NSE) and the index of the new top of the stack as the previous smaller element (PSE).
Compute the area and update the maximum area found. After the traversal, the remaining bars in the stack have their NSE as the end of the array.
Calculate the area for these bars similarly and update the maximum area.

class Solution:
    # Function to find the largest rectangle area
    def largestRectangleArea(self, heights):
        n = len(heights)  # Size of array
        
        # Stack 
        st = []
        
        # To store largest area
        largestArea = 0
        
        # To store current area
        area = 0
        
        # To store the indices of next 
        # and previous smaller elements
        nse = pse = 0
        
        # Traverse on the array
        for i in range(n):
            
            # Pop the elements in the stack until 
            # the stack is not empty and the top 
            # elements is not the smaller element
            while st and heights[st[-1]] >= heights[i]:
                
                # Get the index of top of stack
                ind = st.pop()
                
                # Update the index of previous smaller element
                pse = st[-1] if st else -1
                
                # Next smaller element index for \
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

# Example usage
if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to find the largest rectangle area
    ans = sol.largestRectangleArea(heights)
    
    print("The largest rectangle area is:", ans)

Complexity Analysis:
Time Complexity: O(N) (where N is the size of the given array)

Traversing all the elements of array takes O(N) time.
All the elements are pushed in and popped out from the stack once taking O(N) time.
Space Complexity: O(N)
The stack space used to find the previous smaller element during traversal can go up to O(N).

  '''
class Solution:
    def largestRectangleArea(self, heights):
      n = len(heights)  
      st = []
      largestArea = 0
      area= 0
      nse = pse = 0
      for i in range(n):
          while st and heights[st[-1]] >= heights[i]:
              ind = st.pop()
              pse = st[-1] if st else -1
              nse = i
              area = heights[ind] * (nse - pse - 1)
              largestArea = max(largestArea, area)
          st.append(i)
      
      # For elements that are not popped from stack
      while st:
          nse = n
          ind = st.pop()
          pse = st[-1] if st else -1
          area = heights[ind] * (nse - pse - 1)
          largestArea = max(largestArea, area)
      return largestArea