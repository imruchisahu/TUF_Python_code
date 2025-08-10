'''Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.


Examples:
Input: nums = [10, 5, 2, 7, 1, 9],  k=15

Output: 4

Explanation:

The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.

Input: nums = [-3, 2, 1], k=6

Output: 0

Explanation:

There is no sub-array in the array that sums to 6. Therefore, the output is 0.

Input: nums = [-1, 1, 1], k=1

Output:
3
Constraints:
 1<=n<=105
 -105<=nums[i]<=105
 -109<= k<=109

Intuition
To find the longest subarray with a sum of 𝑘, we'll check the sum of every possible subarray. We use two loops to pick all possible starting and ending indices, and another loop to calculate the sum of each subarray. If a subarray's sum is 𝑘, we compare its length to the longest one we've found so far. This way, we make sure to find the longest subarray with the sum of 𝑘.

Approach
First, we run a loop i to select every possible starting index of the subarray. These starting indices range from index 0 to n-1 (where n is the size of the array).
Inside this loop, we run another loop j to select the ending index of the subarray. For every subarray starting at index i, the ending index j can range from i to n-1.
Next, for each subarray starting from index i and ending at index j (i.e., arr[i...j]), we run an additional loop to calculate the sum of all the elements in that subarray.
If the sum equals k, we consider its length, which is (j-i+1). Among all such subarrays, we keep track of the maximum length by comparing all the lengths.
Dry Run: Please refer to the video for the dry-run.


Complexity Analysis 
Time Complexity: O(N3), where N is the size of the array. Since we are using three nested loops, each running approximately N times.

Space Complexity: O(1), as we are not using any extra space.

#Brute Force solution

class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums) 
        maxLength = 0

        # starting index
        for startIndex in range(n):
            # ending index
            for endIndex in range(startIndex, n):
                # add all the elements of 
                # subarray = nums[startIndex...endIndex]
                currentSum = 0
                for i in range(startIndex, endIndex + 1):
                    currentSum += nums[i]

                if currentSum == k:
                    maxLength = max(maxLength, endIndex - startIndex + 1)

        return maxLength

if __name__ == "__main__":
    nums = [-1, 1, 1]
    k = 1

    # Create an instance of the Solution class
    solution = Solution()
    # Function call to get the result
    length = solution.longestSubarray(nums, k)
    
    print("The length of the longest subarray is:", length)

'''

class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums)  

        preSumMap = {}
        sum = 0
        maxLen = 0
        for i in range(n):
            # calculate the prefix sum till index i
            sum += nums[i]

            # if the sum equals k, update maxLen
            if sum == k:
                maxLen = max(maxLen, i + 1)

            # calculate the sum of remaining part i.e., sum - k
            rem = sum - k

            # calculate the length and update maxLen
            if rem in preSumMap:
                length = i - preSumMap[rem]
                maxLen = max(maxLen, length)

            # update the map if sum is not already present
            if sum not in preSumMap:
                preSumMap[sum] = i

        return maxLen

if __name__ == "__main__":
    nums = [-1, 1, 1]
    k = 1

    # Create an instance of the Solution class
    solution = Solution()
    # Function call to get the result
    length = solution.longestSubarray(nums, k)
    
    print("The length of the longest subarray is:", length)
