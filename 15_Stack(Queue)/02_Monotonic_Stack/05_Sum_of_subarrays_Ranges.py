'''
Given an integer array nums, determine the range of a subarray, defined as the difference between the largest and smallest elements within the subarray. Calculate and return the sum of all subarray ranges of nums.



A subarray is defined as a contiguous, non-empty sequence of elements within the array.


Examples:
Input: nums = [1, 2, 3]

Output: 4

Explanation: The 6 subarrays of nums are the following:

[1], range = largest - smallest = 1 - 1 = 0 

[2], range = 2 - 2 = 0

[3], range = 3 - 3 = 0

[1,2], range = 2 - 1 = 1

[2,3], range = 3 - 2 = 1

[1,2,3], range = 3 - 1 = 2

So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

Input: nums = [1, 3, 3]

Output: 4

Explanation: The 6 subarrays of nums are the following:

[1], range = largest - smallest = 1 - 1 = 0

[3], range = 3 - 3 = 0

[3], range = 3 - 3 = 0

[1,3], range = 3 - 1 = 2

[3,3], range = 3 - 3 = 0

[1,3,3], range = 3 - 1 = 2

So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.

Input: nums = [4, -2, -3, 4, 1]

Output:
59
Constraints:
·  1 <= nums.length <= 1000

·  -109 <= nums[i] <= 109


#Brute
#Intuition:
The brute force way to solve this problem is by generating all the subarrays and finding the minimum and maximum values in all of them. The range of a subarray can be found as the difference between the maximum and minimum value which can be summed up for all the subarrays to get the result.

Approach:
Initialize a variable to store the required sum with 0 initially.
Traverse on the array. Initialize two variables to store the minimum and maximum elements in the subarray.
Use a nested loop to traverse all the subarrays and find the minimum and maximum of each subarray. Update the sum for each subarray by finding the range of subarray (maximum-minimum).
Once all the subarrays are taken into consideration, the result will be stored in the sum variable.

class Solution:
    # Function to find the sum of 
    # subarray ranges in each subarray
    def subArrayRanges(self, arr):
        
        # Size of array
        n = len(arr)
        
        # To store the sum
        total_sum = 0
        
        # Traverse on the array
        for i in range(n):
            
            # To store the smallest value of subarray
            smallest = arr[i]
            
            # To store the largest value of subarray
            largest = arr[i]
            
            # Nested loop to get all 
            # subarrays starting from index i
            for j in range(i, n):
                
                # Update the smallest value
                smallest = min(smallest, arr[j])
                
                # Update the largest value
                largest = max(largest, arr[j])
                
                # Update the sum
                total_sum += (largest - smallest)
        
        # Return the computed sum
        return total_sum

# Main function to test the solution
if __name__ == "__main__":
    arr = [1, 2, 3]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to find the sum of 
    # subarray ranges in each subarray
    ans = sol.subArrayRanges(arr)
    
    print("The sum of subarray ranges is:", ans)

Complexity Analysis:
Time Complexity: O(N2) (where N is the size of the array)
Using two nested loops.

Space Complexity: O(1)
Using only a couple of variables.


#Optimal
Intuition:
Consider the following example:  Hence, instead of summing up the ranges for each subarray, the sum of largest elements in each subarray and sum of smallest elements in each subarray can be added to get the required sum of subarray ranges.

To optimally find the sum of largest and the smallest elements in the array, the concept of Next/Previous Smaller/Greater Elements come into picture as discussed in the Sum of Subarray minimums (Optimal Solution).

Approach:
Four helper functions are used to find specific indices:
Next Smaller Elements (NSE): For each element, find the index of the next smaller element to its right.
Next Greater Elements (NGE): For each element, find the index of the next greater element to its right.
Previous Smaller or Equal Elements (PSEE): For each element, find the index of the previous smaller or equal element to its left.
Previous Greater or Equal Elements (PGEE): For each element, find the index of the previous greater or equal element to its left.
Utilize the NSE and PSEE indices to calculate the sum of the minimum values in all subarrays. Utilize the NGE and PGEE indices to calculate the sum of the maximum values in all subarrays.
The final result is obtained by subtracting the sum of subarray minimums from the sum of subarray maximums. This gives the sum of ranges of all subarrays.

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
            while st and arr[st[-1]] >= currEle:
                st.pop()
            
            # Update the answer
            ans[i] = st[-1] if st else n
            
            # Push the index of current element in the stack
            st.append(i)
        
        # Return the answer
        return ans
    
    # Function to find the indices of 
    # next greater elements
    def findNGE(self, arr):
        
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
            # element is not the greater element
            while st and arr[st[-1]] <= currEle:
                st.pop()
            
            # Update the answer
            ans[i] = st[-1] if st else n
            
            # Push the index of current element in the stack
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
            while st and arr[st[-1]] > currEle:
                st.pop()
            
            # Update the answer
            ans[i] = st[-1] if st else -1
            
            # Push the index of current element in the stack
            st.append(i)
        
        # Return the answer
        return ans
    
    # Function to find the indices of 
    # previous greater or equal elements
    def findPGEE(self, arr):
        
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
            # elements are smaller than the current element
            while st and arr[st[-1]] < currEle:
                st.pop()
            
            # Update the answer
            ans[i] = st[-1] if st else -1
            
            # Push the index of current element in the stack
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
            val = (freq * arr[i] * 1)
            
            # Updating the sum
            total_sum += val
        
        # Return the computed sum
        return total_sum
    
    # Function to find the sum of the 
    # maximum value in each subarray
    def sumSubarrayMaxs(self, arr):
        
        nge = self.findNGE(arr)
        
        pgee = self.findPGEE(arr)
        
        # Size of array
        n = len(arr)
        
        # To store the sum
        total_sum = 0
        
        # Traverse on the array
        for i in range(n):
            
            # Count of first type of subarrays
            left = i - pgee[i]
            
            # Count of second type of subarrays
            right = nge[i] - i
            
            # Count of subarrays where 
            # current element is maximum
            freq = left * right * 1
            
            # Contribution due to current element 
            val = (freq * arr[i] * 1)
            
            # Updating the sum
            total_sum += val
        
        # Return the computed sum
        return total_sum
    
    # Function to find the sum of 
    # subarray ranges in each subarray
    def subArrayRanges(self, arr):
        
        # Return the result
        return (self.sumSubarrayMaxs(arr) - 
                self.sumSubarrayMins(arr))

# Main function to test the solution
if __name__ == "__main__":
    arr = [1, 2, 3]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to find the sum of 
    # subarray ranges in each subarray
    ans = sol.subArrayRanges(arr)
    
    print("The sum of subarray ranges is:", ans)

Complexity Analysis:
Time Complexity: O(N) (where N is the size of given array)
Calculating the sum of subarray maximums takes O(N) time.
Calculating the sum of subarray minimums takes O(N) time.
Space Complexity: O(N)

Calculating the sum of subarray maximums requires O(N) space.
Calculating the sum of subarray minimums requires O(N) space.



'''