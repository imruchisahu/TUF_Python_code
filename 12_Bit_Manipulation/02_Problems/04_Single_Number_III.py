'''
Given an array nums of length n, every integer in the array appears twice except for two integers. Identify and return the two integers that appear only once in the array. Return the two numbers in ascending order.



For example, if nums = [1, 2, 1, 3, 5, 2], the correct answer is [3, 5], not [5, 3].


Examples:
Input : nums = [1, 2, 1, 3, 5, 2]

Output : [3, 5]

Explanation : The integers 3 and 5 have appeared only once.

Input : nums = [-1, 0]

Output : [-1, 0]

Explanation : The integers -1 and 0 have appeared only once.

Input : nums = [1, 9, 1, 2, 8, 2]

Output:
[8, 9]
Constraints:
2 <= nums.length <= 105
-3*105 <= nums[i] <= 3*105
Every integer in nums appears twice except two integers.

#Brute
Intuition:
The brute force way to solve this will be to utilize a frequency counting approach. By keeping track of the frequency of each element in the array, the element that appears only once can be easily identified.

Approach:
Use a hash map to store the frequency of each element in the array. The keys of the map are the elements of the array, and the values are their corresponding frequencies.
Traverse the entire array once, and for each element, update its frequency count in the map.
After populating the map with frequency counts, iterate over the map to find the elements with a frequency of 1. Add these elements in the result array.
Return the resulting array after sorting it.

class Solution:
    # Function to get the single 
    # number in the given array 
    def singleNumber(self, nums):
        
        # Array to store the answer
        ans = []
        
        # Map to store the elements 
        # and their frequencies
        mpp = {}
        
        # Iterate on the array
        for num in nums:
            mpp[num] = mpp.get(num, 0) + 1 # Update the map
        
        # Iterate on the map
        for key, value in mpp.items():
            # If frequency is 1
            if value == 1:
                # Add the element to
                # the result array 
                ans.append(key)
        
        # Return the result after sorting
        ans.sort()
        return ans

# Creating an instance of Solution class
sol = Solution()

# Function call to get the single number in the given array
nums = [1, 2, 1, 3, 5, 2]
ans = sol.singleNumber(nums)

print("The single numbers in given array are:", ans[0], "and", ans[1])


Complexity Analysis:
Time Complexity: O(N) (where N is the size of the array)
Traversing the array to update the Hash Map - O(N).
Traversing on the map - O(N) (in worst case).
Sorting the answer array - O(2*log(2)) ~ O(1).
Hence, O(N) + O(N) + O(1) ~ O(N).
Space Complexity: O(N), Using a hashmap data structure and in the worst-case (when all elements in the array are unique), 
it will store N key-value pairs.

#Optimal
Intuition:
An optimal approach to solve this problem will be possible if we can divide the elements in array into two groups such that each group only contains one unique element. This way, the problem boils down to Single Number-I and both the unique elements can be identified with ease.

Now, to divide the numbers into two groups(buckets), the rightmost set bit in the overall XOR of all elements can be used. The overall XOR of all elements is equivalent to the XOR of the two unique numbers.

Why Divide using the Rightmost Set Bit?

This is because of the following reasons:
The two unique numbers needs to be separated into two different groups, and the rightmost set bit in the overall XOR will indicate the bit position where the the two unique numbers differ.
Using this bit, all the elements in the array can be divided into two groups (buckets):
One group where this bit is set.
Another group where this bit is not set.
Approach:
Traverse the entire array, performing an XOR operation on all numbers. This will effectively cancel out all the numbers that appear twice, leaving us with the XOR of the two unique numbers.
Determine the rightmost set bit (bit that is 1) in the result from the first step. This set bit can be used to differentiate the two unique numbers since they must differ at this bit position.
Traverse the array again, but this time divide the numbers into two groups:
One group where the numbers have the rightmost set bit.
Another group where the numbers do not have this bit set.
Perform XOR operations while adding numbers in each group. This will cancel out the duplicate numbers, leaving only the unique numbers in each group.
Sort the two unique numbers in ascending order and return them.

class Solution:
    # Function to get the single 
    # numbers in the given array 
    def singleNumber(self, nums):
        # Variable to store size of array
        n = len(nums)
        
        # Variable to store XOR of all elements
        XOR = 0
        
        # Traverse the array
        for i in range(n):
            # Update the XOR
            XOR = XOR ^ nums[i]
        
        # Variable to get the rightmost 
        # set bit in overall XOR 
        rightmost = (XOR & (XOR - 1)) ^ XOR
        
        # Variables to stores XOR of
        # elements in bucket 1 and 2
        XOR1, XOR2 = 0, 0
        
        # Traverse the array
        for i in range(n):
            # Divide the numbers among bucket 1
            # and 2 based on rightmost set bit 
            if nums[i] & rightmost:
                XOR1 = XOR1 ^ nums[i]
            else:
                XOR2 = XOR2 ^ nums[i]
        
        # Return the result in sorted order
        return [XOR1, XOR2] if XOR1 < XOR2 else [XOR2, XOR1]

# Example usage
nums = [1, 2, 1, 3, 5, 2]

# Creating an instance of Solution class
sol = Solution()

# Function call to get the single numbers in the given array
ans = sol.singleNumber(nums)

print("The single numbers in given array are:", ans[0], "and", ans[1])

Complexity Analysis:
Time Complexity: O(N), Traversing the array twice results in O(2*N) TC.

Space Complexity: O(1), Using a couple of variables i.e., constant space.

'''
class Solution:   
    def singleNumber(self, nums):
        ans = []
        mpp = {}
        for num in nums:
            mpp[num] = mpp.get(num, 0) + 1 
        for key, value in mpp.items():
            if value == 1: 
                ans.append(key)
        ans.sort()
        return ans