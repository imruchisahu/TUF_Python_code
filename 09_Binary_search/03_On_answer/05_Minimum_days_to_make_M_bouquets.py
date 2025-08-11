'''Given n roses and an array nums where nums[i] denotes that the 'ith' rose will bloom on the nums[i]th day, only adjacent bloomed roses can be picked to make a bouquet. Exactly k adjacent bloomed roses are required to make a single bouquet. Find the minimum number of days required to make at least m bouquets, each containing k roses. Return -1 if it is not possible.


Examples:
Input: n = 8, nums = [7, 7, 7, 7, 13, 11, 12, 7], m = 2, k = 3

Output: 12

Explanation: On the 12th the first 4 flowers and the last 3 flowers would have already bloomed. So, we can easily make 2 bouquets, one with the first 3 and another with the last 3 flowers.

Input: n = 5, nums = [1, 10, 3, 10, 2], m = 3, k = 2

Output: -1

Explanation: If we want to make 3 bouquets of 2 flowers each, we need at least 6 flowers. But we are given only 5 flowers, so, we cannot make the bouquets.

Input: n = 5, nums = [1, 10, 3, 10, 2], m = 3, k = 1

Output:
10
1
2
3

Submit
Constraints:
 1 <= n <= 105
 1 <= nums[i] <= 109
 1 <= m <= 106
 1 <= k <= n

 
 #Linear Search
 Intuition: 
The very straightforward approach is to check all possible answers from range min to max linearly, where, min is the minimum element of the array and max is the maximum element of the array. Each number in the range shows the number of days. The minimum number of days for which at least 'm' bouquet can be made each containing 'k' rose will be our final answer.

Approach: 
Edge case: If the product k*m(minimum number of roses required) is greater than size of the array, then it is impossible to make bouquet, in that case return -1

Working of roseGarden(n, nums, k, m):
Calculate val as the product of 'm' (number of bouquets) and 'k'( number of roses each bouquet should have), ensuring it's cast to long long to avoid overflow. Determine the size n of the array.
Initialize mini and maxi to INT_MAX and INT_MIN, respectively, to find the first day when a flower blooms and the last on which all fowers should have already bloomed.
Iterate through the days starting from mini to maxi. For each day , use the possible function to check if the total number of bouquets on this day, each containing k roses is greater than or equal to 'k'. If yes, return the current day as an answer.
After coming out of the loop, return -1 as no day is found matching the constraints.

Working of possible(nums, day, k):
First, initialize 'n' is to the size of nums, which represents the number of flowers. Initialize 'cnt' to 0 which keeps track of how many flowers have bloomed within the current day threshold day. Initialize 'noOfB' of 0, keeps track of the total number of bouquets formed.
The function iterates through each flower's blooming day in nums. For each flower, if its blooming day is less than or equal to day, increment 'cnt' (indicating a flower that can be used to form a bouquet). If a flower's blooming day exceeds day, calculate how many complete bouquets (cnt / k) can be formed with the flowers that bloomed up to that point (cnt). Add this count to noOfB. Reset 'cnt' to zero because flowers blooming after day cannot be used for the current bouquet.
After iterating through all flowers, there might be remaining flowers (cnt) that have bloomed within day. Calculate how many additional bouquets can be formed with these remaining flowers and add this to noOfB.
Finally, check if the total number of bouquets (noOfB) formed is greater than or equal to m. If so, return true, indicating that it's possible to form at least m bouquets with the given constraints (day and k).If not, return false.



 class Solution:
    """Function to check if it's possible to make
    m bouquets with k flowers each on a given day"""
    def possible(self, nums, day, m, k):
        n = len(nums)
        
        # Count of flowers bloomed
        cnt = 0 
        
        # Count of bouquets formed
        noOfB = 0 

        # Count number of bouquets that can be formed
        for i in range(n):
            if nums[i] <= day:
                # Increment flower count
                cnt += 1 
            else:
                # Calculate number of bouquets formed with flowers <= day
                noOfB += (cnt // k)
                
                # Reset flower count
                cnt = 0 
        
        # Add remaining flowers as a bouquet
        noOfB += (cnt // k) 
        
        # Return true if enough bouquets can be formed
        return noOfB >= m 

    """Function to find the earliest day to
    make m bouquets of k flowers each"""
    def roseGarden(self, n, nums, k, m):
        # Calculate the minimum number of flowers required
        val = m * k 
        
        # Impossible case: not enough flowers to make m bouquets
        if val > n:
            return -1 
        
        # Find maximum and minimum bloom days in the array
        mini = float('inf')
        maxi = float('-inf')
        for num in nums:
            mini = min(mini, num) 
            maxi = max(maxi, num) 
        
        # Linear search to find the earliest day to make m bouquets
        for i in range(mini, maxi + 1):
            if self.possible(nums, i, m, k):
                return i

        # Return -1 if no such day exists
        return -1 

if __name__ == "__main__":
    arr = [7, 7, 7, 7, 13, 11, 12, 7] 
    
    n = len(arr)
    
    # Number of flowers per bouquet
    k = 3 
    
    # Number of bouquets needed
    m = 2 

    # Create an instance of the Solution class
    sol = Solution() 
    
    ans = sol.roseGarden(n, arr, k, m) 

    if ans == -1:
        print("We cannot make m bouquets.") 
    else:
        print(f"We can make bouquets on day {ans}") 
Complexity Analysis: 
Time Complexity:O((max-min+1) * N), where max is the maximum element of the array, min is the minimum element of the array, N is size of the array}.
As, running a loop to check answers that are in the range of [min, max]. For every possible answer, the possible() function is being called. Inside the possible() function, traversing the entire array, which results in O(N).


Space Complexity: As no additional space is used, so the Space Complexity is O(1).


#Binary Search
Intuition: 
The idea here is to use binary search algorithm as the search range[min, max] is sorted, where, min is the earliest and max is the latest day for a rose to bloom. So, if it's feasible to make m bouquets on day 'mid'((low+high)/2), eliminate the right half of the search space to search for an earlier day. Else, eliminate the left half to find a higher range of days. This way, the brute-force solution can be optimized.

Approach: 
Edge case: If the product k*m is greater than size of the array, then it is impossible to make bouquet, in that case return -1.

Working of roseGarden(n, nums, k, m):
Initialize mini to INT_MAX and maxi to INT_MIN to find the earliest and latest bloom days in the nums array.
Use binary search to find the earliest day (ans) where it’s possible to make m bouquets of k flowers each. Initialize left to mini and right to maxi. The range [low,high] defines the search space.
While left is less than or equal to right, calculate the middle day 'mid'. Use the possible function to check if it's feasible to make m bouquets on day mid. If feasible, update ans to mid and move right to mid - 1 to search for an earlier day. Otherwise, move left to mid + 1 to search in the higher range of days.
After the binary search completes, ans will hold the earliest day on which it's possible to make m bouquets of k flowers each. Return ans. If no such day exists (ans remains -1), return -1 indicating it's not possible under the given constraints.

Working of possible(nums, day, k):
First, initialize 'n' is to the size of nums, which represents the number of flowers. Initialize 'cnt' to 0 which keeps track of how many flowers have bloomed within the current day threshold day. Initialize 'noOfB' of 0, keeps track of the total number of bouquets formed.
The function iterates through each flower's blooming day in nums. For each flower, if its blooming day is less than or equal to day, increment 'cnt' (indicating a flower that can be used to form a bouquet). If a flower's blooming day exceeds day, calculate how many complete bouquets (cnt / k) can be formed with the flowers that bloomed up to that point (cnt). Add this count to noOfB. Reset 'cnt' to zero because flowers blooming after day cannot be used for the current bouquet.
After iterating through all flowers, there might be remaining flowers (cnt) that have bloomed within day. Calculate how many additional bouquets can be formed with these remaining flowers and add this to noOfB.
Finally, check if the total number of bouquets (noOfB) formed is greater than or equal to m. If so, return true, indicating that it's possible to form at least m bouquets with the given constraints (day and k).If not, return false.




class Solution:
    """Function to check if it's possible to make
    m bouquets with k flowers each on day """
    def possible(self, nums, day, m, k):
        n = len(nums)
        
        # Count of flowers bloomed
        cnt = 0 
        
        # Count of bouquets formed
        noOfB = 0 

        # Count number of bouquets that can be formed
        for i in range(n):
            if nums[i] <= day:
                # Increment flower count
                cnt += 1 
            else:
                """ Calculate number of bouquets
                formed with flowers <= day """
                noOfB += (cnt // k)
                
                # Reset flower count
                cnt = 0 
        
        # Add remaining flowers as a bouquet
        noOfB += (cnt // k) 
        
        """ Return true if enough 
        bouquets can be formed """
        return noOfB >= m 

    """ Function to find the earliest day to
    make m bouquets of k flowers each """
    def roseGarden(self, n, nums, k, m):
        
        """ Calculate the minimum 
        number of flowers required """
        val = m * k 
        
        """ Impossible case: not enough 
            flowers to make m bouquets """
        if val > n:
            return -1 
        
        """ Find maximum and minimum
            bloom days in the array """
        mini = float('inf')
        maxi = float('-inf')
        for num in nums:
            mini = min(mini, num) 
            maxi = max(maxi, num) 
        
        """ Binary search to find the
            earliest day to make m bouquets """
        left = mini 
        right = maxi 
        ans = -1
        while left <= right:
            
            # Calculate the middle day
            mid = left + (right - left) // 2 
            
            """ Check if it's possible to 
                make m bouquets on day mid """
            if self.possible(nums, mid, m, k):
                
                # Update the answer to mid
                ans = mid 
                
                # Try for a smaller day
                right = mid - 1 
            else:
                left = mid + 1 
        
        """ Return the earliest day or 
        -1 if no such day exists"""
        return ans 

if __name__ == "__main__":
    arr = [7, 7, 7, 7, 13, 11, 12, 7] 
    
    n = len(arr)
    
    # Number of flowers per bouquet
    k = 3 
    
    # Number of bouquets needed
    m = 2 

    # Create an instance of the Solution class
    sol = Solution() 
    
    ans = sol.roseGarden(n, arr, k, m) 

    if ans == -1:
        print("We cannot make m bouquets.") 
    else:
        print(f"We can make bouquets on day {ans}") 
Complexity Analysis: 
Time Complexity:O(log(max-min+1) * N), where max is the maximum element of the array, min is the minimum element of the array, N is size of the array.
As binary search is being applied on answers that are in the range of [min, max]. For every possible answer ‘mid’, the possible() function is being called. Inside the possible() function, traversing the entire array, which results in O(N).

Space Complexity: As no additional space is used, so the Space Complexity is O(1).
'''
class Solution:
    def possible(self, nums, day, m, k):
        n=len(nums)
        cnt=0
        noOfB = 0
        for i in range(n):
            if nums[i] <= day:
                cnt += 1
            else:
                noOfB += (cnt // k)
                cnt = 0
        noOfB += (cnt // k)
        return noOfB >= m
    def roseGarden(self, n, nums, k, m):
        val = m * k
        if val > n:
            return -1
        mini = float('inf')
        maxi = float('-inf')
        for num in nums:
            mini = min(mini, num)
            maxi= max(maxi, num) 
        left = mini 
        right = maxi 
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2 
            if self.possible(nums, mid, m, k):  
                ans = mid
                right = mid - 1 
            else:
                left = mid + 1  
        return ans
