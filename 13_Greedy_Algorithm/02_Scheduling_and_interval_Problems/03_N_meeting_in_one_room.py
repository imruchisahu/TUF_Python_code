'''
Given one meeting room and N meetings represented by two arrays, start and end, where start[i] represents the start time of the ith meeting and end[i] represents the end time of the ith meeting, determine the maximum number of meetings that can be accommodated in the meeting room if only one meeting can be held at a time.


Examples:
Input : Start = [1, 3, 0, 5, 8, 5] , End = [2, 4, 6, 7, 9, 9]

Output : 4

Explanation : The meetings that can be accommodated in meeting room are (1,2) , (3,4) , (5,7) , (8,9).

Input : Start = [10, 12, 20] , End = [20, 25, 30]

Output : 1

Explanation : Given the start and end time, only one meeting can be held in meeting room.

Input : Start = [1, 4, 6, 9] , End = [2, 5, 7, 12]

Output:
4
Constraints:
1 <= N <= 105
0 <= start[i] < end[i] <= 105

Intuition
If there are two meetings, one that finishes early and another that finishes later, it is better to choose the meeting that finishes early. Choosing a meeting that ends earlier frees up the room sooner, allowing more meetings to be accommodated afterwards. By prioritizing meetings that end early, the meeting room is utilized more efficiently, maximizing the total number of meetings that can be held.
Approach
Use a vector to store pairs of start and end times of the meetings. This helps in easily accessing and sorting the meeting times.
Sort the meetings based on their end times in ascending order. This ensures that the meetings which finish earliest are considered first.
Create a variable to keep track of the end time of the last selected meeting. Also, initialize a counter to count the number of meetings that can be accommodated.
Loop through the sorted meetings and for each meeting:
Check if the start time of the current meeting is greater than the end time of the last selected meeting.
If true, select the current meeting, update the end time to the end time of the current meeting, and increment the counter.
After iterating through all meetings, the counter will contain the maximum number of non-overlapping meetings that can be accommodated.
class Solution:
    # Function to find the maximum number of meetings that can be held
    def maxMeetings(self, start, end):
        n = len(start)
        # List to store meetings
        meetings = []
        
        # Fill the meetings list with start and end times
        for i in range(n):
            meetings.append((start[i], end[i]))

        # Sort the meetings based on end times in ascending order
        meetings.sort(key=lambda x: x[1])

        # The end time of last selected meeting
        limit = meetings[0][1]
        # Initialize count
        count = 1

        # Iterate through the meetings to select the maximum number of non-overlapping meetings
        for i in range(1, n):
            # If the current meeting starts after the last selected meeting ends
            if meetings[i][0] > limit:
                # Update the limit to the end time of the current meeting
                limit = meetings[i][1]
                # Increment count
                count += 1

        # Return count
        return count

# Example usage
if __name__ == "__main__":
    obj = Solution()
    # Start and end times of the meetings
    start = [1, 3, 0, 5, 8, 5]
    end = [2, 4, 6, 7, 9, 9]
    # Get the maximum number of meetings that can be held
    maxMeetings = obj.maxMeetings(start, end)
    # Output the maximum number of meetings
    print("Maximum number of meetings:", maxMeetings)

    
Complexity Analysis
Time Complexity: O(N+N logN) where 𝑁 is the size of the start and end arrays. The O(N) term accounts for filling the meetings array with start and end times. The O(NlogN) term arises from sorting the meetings based on their end times. After sorting, the function iterates through the sorted meetings in O(N) time to count the maximum number of non-overlapping meetings.
Space Complexity: O(N) since we used an additional data structure for storing the start time and end time.

'''
class Solution:
    def maxMeetings(self, start, end):
        n = len(start)
        meetings = []
        for i in range(n):
            meetings.append((start[i], end[i]))
        meetings.sort(key=lambda x: x[1])
        limit = meetings[0][1]
        count = 1
        for i in range(1, n):
            if meetings[i][0] > limit:
                limit = meetings[i][1]
                count += 1
        return count
