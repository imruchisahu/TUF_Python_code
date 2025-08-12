'''
Given a sorted array arr of size n, containing integer positions of n gas stations on the X-axis, and an integer k, place k new gas stations on the X-axis.



The new gas stations can be placed anywhere on the non-negative side of the X-axis, including non-integer positions.



Let dist be the maximum distance between adjacent gas stations after adding the k new gas stations.



Find the minimum value of dist.


Examples:
Input: n = 10, arr = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10], k = 9

Output: 0.50000

Explanation:

One of the possible ways to place 10 gas stations is [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10].

Thus the maximum difference between adjacent gas stations is 0.5.

Hence, the value of dist is 0.5.

It can be shown that there is no possible way to add 10 gas stations in such a way that the value of dist is lower than this.

Input : n = 10, arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 1

Output: 1.00000

Explanation:

One of the possible ways to place 1 gas station is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].
New Gas Station is at 11.
Thus the maximum difference between adjacent gas stations is still 1.
Hence, the value of dist is 1.
It can be shown that there is no possible way to add 1 gas station in such a way that the value of dist is lower than this. 
Input: n = 10, arr= [3, 6, 12, 19, 33, 44, 67, 72, 89, 95], k = 2

Output:
14.00000
Constraints:
10 <= n <= 5000 
0 <= arr[i] <= 109
arr is sorted in a strictly increasing order 
0 <= k <= 105


#Brute


Intuition: 
The idea here is to use very straightforward approach to solve this problem by using extra space. Declare an array of size n-1, where n is the size of the array given. Each of its indexes will represent the respective sections between the given gas stations. In each iteration, identify the index, such that subtraction of element at that index from element at the very next index is the maximum. Then, insert new stations into that section to reduce that maximum distance. The number of stations inserted in each section will be tracked using the previously declared array of size n-1.
Finally, after placing all the stations find the maximum distance between two consecutive stations. Among all the values of distances, the maximum one will be our answer.
Approach: 
First, declare an array ‘howMany’ of size n-1, to keep track of the number of placed gas stations, where n is the size of the array provided.
Next, traverse the gas stations from 1 to k using a loop and pick gas stations one at a time.
Then, using a nested loop, identify a index, such that subtraction of element at that index from element at the very next index is the maximum and insert the current gas station between arr[index] and arr[index+1] (i.e. howMany[i]++).
Finally, after placing all the new stations, find the distance between two consecutive gas stations. For a particular section, distance = section_length / (number_of_stations_ inserted+1) = (arr[i+1]-arr[i]) / (howMany[i]+1)
Among all the distances, the maximum one will be the answer.


class Solution:
    """ Function to minimize the maximum
    distance between gas stations """
    def minimiseMaxDistance(self, arr, k):
        n = len(arr)  
        howMany = [0] * (n - 1)

        # Pick and place k gas stations
        for gasStations in range(1, k + 1):
        
            maxSection = -1
            maxInd = -1
        
            """ Find the maximum section 
            and insert the gas station"""
            for i in range(n - 1):
                diff = arr[i + 1] - arr[i]
                sectionLength = diff / (howMany[i] + 1)
            
                """ Update the maximum section
                length and its index """
                if sectionLength > maxSection:
                    maxSection = sectionLength
                    maxInd = i
                  
            """ Insert the current gas 
            station into the section"""
            howMany[maxInd] += 1

        # Find the maximum distance i.e. the answer
        maxAns = -1
    
        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            sectionLength = diff / (howMany[i] + 1)
            maxAns = max(maxAns, sectionLength)
        
        return maxAns

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 4

    # Create an instance of the Solution class
    sol = Solution()

    # Call the minimiseMaxDistance method and print the result
    ans = sol.minimiseMaxDistance(arr, k)
    print(f"The answer is: {ans:.6f}")
Complexity Analysis: 
Time Complexity:O(k*N) + O(N), N is size of the given array, k is number of gas stations to be placed. O(k*N) to insert k gas stations between the existing stations with maximum distance. Another O(N) for finding the answer i.e. the maximum distance.

Space Complexity: O(N-1), As an array is used to keep track of placed gas stations.

#Better Approach
Intuition: 
The idea here is to use the Heap data structure, which can be implemented as a Priority Queue, to solve the problem more efficiently. Instead of the brute-force approach where we iterate over each gas station to find the maximum distance to the next one, we can optimize this using a heap.
In a max heap implementation, the largest element is always at the root. This property allows us to efficiently retrieve the maximum distance. Store the elements in the heap as pairs, where each pair consists of the distance and its corresponding index. This way, we can keep track of the distances and their respective positions as we process each gas station.
By using a max heap (implemented via a priority queue), we avoid the need to iterate through the array multiple times to find the maximum distance manually. Instead, the heap structure inherently keeps track of the maximum distance, allowing us to place each gas station optimally.
Approach: 
First, declare an array howMany of size n-1, to keep track of the number of placed gas stations and a priority queue that uses max heap, where n is the size of array provided in question.
Now, insert the first n-1 indices with the respective distance value, for every index.
Next, using a loop we will pick k gas stations one at a time. Then pick the first element of the priority queue as this is the element with the maximum distance. Let’s call the index ‘secInd’.
Now place the current gas station at ‘secInd’(howMany[secInd]++) and calculate the new section length. After that, again insert the pair(new section length, secInd) into the priority queue for further consideration.
After performing all the steps for k gas stations, the distance at the top of the priority queue will be the answer as we want the maximum distance.

import heapq

class Solution:
    """ Function to minimize the maximum
        distance between gas stations """
    def minimiseMaxDistance(self, arr, k):
        
        n = len(arr) 
        
        """ Array to store how many gas 
            stations are placed in each section """
        howMany = [0] * (n - 1)
        
        """ Min heap to store sections by
            their current maximum distance """
        pq = []

        """ Insert first n-1 elements into priority
            queue with respective distance values """
        for i in range(n - 1):
            heapq.heappush(pq, (-float(arr[i + 1] - arr[i]), i))

        for gasStations in range(1, k + 1):
            """ Find the maximum section 
                and insert the gas station """
            neg_dist, secInd = heapq.heappop(pq) 
            
             # Get the section with maximum distance
            max_dist = -neg_dist 
            
            # Insert current gas station into section
            howMany[secInd] += 1

            """ Calculate the initial difference
                between adjacent gas stations """
            inidiff = float(arr[secInd + 1] - arr[secInd])

            """ Calculate the new section length 
                after inserting another gas station """
            newSecLen = inidiff / (howMany[secInd] + 1)

            """ Push the updated section 
                back into the priority queue """
            heapq.heappush(pq, (-newSecLen, secInd))

        """ Return the maximum distance in
        the top section of the heap"""
        return -pq[0][0]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 4

    # Create an instance of the Solution class
    sol = Solution()

    # Call the minimiseMaxDistance method and print the result
    ans = sol.minimiseMaxDistance(arr, k)
    print(f"The answer is: {ans}")
Complexity Analysis: 
Time Complexity:O(NlogN + klogN), N is size of the given array, k = no. of gas stations to be placed. As, the insert operation of priority queue takes logN time complexity. O(NlogN) for inserting all the indices with distance values and O(klogN) for placing the gas stations.

Space Complexity:O(N-1)+O(N-1). The first O(N-1) is for the array to keep track of placed gas stations and the second one is for the priority queue.


#Optimal Approach
Intuition: 
The idea here is to use the Binary Search algorithm to optimize the approach. The primary objective of the Binary Search algorithm is to efficiently determine the appropriate half to eliminate, thereby reducing the search space by half. It does this by determining a specific condition that ensures that the target is not present in that half.

Observation:
Minimum possible answer: The minimum possible answer is obtained when all the gas stations are placed in a single location. In this case, the maximum distance will be 0.
Maximum possible answer: Stations will not be placed before the first or after the last station; instead, they will be placed in between the existing stations. Therefore, the maximum possible answer is determined by the maximum distance between two consecutive existing stations.
Upon closer observation, it can be recognized that the answer space ranges between [0, max(dist)] and it is sorted. Additionally, a pattern can be identified that allows the space to be divided into two halves: one consisting of potential answers and the other of non-viable options. Therefore, binary search will be applied on the answer space.

Changes in the binary search algorithm to apply it to the decimal answer space:
The traditional binary search algorithm used for integer answer space won't be effective in this case, as the answer space consists of decimal numbers. Changes need to be made to adjust some conditions to tailor the algorithm to this specific context. These changes are as follows:
The condition 'while(low <= high)' inside the 'while' loop won't work for decimal answers and might lead to a TLE (Time Limit Exceeded) error. To avoid this, the condition can be modified to 'while(high - low > 10^(-6))'. This ensures that only differences up to the 6th decimal place are considered. Any differences beyond this decimal precision won't be taken into account, as answers within 10^-6 of the actual answer are explicitly accepted by the question.
The operation 'low = mid + 1' is used to eliminate the left half. However, to ensure that we do not skip over potential decimal numbers and possibly miss the actual answer, 'low = mid' will be used instead.
Similarly, the operation 'high = mid - 1' is used to eliminate the right half. However, to ensure that potential decimal numbers are not overlooked and that the actual answer is not missed, 'high = mid' will be used instead.<.li>
Approach: 
Binary search is being applied on the answer, specifically on the possible values of distances. Therefore, a method needs to be devised to determine the number of gas stations that can be placed for a particular value of distance.

Working of minimiseMaxDistance(arr, k):
The maximum distance between two consecutive gas stations, denoted as max(dist), is first determined.
Pointers, denoted as low and high, are initially positioned. Low points to 0, and high points to max(dist).
Employ the while with the condition ‘while(high - low > 10^(-6))’. Within the loop, the value of ‘mid’ is calculated using the formula mid = (low + high) / 2.0.
Invoke the ‘numberOfGasStationsRequired()’ function with ‘mid’ as the potential distance value to determine the number of gas stations that can be placed.
If the result returned by the function is greater than k, the left half is eliminated (low = mid). Otherwise, the right half is eliminated (high = mid).
Finally, outside the loop, return either low or high as their difference is less than or equal to 10^(-6), both potentially representing the answer. Here, 'high' is returned as the chosen possible answer.

Working of numberOfGasStationsRequired(dist, arr):
First, initialize few variables: 'n' stores the size of the vector arr and 'cnt' is initialized to count the number of gas stations required.
Iterate through the array and for each pair of consecutive elements, calculate the 'numberInBetween', which represents the number of gas stations needed between these two points. This gives an estimate of how many stations would be needed if they were evenly spaced along the distance 'dist'.
If the actual distance calculated perfectly matches (dist * numberInBetween), adjust 'numberInBetween' by subtracting 1. This adjustment is intended to handle cases where the distance exactly matches the spacing defined by 'dist'. Otherwise increase the 'cnt' by 'numberInBetween'. Finally return 'cnt' variable.


import math

class Solution:
    # Function to calculate the number of gas 
    # stations required for given distance
    def numberOfGasStationsRequired(self, dist, arr):
        n = len(arr)
        cnt = 0
        for i in range(1, n):
            # Calculate number of gas stations 
            # needed between two points
            numberInBetween = (arr[i] - arr[i - 1]) / dist
            
            # Adjust if exact distance fits perfectly
            if (arr[i] - arr[i - 1]) == (dist * int(numberInBetween)):
                numberInBetween -= 1

            cnt += int(numberInBetween)
        return cnt

    # Function to minimize the maximum 
    # distance between gas stations
    def minimiseMaxDistance(self, arr, k):
        n = len(arr)
        low = 0
        high = 0

        # Find the maximum distance between 
        # consecutive gas stations
        for i in range(n - 1):
            high = max(high, arr[i + 1] - arr[i])

        # Apply Binary search to find the 
        # minimum possible maximum distance
        diff = 1e-6
        while high - low > diff:
            mid = (low + high) / 2.0
            cnt = self.numberOfGasStationsRequired(mid, arr)

            # Adjust the search range based on the 
            # number of gas stations required
            if cnt > k:
                low = mid
            else:
                high = mid

        # Return the smallest maximum distance found
        return high


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 4

    # Create an instance of the Solution class
    sol = Solution()

    # Call the minimiseMaxDistance method and print the result
    ans = sol.minimiseMaxDistance(arr, k)
    print(f"The answer is: {ans}")
Complexity Analysis: 
Time Complexity:O(N*log(Len)) + O(N), N is size of the given array, Len is length of the answer space. Binary search is being applied on the answer space. For every possible answer, the function numberOfGasStationsRequired() is called, which has a time complexity of O(N). Additionally, O(N) time complexity is incurred initially for finding the maximum distance.

Space Complexity: As no additional space is used, so the Space Complexity is O(1).

'''
import math

class Solution:
    def numberOfGasStationsRequired(self, dist, arr):
        n = len(arr)
        cnt = 0
        for i in range(1, n):
            numberInBetween = (arr[i] - arr[i - 1]) / dist
            if (arr[i] - arr[i - 1]) == (dist * int(numberInBetween)):
                numberInBetween -= 1

            cnt += int(numberInBetween)
        return cnt
    def minimiseMaxDistance(self, arr, k):
        n = len(arr)
        low = 0
        high = 0

        # Find the maximum distance between 
        # consecutive gas stations
        for i in range(n - 1):
            high = max(high, arr[i + 1] - arr[i])

        # Apply Binary search to find the minimum possible maximum distance
        diff = 1e-6
        while high - low > diff:
            mid = (low + high) / 2.0
            cnt = self.numberOfGasStationsRequired(mid, arr)
            if cnt > k:
                low = mid
            else:
                high = mid
        return high


