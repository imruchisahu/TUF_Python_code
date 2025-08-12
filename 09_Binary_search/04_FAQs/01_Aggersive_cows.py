'''Given an array nums of size n, which denotes the positions of stalls, and an integer k, which denotes the number of aggressive cows, assign stalls to k cows such that the minimum distance between any two cows is the maximum possible. Find the maximum possible minimum distance.


Examples:
Input: n = 6, k = 4, nums = [0, 3, 4, 7, 10, 9]

Output: 3

Explanation: The maximum possible minimum distance between any two cows will be 3 when 4 cows are placed at positions [0, 3, 7, 10]. Here the distances between cows are 3, 4, and 3 respectively. We cannot make the minimum distance greater than 3 in any ways.

Input : n = 5, k = 2, nums = [4, 2, 1, 3, 6]

Output: 5

Explanation: The maximum possible minimum distance between any two cows will be 5 when 2 cows are placed at positions [1, 6]. 

Input : n = 5, k = 3, nums = [10, 1, 2, 7, 5]

Output:
4
Constraints:
  2 <= n <= 105
  2 <= k <= n
  0 <= nums[i] <= 109
  

  #Linear Search

  Intuition: 
The extremely naive approach is to use linear search to check all possible distances from 1 to (max-min) where, max is the maximum element of the array and min is the minimum element of the array. The maximum distance for which the cows can be placed, will be our answer.

Approach: 
Working of aggresiveCows(nums, k):
First, sort the arrays and find out the range of the search space, the range will be from [1, (max-min)]. Where max is the maximum element of the array and min is the minimum element of the array. Every number in this range is a possible distance between the cows.
Traverse througth the search space and for each possible distance call the canWePlace() function, if the function returns false then, that means the maximum distance is the (current distance - 1) for which the cows can be placed.
If no such distance is found, then return the (max-min) as answer.

Working of canWePlace(nums, dist, cow):
Start by getting the size of the array and store it in 'n'. Initialize 'cntCows' to 1, indicating the number of cows already placed (starting with the first cow) also initialize 'last' to first element of array, which represents the position of the last placed cow.
Iterate through the array and check if the distance between the current position and the last placed cow is greater than or equal to dist. If true, it means you can place another cow at current position. Increment 'cntCows' to reflect placing another cow. Update 'last' to current element, marking current element as the position of the last placed cow.
If the loop completes without placing all cows (cntCows < cows), return false, indicating it's not possible to place all cows with at least dist distance apart.



class Solution:
    """Function to check if we can place 'cows' 
    cows with at least 'dist' distance apart"""
    def canWePlace(self, nums, dist, cows):
        # Size of array
        n = len(nums)
        
        # Number of cows placed
        cntCows = 1
        
        # Position of last placed cow
        last = nums[0]
        for i in range(1, n):
            if nums[i] - last >= dist:
                # Place next cow
                cntCows += 1
                
                # Update the last location
                last = nums[i]
            if cntCows >= cows:
                return True
                
        return False

    """ Function to find the maximum possible minimum
    distance 'k' cows can have between them in 'nums'"""
    def aggressiveCows(self, nums, k):
        # Size of array
        n = len(nums)
        
        # Sort the nums
        nums.sort()
        
        limit = nums[-1] - nums[0]
        for i in range(1, limit + 1):
            if not self.canWePlace(nums, i, k):
                return i - 1
                
        # Return the answer
        return limit

if __name__ == "__main__":
    nums = [0, 3, 4, 7, 10, 9]
    k = 4
    
    # Create an instance of the Solution class
    sol = Solution()
    
    ans = sol.aggressiveCows(nums, k)
    
    # Output the result
    print("The maximum possible minimum distance is:", ans)
Complexity Analysis: 
Time Complexity:O(NlogN) + O(N *(max-min)), where N is size of the array, max is the maximum element in array, min is the minimum element in array.
O(NlogN) for sorting the array. The loop runs for 1 to (max-min) to check all possible distances. Inside the loop, canWePlace() function is being called for each distance. Now, inside the canWePlace() function, the loop runs for N times.

Space Complexity: As no additional space is used, so the Space Complexity is O(1).


#Binary Search

Intuition: 
Here, the idea is to use binary search as the search range from [1 , max-min] is sorted. So, the brute-force solution can be optimized by dividing the space into two halves: one consisting of potential answers and the other of non-viable options.

Approach: 
Working of aggresiveCows(nums, k):
First, sort the array. Sorting is crucial as it allows us to efficiently apply binary search later, focusing on minimizing the maximum distance between cows.
Initialize low as 1, which represents the minimum possible distance between any two cows and initialize high as the maximum possible distance between the first and the last stall(difference between the first and last element of the sorted array).
Iterate the search space using a while loop till low is less than or equal to high. Calculate the mid point as the average of low and high. Use the canWePlace function to check if it's possible to place all cows with at least mid distance apart.
If placing cows with mid distance apart is possible (canWePlace returns true), update low to mid + 1 to search for potentially larger distances. Else, update high to mid - 1 to search for smaller distances.
Once the binary search concludes (low > high), high holds the maximum distance that can be achieved while still allowing cows to be placed (high is the largest distance where canWePlace was successful).

Working of canWePlace(nums, dist, cow):
Start by getting the size of the array and store it in 'n'. Initialize 'cntCows' to 1, indicating the number of cows already placed (starting with the first cow) also initialize 'last' to first element of array, which represents the position of the last placed cow.
Iterate through the array and check if the distance between the current position and the last placed cow is greater than or equal to dist. If true, it means you can place another cow at current position. Increment 'cntCows' to reflect placing another cow. Update 'last' to current element, marking current element as the position of the last placed cow.
If the loop completes without placing all cows (cntCows < cows), return false, indicating it's not possible to place all cows with at least dist distance apart.


class Solution:
    """Function to check if we can place 'cows' 
    cows with at least 'dist' distance apart"""
    def canWePlace(self, nums, dist, cows):
        # Size of array
        n = len(nums)
        
        # Number of cows placed
        cntCows = 1
        
        # Position of last placed cow
        last = nums[0]
        for i in range(1, n):
            if nums[i] - last >= dist:
                # Place next cow
                cntCows += 1
                
                # Update the last location
                last = nums[i]
            if cntCows >= cows:
                return True
                
        return False

    """ Function to find the maximum possible minimum
    distance 'k' cows can have between them in 'nums'"""
    def aggressiveCows(self, nums, k):
        # Size of array
        n = len(nums)
        
        # Sort the nums
        nums.sort()
        
        low = 1
        high = nums[n - 1] - nums[0]
        # Apply binary search
        while low <= high:
            mid = (low + high) // 2
            if self.canWePlace(nums, mid, k):
                low = mid + 1
            else:
                high = mid - 1
        return high

if __name__ == "__main__":
    nums = [0, 3, 4, 7, 10, 9]
    k = 4
    
    # Create an instance of the Solution class
    sol = Solution()
    
    ans = sol.aggressiveCows(nums, k)
    
    # Output the result
    print("The maximum possible minimum distance is:", ans)
Complexity Analysis: 
Time Complexity:O(NlogN) + O(N *log(max-min)), where N is size of the array, max is the maximum element in array, min is the minimum element in array.
O(NlogN) for sorting the array. As binary search is applied, which runs for 1 to (max-min) to check all possible distances, so O(log(max-min)). Inside the loop, canWePlace() function is being called for each distance. Now, inside the canWePlace() function, the loop runs for N times.

Space Complexity: As no additional space is used, so the Space Complexity is O(1).

  '''
class Solution:
    def canWePlace(self, nums, dist, cows):
        n = len(nums)
        cntCows = 1
        
        # Position of last placed cow
        last = nums[0]
        for i in range(1, n):
            if nums[i] - last >= dist:
                cntCows += 1
                # Update the last location
                last = nums[i]
            if cntCows >= cows:
                return True
                
        return False
    def aggressiveCows(self, nums, k):
        n = len(nums)
        nums.sort()
        
        low = 1
        high = nums[n - 1] - nums[0]
        # Apply binary search
        while low <= high:
            mid = (low + high) // 2
            if self.canWePlace(nums, mid, k):
                low = mid + 1
            else:
                high = mid - 1
        return high

