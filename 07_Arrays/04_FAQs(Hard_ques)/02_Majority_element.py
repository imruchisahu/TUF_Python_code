'''Given an integer array nums of size n, return the majority element of the array.



The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.


Examples:
Input: nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]

Output: 7

Explanation: The number 7 appears 5 times in the 9 sized array

Input: nums = [1, 1, 1, 2, 1, 2]

Output: 1

Explanation: The number 1 appears 4 times in the 6 sized array

Input: nums = [-1, -1, -1, -1]

Output:
-1
Constraints:
n == nums.length.
1 <= n <= 105
-104 <= nums[i] <= 104
One value appears more than n/2 times.

Similar Problems

Hint 1

Hint 2
Intuition 
Naive way is to count the occurrences of each element. The element which will have count greater than half the array size will be the majority element.

Approach 
Iterate in the array to select the elements of the array one by one. Now, for each element, run another loop and count its occurrence in the given array.
If any element occurs more than the floor of (N/2), simply return it.


Complexity Analysis 
Time Complexity: O(N2), for nested for loops used, where N is the size of the array

Space Complexity: O(1) as no extra space is used.

from typing import List

class Solution:
    # Function to find the majority element in an array
    def majorityElement(self, nums: List[int]) -> int:
        
        # Size of the given array
        n = len(nums)
        
        # Iterate through each element of the array
        for i in range(n):
            
            # Counter to count occurrences of nums[i]
            cnt = 0 
            
            # Count the frequency of nums[i] in the array
            for j in range(n):
                if nums[j] == nums[i]:
                    cnt += 1
            
            # Check if frequency of nums[i] is greater than n/2
            if cnt > (n // 2):
                # Return the majority element
                return nums[i]
        
        # Return -1 if no majority element is found
        return -1

if __name__ == "__main__":
    arr = [2, 2, 1, 1, 1, 2, 2]
    
    # Create an instance of Solution class
    sol = Solution()
 
    ans = sol.majorityElement(arr)
    
    # Print the majority element found
    print("The majority element is:", ans)

'''
class Solution:
    def majorityElement(self, nums):
        n=len(nums)
        for i in range(n):
            count=0
            for j in range(n):
                if nums[j]==nums[i]:
                    count += 1
            if count > (n//2):
                return nums[i]
        return -1
        