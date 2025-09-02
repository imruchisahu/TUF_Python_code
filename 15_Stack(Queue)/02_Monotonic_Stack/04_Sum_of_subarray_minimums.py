'''
Given an array of integers arr of size n, calculate the sum of the minimum value in each (contiguous) subarray of arr. Since the result may be large, return the answer modulo 109 +7.


Examples:
Input: arr = [3, 1, 2, 5]

Output: 18

Explanation: The minimum of subarrays: [3], [1], [2], [5], [3, 1], [1, 2], [2, 5], [3, 1, 2], [1, 2, 5], [3, 1, 2, 5] are 3, 1, 2, 5, 1, 1, 2, 1, 1, 1 respectively and their sum is 18.

Input: arr = [2, 3, 1]

Output: 10

Explanation: The minimum of subarrays: [2], [3], [1], [2,3], [3,1], [2,3,1] are 2, 3, 1, 2, 1, 1 respectively and their sum is 10.

Input: arr = [11, 81, 94, 43, 3]

Output:
444
Constraints:
  1 <= arr.length <= 105
  1 <= arr[i] <= 106

#Brute
Intuition:
The brute force way to solve this problem is by generating all the subarrays and finding the minimum in all of them. All the minimums can be summed up while taking modulus with 109 + 7 to return the result.

Approach:
Initialize a variable to store the required sum with 0 initially.
Traverse on the array. Initialize a variable to store the minimum element in the subarray.
Use a nested loop to traverse for all the subarrays and find the minimum of each subarray. Update the sum for each subarray.
Once all the subarrays are taken into consideration, the result will be stored in the sum variable.

class Solution:
   def sumSubarrayMins(self, arr):
       
       # Size of array
       n = len(arr)
       
       mod = int(1e9 + 7)  # Mod value
       
       # To store the sum
       total_sum = 0
       
       # Traverse on the array
       for i in range(n):
           
           # To store the minimum of subarray
           mini = arr[i]
           
           # Nested loop to get all 
           # subarrays starting from index i
           for j in range(i, n):
               
               # Update the minimum value
               mini = min(mini, arr[j])
               
               # Update the sum
               total_sum = (total_sum + mini) % mod
       
       # Return the computed sum
       return total_sum

# Main function to test the solution
if __name__ == "__main__":
   arr = [3, 1, 2, 5]
   
   # Creating an instance of Solution class
   sol = Solution()
   
   # Function call to find the sum of the 
   # minimum value in each subarray
   ans = sol.sumSubarrayMins(arr)
   
   print("The sum of minimum value in each subarray is:", ans)

Complexity Analysis:
Time Complexity: O(N2)
Using two nested loops.

Space Complexity: O(1)
Using only a couple of variables.


#Optimal
Intuition:
Consider the following example: 
Hence it is clear that instead of generating all the subarrays and finding the minimum in each subarray to find the sum, we can get the required sum by finding the number of times(frequency) an element in the array will be considered in sum.

Considering the above dry run, we can see that:

Element 3 is contributing for a total of 1 time.
Element 1 is contributing for a total of 6 times.
Element 2 is contributing for a total of 2 times.
Element 5 is contributing for a total of 1 time..
How to find the frequency of an element in the required sum?
To find the frequency, the number of subarrays where the current element will be minimum must be known.
Understanding:
Consider the following example: 
It can be seen that the current element will be considered in all those subarrays that:
Do not start with the previous smaller element (if it exists), which includes the current element.
Do not end with the next smaller element (if it exists), which includes the current element.
Finding count of required subarrays:
The count of subarrays that contain the current element as the minimum element is the subarrays whose:
Starting index lies in the range (psee[ind], ind] (excluding psee(ind) and including ind).
Count of such subarrays is: ind - (psee[ind] + 1) + 1, i.e.,
Count of such subarrays is: ind - psee[ind]. and,
Ending index lies in the range [ind, nse[ind]) (including ind and excluding nse[ind]).
Count of such subarrays is: (nse[ind] - 1) - ind + 1, i.e.,
Count of such subarrays is: nse[ind] - ind.
(where pse[ind] and nse[ind] refer to the indices of previous smallest element and the next smaller element for the element at index ind.)

Hence, the count of subarrays having the current element (having index ind) as the minimum element is:
(ind - psee[ind]) * (nse[ind] - ind).
Edge Cases:
Edge Cases:
Case 1: Empty array
If the input array is empty, there are no subarrays, and hence, the sum of subarray minimums should be 0. The function should handle this case appropriately.

vector arr = {};
int result = sol.sumSubarrayMins(arr);  // Output: 0
Case 2: Array with all elements being the same
When all elements of the array are the same, each element is the minimum in every subarray it appears in. This case can lead to a large sum because each element is counted multiple times.

vector arr = {2, 2, 2, 2};
int result = sol.sumSubarrayMins(arr);  // Output: 16
Case 3: Array with a single element
If the array contains just one element, then that element will be the minimum for the single subarray (which is the entire array itself).

vector arr = {5};
int result = sol.sumSubarrayMins(arr);  // Output: 5
Case 4: Array with strictly increasing or decreasing elements
If the array elements are strictly increasing or strictly decreasing, the next smaller element (NSE) and the previous smaller or equal element (PSEE) indices will be easy to compute, and the function should handle these cases efficiently.

vector arr = {1, 2, 3, 4};
int result = sol.sumSubarrayMins(arr);  // Output: 20
Case 5: Large Input Array
The function should handle large input arrays efficiently, adhering to the O(N) time complexity. It's important to test the function’s performance with large arrays (up to the limit defined by the problem).

vector arr(1000000, 1);  // Large array with 1 million elements
int result = sol.sumSubarrayMins(arr);  // Check if it runs within time limits
Approach:
For each element in the array, find the index of the next smaller element(NSE) to the right. Use a stack to efficiently track these indices.
For each element in the array, find the index of the previous smaller or equal element(PSEE) to the left. Use a stack to efficiently track these indices.
For each element in the array, calculate its contribution to the sum of subarray minimums based on its frequency as the minimum in the subarrays. Use the indices from NSE and PSEE to determine the count of subarrays where the current element is the minimum.
Multiply the frequency obtained by the element's value to get its contribution and add this to the total sum. The result is computed modulo 109 + 7 to handle large numbers.

class Solution:
    # Function to find the indices 
    # of next smaller elements
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
    # previous smaller or equal elements
    def findPSEE(self, arr):
        
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
            # elements are greater than the current element
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            
            # Update the answer
            ans[i] = st[-1] if st else -1
            
            # Push the index of current 
            # element in the stack
            st.append(i)
        
        # Return the answer
        return ans

    # Function to find the sum of the 
    # minimum value in each subarray
    def sumSubarrayMins(self, arr):
        
        nse = self.findNSE(arr)
        psee = self.findPSEE(arr)
        
        # Size of array
        n = len(arr)
        
        mod = int(1e9 + 7)  # Mod value
        
        # To store the sum
        total_sum = 0
        
        # Traverse on the array
        for i in range(n):
            
            # Count of first type of subarrays
            left = i - psee[i]
            
            # Count of second type of subarrays
            right = nse[i] - i
            
            # Count of subarrays where 
            # current element is minimum
            freq = left * right * 1
            
            # Contribution due to current element 
            val = (freq * arr[i]) % mod
            
            # Updating the sum
            total_sum = (total_sum + val) % mod
        
        # Return the computed sum
        return total_sum

# Main function to test the solution
if __name__ == "__main__":
    arr = [3, 1, 2, 5]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to find the sum of the 
    # minimum value in each subarray
    ans = sol.sumSubarrayMins(arr)
    
    print("The sum of minimum value in each subarray is:", ans)

Complexity Analysis:
Time Complexity: O(N) (where N is the size of given array)

Finding the indices of next smaller elements and previous smaller elements take O(2*N) time each.
Calculating the sum of subarrays minimum takes O(N) time.
Space Complexity: O(N)

Finding the indices of the next smaller elements and previous smaller elements takes O(N) space each due to stack space.
Storing the indices of the next smaller elements and previous smaller elements takes O(N) space each.




  '''