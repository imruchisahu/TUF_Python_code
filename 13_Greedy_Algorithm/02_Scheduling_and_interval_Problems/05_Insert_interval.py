'''Given a 2D array Intervals, where Intervals[i] = [start[i], end[i]] represents the start and end of the ith interval, the array represents non-overlapping intervals sorted in ascending order by start[i]. 



Given another array newInterval, where newInterval = [start, end] represents the start and end of another interval, merge newInterval into Intervals such that Intervals remain non-overlapping and sorted in ascending order by start[i].



Return Intervals after the insertion of newInterval.


Examples:
Input : Intervals = [ [1, 3] , [6, 9] ] , newInterval = [2, 5]



Output : [ [1, 5] , [6, 9] ]



Explanation : After inserting the newInterval the Intervals array becomes [ [1, 3] , [2, 5] , [6, 9] ].

So to make them non overlapping we can merge the intervals [1, 3] and [2, 5].

So the Intervals array is [ [1, 5] , [6, 9] ].

Input : Intervals = [ [1, 2] , [3, 5] , [6, 7] , [8,10] ] , newInterval = [4, 8]



Output : [ [1, 2] , [3, 10] ]



Explanation : The Intervals array after inserting newInterval is [ [1, 2] , [3, 5] , [4, 8] , [6, 7] , [8, 10] ].

We merge the required intervals to make it non overlapping.

So final array is [ [1, 2] , [3, 10] ].

Input : Intervals = [ [1, 2] , [3, 5] , [6, 7] , [8,10] ] , newInterval = [1, 8]

Output:
[[1, 10]]
Constraints:
0 <= Intervals.length <= 105
0 <= start[i] < end[i] <= 107
0 <= start < end <= 107
Intervals[i].length = 2
newInterval.length = 2
Intuition
Inserting a new interval into a sorted list of non-overlapping intervals involves a straightforward approach. Start by adding intervals that come completely before the new interval. For intervals that overlap with the new one, adjust the start and end times to merge them into a single interval. After handling the overlapping intervals, add any remaining intervals that come after the new interval.
Approach
Initialize Result Structure: Start by creating an empty 2D array to store the resulting list of intervals after insertion and merging. Also, set up an index to keep track of your position as you iterate through the intervals.
Insert Intervals Before the New Interval: Go through the intervals that end before the new interval starts. These intervals do not overlap with the new interval and can be directly added to the result.
Merge Overlapping Intervals: Next, look at the intervals that start before or at the same time the new interval ends. These intervals overlap with the new interval and need to be merged. Update the new interval’s start time to the earliest start time and its end time to the latest end time among the overlapping intervals.
Add the Merged Interval: Once all overlapping intervals have been merged, add the new interval, now updated with its new start and end times, to the result.
Insert Remaining Intervals: Finally, add any intervals that start after the new interval ends. These intervals do not overlap with the new interval and can be directly added to the result.
Return the Result: The result array now contains the updated list of intervals, with the new interval correctly inserted and merged.

class Solution:
     # To insert new interval
    def insertNewInterval(self, intervals, new_interval):
        # Initialize result
        res = []
        
        # Track the index 
        i = 0
        
        # Get total intervals
        n = len(intervals)
        
        # Insert intervals before new_interval
        while i < n and intervals[i][1] < new_interval[0]:
            # Add intervals to the result 
            # list until their end time 
            # is before the start time 
            # of new_interval
            res.append(intervals[i])
            # Move to next interval
            i += 1
        
        # Merge overlapping intervals
        while i < n and intervals[i][0] <= new_interval[1]:
            # Update the start time of new_interval to the minimum 
            # of its current start time and the start time of the 
            # current interval
            new_interval[0] = min(new_interval[0], intervals[i][0])
            # Update the end time of new_interval to the maximum 
            # of its current end time and the end time of the 
            # current interval
            new_interval[1] = max(new_interval[1], intervals[i][1])
            # Move to the next interval
            i += 1
        
        # Insert the merged interval
        res.append(new_interval)
        
        # Insert remaining 
        # intervals after 
        # new_interval
        while i < n:
            # Add the remaining 
            # intervals after new_interval
            # to the result list
            res.append(intervals[i])
            # Move to next interval
            i += 1
        
        # Return result 
        return res

# Test the function
intervals = [[1, 2], [3, 4], [6, 7], [8, 10], [12, 16]]
new_interval = [5, 8]

print("Intervals Array:", intervals)
print("New Interval to be Inserted:", new_interval)

solution = Solution()
result = solution.insertNewInterval(intervals, new_interval)
print("Resulting Intervals after Insertion:", result)

Complexity Analysis
Time Complexity: O(N) where N is the number of intervals.This is because we iterate through the intervals linearly in a single pass.
During this pass, we perform three main operations: inserting intervals that come before the new interval, merging overlapping intervals with the new interval, and inserting intervals that come after the new interval.
Each of these operations is done within the same traversal of the intervals array, ensuring that the algorithm maintains a linear time complexity.
Space Complexity: O(N) where N is the number of intervals. We use an additional space to store the result list of intervals. In the worst case, where all intervals need to be included in the result list, the size of the result list will be equal to the size of the input list plus one.

'''
class Solution:
    def insertNewInterval(self, Intervals, newInterval):
        res = []
        i = 0
        n = len(Intervals)
        while i < n and Intervals[i][1] < newInterval[0]:
            res.append(Intervals[i])
            i += 1
        while i < n and Intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], Intervals[i][0])
            newInterval[1] = max(newInterval[1], Intervals[i][1])
            i += 1
        res.append(newInterval)
        while i < n:
            res.append(Intervals[i])
            i += 1
        return res