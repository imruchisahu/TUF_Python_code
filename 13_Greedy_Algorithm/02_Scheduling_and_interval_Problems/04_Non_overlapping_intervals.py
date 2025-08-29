'''
Given an array of N intervals in the form of (start[i], end[i]), where start[i] is the starting point of the interval and end[i] is the ending point of the interval, return the minimum number of intervals that need to be removed to make the remaining intervals non-overlapping.


Examples:
Input : Intervals = [ [1, 2] , [2, 3] , [3, 4] ,[1, 3] ]



Output : 1



Explanation : You can remove the interval [1, 3] to make the remaining interval non overlapping.

Input : Intervals = [ [1, 3] , [1, 4] , [3, 5] , [3, 4] , [4, 5] ]



Output : 2



Explanation : You can remove the intervals [1, 4] and [3, 5] and the remaining intervals becomes non overlapping.

Input : Intervals = [ [1, 10] , [1, 4] , [3, 8] , [3, 4] , [4, 5] ]

Output:
3
Constraints:
1 <= Intervals.length <= 105
0 <= start[i] < end[i] <= 105
Intervals[i].length = 2

Intuition
Determining if one interval overlaps with another can be done by checking if the end of the current interval is greater than the start of the next interval. Minimizing the number of intervals to remove involves keeping the end points of the selected intervals as small as possible. This maximizes the space available for subsequent intervals.
Approach
Sort the intervals based on their end times in ascending order to prioritize intervals that finish earliest.
Keep a count of the number of non-overlapping intervals and remember the end time of the last selected interval.
Go through the sorted intervals starting from the second one. For each interval:
Check if the start time of the current interval is at or after the end time of the last selected interval.
If it is, select this interval, update the end time to the current interval's end time, and increase the count of non-overlapping intervals.
Determine the minimum number of intervals to remove by subtracting the count of non-overlapping intervals from the total number of intervals.
Return the minimum number of intervals to remove to make the rest non-overlapping.
class Solution:
    # Function to compare intervals based on ending times
    @staticmethod
    def comp(val1, val2):
        # Compare the ending times of the intervals
        return val1[1] < val2[1]

    # Function to count the maximum number of non-overlapping intervals
    def MaximumNonOverlappingIntervals(self, intervals):
        # Sort the intervals based on their ending times
        intervals.sort(key=lambda x: x[1])

        # Get total number of intervals
        n = len(intervals)

        # Initialize counter
        cnt = 1

        # Keep track of the ending time
        last_end_time = intervals[0][1]

        # Iterate through all intervals
        for i in range(1, n):
            # Check if the starting time of the current 
            # interval is greater than or equal to the 
            # ending time of the last selected interval
            if intervals[i][0] >= last_end_time:
                # Increment counter
                cnt += 1
                # Update the ending time
                last_end_time = intervals[i][1]

        return n-cnt

# Example usage
if __name__ == "__main__":
    obj = Solution()
    intervals = [[0, 5], [3, 4], [1, 2], [5, 9], [7, 9]]
    
    for i, interval in enumerate(intervals):
        print(f"Interval {i + 1} Start: {interval[0]} End: {interval[1]}")
    
    ans = obj.MaximumNonOverlappingIntervals(intervals)
    print(f"Maximum Non-Overlapping Intervals: {ans}")

    
Complexity Analysis
Time Complexity: O(N log N + N) where N is the number of intervals. We sort the intervals based on their end timings which takes up O(N log N). We then iterate over the sorted intervals to find the maximum number of non-overlapping intervals.
Space Complexity: O(1) as no additional data structure has been used.

'''
class Solution:
    def MaximumNonOverlappingIntervals(self, Intervals):
        Intervals.sort(key=lambda x: x[1])
        n = len(Intervals)
        cnt = 1
        last_end_time = Intervals[0][1]
        for i in range(1, n):
            if Intervals[i][0] >= last_end_time:
                cnt += 1
                last_end_time = Intervals[i][1]

        return n-cnt