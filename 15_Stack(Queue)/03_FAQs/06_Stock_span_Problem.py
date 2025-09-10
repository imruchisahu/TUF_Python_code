'''
Given an array arr of size n, where each element arr[i] represents the stock price on day i. Calculate the span of stock prices for each day.



The span Si for a specific day i is defined as the maximum number of consecutive previous days (including the current day) for which the stock price was less than or equal to the price on day i.


Examples:
Input: n = 7, arr = [120, 100, 60, 80, 90, 110, 115]

Output: [1, 1, 1, 2, 3, 5, 6]

Explanation:

Traversing the given input span:

120 is greater than or equal to 120 and there are no more elements behind it so the span is 1,

100 is greater than or equal to 100 and smaller than 120 so the span is 1,

60 is greater than or equal to 60 and smaller than 100 so the span is 1,

80 is greater than or equal to 60, 80 and smaller than 100 so the span is 2,

90 is greater than or equal to 60, 80, 90 and smaller than 100 so the span is 3,

110 is greater than or equal to 60, 80, 90, 100, 110 and smaller than 120 so the span is 5,

115 is greater than or equal to all previous elements and smaller than 120 so the span is 6.

Hence the output will be 1 1 1 2 3 5 6.

Input: n = 6, arr = [15, 13, 12, 14, 16, 20]

Output: [1, 1, 1, 3, 5, 6]

Explanation:

Traversing the given input span:

15 is greater than or equal to 15 and there are no more elements behind it, so the span is 1.

13 is smaller than 15, so the span is 1.

12 is smaller than 13, so the span is 1.

14 is greater than or equal to 12 and 13, but smaller than 15, so the span is 3 (days with values 12, 13, and 14).

16 is greater than or equal to 14, 12, 13, and 15, so the span is 5.

20 is greater than or equal to all previous elements, so the span is 6.

Hence the output will be 1 1 1 3 5 6.

Input: n = 8, arr = [30, 20, 25, 28, 27, 29, 35, 40]

Output:
[1, 1, 2, 3, 3, 6, 7, 8]
[1, 1, 2, 3, 3, 5, 7, 8]
[1, 1, 3, 3, 3, 5, 7, 8]
[1, 1, 2, 3, 1, 5, 7, 8]

Submit
Constraints:
1 ≤ n ≤ 105
1 ≤ arr[i] ≤ 109

#Brute
Intuition:
The brute force to solve the problem is to start counting the days (for each day) where the stock prices were less than or equal to the price of stocks on current day.

Approach:
Initialise an array to store the answer. Start traversing on the given array.
For every element, traverse back till the stock prices are less than or equal to the stock prices on current day.
Store the stock span for each day. Once done, return the answer.

class Solution:
    # Function to find the span of stock 
    # prices for each day
    def stockSpan(self, arr, n):
        
        # To store the answer
        ans = [0] * n
        
        # Traverse on the array
        for i in range(n):
            
            # To store the current span of stocks
            currSpan = 0
            
            # Traversing backwards to find stock span
            for j in range(i, -1, -1):
            
                # Update stock span
                if arr[j] <= arr[i]:
                    currSpan += 1
                
                # Else break out from loop
                else:
                    break
            
            # Store the current span
            ans[i] = currSpan
        
        # Return the result
        return ans

# Main code
if __name__ == "__main__":
    n = 7
    arr = [120, 100, 60, 80, 90, 110, 115]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to find the span 
    # of stock prices for each day
    ans = sol.stockSpan(arr, n)
    
    print("The span of stock prices is:", end=" ")
    for span in ans:
        print(span, end=" ")

Complexity Analysis:
Time Complexity: O(N2) (where N is the length of given array)
Using two nested loops.

Space Complexity: O(1)
Using only a couple of variables.

#Optimal
Intuition:
As stated in the problem, the stock span is the number of consecutive days for which the stock price was less than or equal to the price on current day. Hence, to get the stock span for current day, the aim is to find the position of its previous greater element. This will significantly improve the solution by eliminating multiple backwards traversals on the given array.

Understanding:
Finding the previous greater element is similar to finding the next greater element, the only difference is that the direction of traversal will be reversed while maintaining the decreasing order of elements in the stack (monotonic stack).
Approach:
Determine the indices of previous greater elements using monotonic stack (maintaining elements in decreasing order in a stack)
Once the indices are known, the stock span for each day will be difference between the current index and the index of its previous greater element.
Traverse the array, updating the stock span for each day.
After the traversal is over, return the result.

class Solution:
    # Function to find the indices of previous 
    # greater element for each element in the array
    def findPGE(self, arr):
        
        n = len(arr) # size of array
        
        # To store the previous greater elements
        ans = [0] * n
        
        # Stack to get elements in LIFO fashion
        st = []
        
        # Start traversing from the front
        for i in range(n):
            
            # Get the current element
            currEle = arr[i]
            
            # Pop the elements in the stack until 
            # the stack is not empty and the top 
            # element is not the greater element
            while st and arr[st[-1]] <= currEle:
                st.pop()
            
            # If the greater element is not 
            # found, stack will be empty
            if not st:
                ans[i] = -1
                
            # Else store the answer
            else:
                ans[i] = st[-1]
            
            # Push the current index in the stack 
            st.append(i)
        
        # Return the result
        return ans
    
    # Function to find the span of stock prices for each day
    def stockSpan(self, arr, n):
        
        # Get the indices of previous greater elements
        PGE = self.findPGE(arr)
        
        # To store the answer
        ans = [0] * n
        
        # Compute the result
        for i in range(n):
            ans[i] = i - PGE[i]
        
        # Return the result
        return ans

# Main code
if __name__ == "__main__":
    n = 7
    arr = [120, 100, 60, 80, 90, 110, 115]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to find the span of stock prices for each day
    ans = sol.stockSpan(arr, n)
    
    print("The span of stock prices is:", end=" ")
    for span in ans:
        print(span, end=" ")

Complexity Analysis:
Time Complexity: O(N)
Finding the indices of previous greater elements takes O(N) time.
Traversing the array once to find the stock span taking O(N) time.
Space Complexity: O(N)
The stack space used to find the previous greater elements can go up to O(N) in the worst case.

'''
class Solution:
    
    def findPGE(self, arr):
      
      n = len(arr) # size of array
      
      # To store the previous greater elements
      ans = [0] * n
      
      # Stack to get elements in LIFO fashion
      st = []
      
      # Start traversing from the front
      for i in range(n):
          
          # Get the current element
          currEle = arr[i]
          
          # Pop the elements in the stack until 
          # the stack is not empty and the top 
          # element is not the greater element
          while st and arr[st[-1]] <= currEle:
              st.pop()
          
          # If the greater element is not 
          # found, stack will be empty
          if not st:
              ans[i] = -1
              
          # Else store the answer
          else:
              ans[i] = st[-1]
          
          # Push the current index in the stack 
          st.append(i)
      
      # Return the result
      return ans
  
    # Function to find the span of stock prices for each day
    def stockSpan(self, arr, n):
        
        # Get the indices of previous greater elements
        PGE = self.findPGE(arr)
        
        # To store the answer
        ans = [0] * n
        
        # Compute the result
        for i in range(n):
            ans[i] = i - PGE[i]
        
        # Return the result
        return ans