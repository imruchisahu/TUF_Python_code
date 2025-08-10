'''Given an array of integers nums and an integer k, return the total number of subarrays whose XOR equals to k.


Examples:
Input : nums = [4, 2, 2, 6, 4], k = 6



Output : 4



Explanation : The subarrays having XOR of their elements as 6 are [4, 2],  [4, 2, 2, 6, 4], [2, 2, 6], and [6]

Input :nums = [5, 6, 7, 8, 9], k = 5



Output : 2



Explanation : The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]

Input : nums = [5, 2, 9], k = 7

Output:
1
Constraints:
  1 <= nums.length <= 105
  1 <= nums[i] <= 109
  1 <= k <= 109
Intuition
We will check the XOR of every possible subarray and count how many of them are equal to k. To do this, use three nested loops. The first two loops (let's call them i and j) will iterate over every possible starting and ending index of a subarray. In each iteration, the subarray range will be from index i to index j. Using another loop, calculate the XOR of the elements in the subarray [i...j]. Count the number of subarrays where the XOR is equal to k.

Note: Select every possible subarray using two nested loops, and for each subarray, calculate the XOR of all its elements using another loop.

Approach
First, run a loop (let's call it i) that selects every possible starting index of the subarray. The starting indices can range from index 0 to n−1 (where n is the size of the array). Inside this loop, run another loop (let's call it j) that signifies the ending index of the subarray. For each subarray starting from index i, the ending index can range from i to n−1.
For each subarray from index i to j (i.e., arr[i...j]), run another loop to calculate the XOR of all the elements in that subarray.
If the XOR equals k, increase the count by 1.


#Brute Force
class Solution:
    # Function to count the number of subarrays with XOR k
    def subarraysWithXorK(self, nums, k):
        n = len(nums)
        cnt = 0

        # Step 1: Generate subarrays
        for i in range(n):
            for j in range(i, n):
                xorr = 0
                # Step 2: Calculate XOR of all elements in the subarray
                for K in range(i, j + 1):
                    xorr ^= nums[K]
                # Step 3: Check XOR and count
                if xorr == k:
                    cnt += 1
        return cnt

if __name__ == "__main__":
    a = [4, 2, 2, 6, 4]
    k = 6

    # Create an instance of the Solution class
    solution = Solution()

    # Function call to get the result
    ans = solution.subarraysWithXorK(a, k)
 
    print("The number of subarrays with XOR k is:", ans)
Complexity Analysis 
Time Complexity: O(N3), where N is the size of the array. This is because we are using three nested loops, each running approximately N times.

Space Complexity: O(1) since we are not using any additional space.

#Better

class Solution:
    # Function to count the number of subarrays with XOR k
    def subarraysWithXorK(self, nums, k):
        n = len(nums)
        cnt = 0

        # Step 1: Generate subarrays
        for i in range(n):
            xorr = 0
            for j in range(i, n):
                # Step 2: Calculate XOR of all elements in the subarray
                xorr ^= nums[j]

                # Step 3: Check XOR and count
                if xorr == k:
                    cnt += 1
        return cnt

if __name__ == "__main__":
    a = [4, 2, 2, 6, 4]
    k = 6

    # Create an instance of the Solution class
    solution = Solution()

    # Function call to get the result
    ans = solution.subarraysWithXorK(a, k)
    
    print("The number of subarrays with XOR k is:", ans)

    Complexity Analysis  
Time Complexity: O(N2), where N is the size of the array. Since we are using two nested loops, each running for N times, the time complexity will be approximately O(N2).

Space Complexity: O(1) as we are not using any additional space.




'''

class Solution:
    def subarraysWithXorK(self, nums, k):
        n = len(nums)
        xr = 0
        mpp = {}
        # setting the value of 0.
        mpp[xr] = mpp.get(xr, 0) + 1
        cnt = 0

        for i in range(n):
            # prefix XOR till index i:
            xr = xr ^ nums[i]

            # By formula: x = xr ^ k:
            x = xr ^ k

            # add the occurrence of xr ^ k to the count:
            cnt += mpp.get(x, 0)

            # Insert the prefix xor till index i into the map:
            mpp[xr] = mpp.get(xr, 0) + 1

        return cnt

if __name__ == "__main__":
    a = [4, 2, 2, 6, 4]
    k = 6

    # Create an instance of the Solution class
    solution = Solution()

    # Function call to get the result
    ans = solution.subarraysWithXorK(a, k)

    print("The number of subarrays with XOR k is:", ans)
    
'''Complexity Analysis 
Time Complexity: O(N) or O(NxlogN), where N is the size of the array. If we use an unordered_map in C++, the time complexity is O(N). However, with a map data structure, the time complexity is O(NxlogN). In the worst case for an unordered_map, the searching time can increase to O(N), making the overall time complexity O(N2).

Space Complexity: O(N), as we are using a map data structure.'''