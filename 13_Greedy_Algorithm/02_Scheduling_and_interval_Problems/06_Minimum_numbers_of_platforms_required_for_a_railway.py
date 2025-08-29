'''
Given the arrival and departure times of all trains reaching a particular railway station, determine the minimum number of platforms required so that no train is kept waiting. Consider all trains arrive and depart on the same day.



In any particular instance, the same platform cannot be used for both the departure of one train and the arrival of another train, necessitating the use of different platforms in such cases.


Examples:
Input : Arrival = [0900, 0940, 0950, 1100, 1500, 1800] , Departure = [0910, 1200, 1120, 1130, 1900, 2000]



Output : 3



Explanation : The first , second , fifth number train can use the platform 1.

The third and sixth train can use the platform 2.

The fourth train will use platform 3.

So total we need 3 different platforms for the railway station so that no train is kept waiting.

Input : Arrival = [0900, 1100, 1235] , Departure = [1000, 1200, 1240]



Output : 1



Explanation : All the three trains can use the platform 1.

So we required only 1 platform.

Input : Arrival = [0900, 1000, 1200] , Departure = [1000, 1200, 1240]

Output:
2
Constraints:
1 <= N <= 105
0000 <= Arrival[i] <= Departure[i] <= 2359
#Brute
Intuition
Consider each train's schedule and see how many other trains are at the station at the same time. For each train, compare its arrival and departure times with those of all other trains to find overlaps.

To find the overlap, check if the arrival time (or the departure time) of the current train lies in between the arrival time and departure time of another train. If the conditions are met, it means the trains overlap, and you need to increment the count of overlapping trains.

Count how many trains are at the station simultaneously and keep track of the highest number you find.
Approach
Start by setting an initial count to one, assuming that at least one platform is needed.
Loop through each train's arrival time to check how many other trains are at the station simultaneously, one by one.
For each train, start a counter at one to include the current train itself, keeping track of how many trains overlap with it.
Within the loop for each train, compare it with all subsequent trains to check if their schedules overlap with the current train's schedule.
During these comparisons, check if the current train’s arrival and departure times overlap with those of the subsequent trains. If they do, increment the counter.
After counting overlaps for the current train, update the initial count to reflect the highest number of overlapping trains found, ensuring you are tracking the maximum number of platforms needed.
After looping through all trains and checking overlaps, the highest count will be the minimum number of platforms required to ensure no train has to wait.

class Solution:
    # Function to find minimum number of platforms required
    def findPlatform(self, Arrival, Departure):
        n = len(Arrival)

        # To store the result
        ans = 1

        # Iterate on the trains platforms
        for i in range(n):
            
            count = 1

            # Iterate on all the trains 
            for j in range(n):
                # Check with other trains
                if i != j:

                    # Check for the overlapping trains 
                    if Arrival[i] >= Arrival[j] and Departure[j] >= Arrival[i]:
                        # Increment count
                        count += 1

                    # Update the minimum platforms needed
                    ans = max(ans, count)

        # Return number of platforms
        return ans


if __name__ == "__main__":
    arr = [900, 945, 955, 1100, 1500, 1800]
    dep = [920, 1200, 1130, 1150, 1900, 2000]

    # Creating an instance of Solution class
    sol = Solution()

    # Function call to find minimum number of platforms required
    ans = sol.findPlatform(arr, dep)

    print("Minimum number of Platforms required:", ans)

Complexity Analysis
Time Complexity: O(N2) where N is the number of trains.
The two nested loops result in quadratic time complexity.
Space Complexity : O(1) because no extra space is used.

#optiml
Intuition
Start by sorting both the arrival and departure times. Once these times are sorted, it becomes much easier to keep track of the trains currently at the station. By moving through these sorted times, we can count how many trains have arrived but not yet departed at any given moment. The difference between the number of arrivals and departures at each point will tell us how many platforms are needed at that time. The highest number of platforms required during these times gives us the final answer.
Approach
Start by sorting both the arrival and departure arrays. Sorting helps in managing the train schedules efficiently.
Initialize two pointers, one for the arrival array and one for the departure array. These pointers will help in traversing both arrays simultaneously.
Also, initialize two variables to keep track of the count of platforms needed at any time and the maximum number of platforms needed.
Use a loop to iterate through the arrival and departure times. Compare the current arrival time with the current departure time using the two pointers.
If the arrival time is less than or equal to the departure time, it means a train has arrived before the earliest train has departed, so increment the count of platforms needed and move the arrival pointer to the next train.
If the arrival time is greater than the departure time, it means a train has departed, freeing up a platform. Decrement the count of platforms needed and move the departure pointer to the next train.
After each comparison, update the maximum number of platforms needed if the current count exceeds the previous maximum.
Continue this process until you have processed all trains, then return the maximum number of platforms needed, which will be the final answer.

class Solution:
     #  To find number of platforms
    def findPlatform(self, Arrival, Departure):
        n = len(Arrival)

        # Sort both arrival and departure arrays
        Arrival.sort()
        Departure.sort()

        ans = 1
        count = 1
        i, j = 1, 0

        # Iterate through the arrays
        while i < n and j < n:
            if Arrival[i] <= Departure[j]:
                # Increment count
                count += 1
                i += 1
            else:
                # Decrement count
                count -= 1
                j += 1
            # Find maximum
            ans = max(ans, count)
        return ans

# Test the solution
arr = [900, 945, 955, 1100, 1500, 1800]
dep = [920, 1200, 1130, 1150, 1900, 2000]

solution = Solution()
print("Minimum number of Platforms required:", solution.findPlatform(arr, dep))

Complexity Analysis
Time Complexity: O(N log N) where N is the size of each array.This is primarily due to the sorting operations on the arrival and departure arrays, each taking O(N log N). The subsequent traversal of the arrays using the two-pointer technique takes O(N), but this does not affect the overall complexity, which is dominated by the sorting step. Therefore, the combined time complexity remains O(N log N).
Space Complexity: O(1) as no extra space is used.

'''
class Solution:
    def findPlatform(self, Arrival, Departure):
        n = len(Arrival)
        Arrival.sort()
        Departure.sort()

        ans = 1
        count = 1
        i, j = 1, 0
        while i < n and j < n:
            if Arrival[i] <= Departure[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            ans = max(ans, count)
        return ans