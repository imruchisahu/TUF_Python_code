'''Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.


Examples:
Input: nums = [1, 1, 1], k = 2

Output: 2

Explanation: In the given array [1, 1, 1], there are two subarrays that sum up to 2: [1, 1] and [1, 1]. Hence, the output is 2.

Input: nums = [1, 2, 3], k = 3

Output: 2

Explanation: In the given array [1, 2, 3], there are two subarrays that sum up to 3: [1, 2] and [3]. Hence, the output is 2.

Input: nums = [3, 1, 2, 4], k = 6

Output:
2
Constraints:
   1 <= nums.length <= 105
   -1000 <= nums[i] <= 1000
   -107 <= k <= 107

Similar Problems
Intuition
To find the number of subarrays with a sum equal to k, use three nested loops. The first two loops (i and j) will iterate over every possible starting and ending index of a subarray, respectively. In each iteration, the subarray range will be from index i to index j. Using a third loop, calculate the sum of the elements in the subarray [i…j], then count only those subarrays where the calculated sum equals k.

Approach
First, use a loop (i) to select every possible starting index of the subarray. The starting indices can range from index 0 to index n-1 (where n is the size of the array).
Inside this loop, run another loop (j) to signify the ending index of the subarray. For each subarray starting from index i, the possible ending indices can vary from index i to n-1.
Next, for each subarray defined by the range i to j (i.e., arr[i…j]), use another loop to calculate the sum of all the elements in that subarray.
After calculating the sum, check if the sum is equal to the given k. If it is, increase the count.

Complexity Analysis 
Time Complexity: O(N3), where N is the size of the array. We are using three nested loops here. Though all loops are not running exactly N times, the time complexity will be approximately O(N3).

Space Complexity: O(1), as we are not using any extra space.

#Brute Froce
class Solution:
    def subarraySum(self, nums, k):
        n = len(nums)
        # Number of subarrays
        cnt = 0

        # starting index i
        for i in range(n):
            # ending index j
            for j in range(i, n):

                # calculate the sum of subarray [i...j]
                sum = 0
                for K in range(i, j + 1):
                    sum += nums[K]

                # Increase the count if sum == k:
                if sum == k:
                    cnt += 1
        return cnt

if __name__ == "__main__":
    solution = Solution()
    nums = [3, 1, 2, 4]
    k = 6
    # Function call to find the result
    cnt = solution.subarraySum(nums, k)
    print("The number of subarrays is:", cnt)


    #better Approach

class Solution:
    def subarraySum(self, nums, k):
        n = len(nums)
        # Number of subarrays
        count = 0

        # starting index
        for startIndex in range(n):
            currentSum = 0
            # ending index
            for endIndex in range(startIndex, n):
                # calculate the sum of subarray [startIndex...endIndex]
                # sum of [startIndex..endIndex-1] + nums[endIndex]
                currentSum += nums[endIndex]

                # Increase the count if currentSum == k:
                if currentSum == k:
                    count += 1
        return count

if __name__ == "__main__":
    solution = Solution()
    nums = [3, 1, 2, 4]
    k = 6
    # Function call to find the result
    count = solution.subarraySum(nums, k)
    print("The number of subarrays is:", count)

'''

class Solution:
    def subarraySum(self, nums, k):
        n = len(nums)
        prefix_sum_map = {0: 1}
        current_prefix_sum = 0
        subarray_count = 0

        for i in range(n):
            # Add current element to the prefix sum:
            current_prefix_sum += nums[i]

            """Calculate the value to remove
           (current_prefix_sum - k)"""
            sum_to_remove = current_prefix_sum - k

            """ Add the number of subarrays 
            with the sum to be removed"""
            subarray_count += prefix_sum_map.get(sum_to_remove, 0)

            """ Update the count of  current
            prefix sum in the map"""
            prefix_sum_map[current_prefix_sum] = prefix_sum_map.get(current_prefix_sum, 0) + 1

        return subarray_count

if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()
    nums = [3, 1, 2, 4]
    k = 6
    # Function call to get the result
    subarray_count = solution.subarraySum(nums, k)
    print("The number of subarrays is:", subarray_count)
