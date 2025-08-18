'''Given an array of integers nums of unique elements. Return all possible subsets (power set) of the array.



Do not include the duplicates in the answer.


Examples:
Input : nums = [1, 2, 3]

Output : [ [ ] , [1] , [2] , [1, 2] , [3] , [1, 3] , [2, 3] , [1, 2 ,3] ]

Input : nums = [1, 2]

Output : [ [ ] , [1] , [2] , [1, 2] ]

Input : nums = [0]

Output:
[ [], [0]]
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10

Intuition:
The power set of a given array is the set of all possible subsets of the array, including the empty set and the set itself. Each element can either be included in a subset or not, resulting in 2n (where n is the number of elements) possible subsets.

Approach:
Each subset can be represented by a binary number of length n (where n is the size of the array). If the binary number is 101, it means the subset includes the elements at positions 1 and 3 of the array.
Store the size of array, the count of subarrays in variables. Declare a list of lists to return the required answer.
Loop through all possible values from 0 to count-1. Initialize an empty list for the current subset.
For each value, use its binary representation to decide which elements are included in the current subset. Loop through each bit of the current value. If the bit is set, add the corresponding element from the array in the subset.
Add all the subsets generated to the list of list which can be returned as our answer.

class Solution:
    # Function call to get the
    # Power set of given array
    def powerSet(self, nums):
        
        # Variable to store size of array
        n = len(nums)
        
        # To store the answer
        ans = []
        
        # Variable to store the 
        # count of total susbsets
        count = (1 << n)
        
        # Traverse for every value
        for val in range(count):
            
            # To store the current subset
            subset = []
            
            # Traverse on n bits
            for i in range(n):
                if val & (1 << i):
                    subset.append(nums[i])
            
            # Add the current subset 
            # to final answer 
            ans.append(subset)
        
        # Return stored answer
        return ans

# Creating an instance of Solution class
sol = Solution()

# Function call to get the Power set of given array
nums = [1, 2, 3]
ans = sol.powerSet(nums)

ans.sort(key=lambda x: len(x))

# Output
print("The power set for the given array is: ")
for subset in ans:
    print(" ".join(map(str, subset)))

Complexity Analysis:
Time Complexity: O(2N*N) (where N is the size of the array) –
The outer loop runs for count numbers of times, and count is 2N resulting in O(2N) TC.
The inner for loop runs to check N bits, resulting in O(N) TC.
Space Complexity: O(2N*N) – Space required to store the power set (approximately).

'''
class Solution:
    def powerSet(self, nums):
        n = len(nums)
        ans = []
        count = (1 << n)
        for val in range(count):
            subset = []
            for i in range(n):
                if val & (1 << i):
                    subset.append(nums[i]) 
            ans.append(subset)
        return ans
