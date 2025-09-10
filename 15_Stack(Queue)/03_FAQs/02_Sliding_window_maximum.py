'''
Given an array of integers arr, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.


Examples:
Input: arr = [4, 0, -1, 3, 5, 3, 6, 8], k = 3

Output: [4, 3, 5, 5, 6, 8]

Explanation: 



Window position          Max

------------------------     -----

[4 0 -1] 3 5 3 6 8      4

 4 [0 -1 3] 5 3 6 8      3

 4 0 [-1 3 5] 3 6 8      5

 4 0 -1 [3 5 3] 6 8      5

 4 0 -1 3 [5 3 6] 8      6

 4 0 -1 3 5 [3 6 8]     8



For each window of size k=3, we find the maximum element in the window and add it to our output array.

Input: arr = [20, 25], k = 2

Output: [25]

Explanation: There’s just one window of size 2 that is possible and the maximum of the two elements is our answer.

Input: arr = [1, 3, -1, -3, 5, 3, 6, 7], k = 3

Output:
[3, 3, 5, 5, 6, 7]
Constraints:
1 <= arr.length <= 105
-104 <= arr[i] <= 104
1 <= k <= arr.length

#Brute
Intuition:
A naive approach to solve this problem involves considering every window possible of size K and then finding the maximum element for each window.

Approach:
Traverse on the array getting all the windows possible of size K using a for loop.
For each window, find the maximum element using a nested for loop. Store the maximums obtained in a list.
Once the traversal for all the windows is complete, return the list as answer.

class Solution:
    # Function to get the maximum sliding window
    def maxSlidingWindow(self, arr, k):
        
        n = len(arr) # Size of array
        
        # To store the answer
        ans = []
        
        # Traverse on the array for valid window
        for i in range(n - k + 1):
            
            # To store the maximum of the window
            maxi = arr[i]
            
            # Traverse the window
            for j in range(i, i + k):
                # Update the maximum
                maxi = max(maxi, arr[j])
            
            # Add the maximum to the result
            ans.append(maxi)
        
        # Return the stored result
        return ans

# Creating an instance of Solution class
sol = Solution()

arr = [4, 0, -1, 3, 5, 3, 6, 8]
k = 3

# Function call to get the maximum sliding window
ans = sol.maxSlidingWindow(arr, k)

print("The maximum elements in the sliding window are: ")
for num in ans:
    print(num, end=" ")

Complexity Analysis:
Time Complexity: O((N-K)*K) (where N is the size of given array)
Using two nested loops.

Space Complexity: O(N-K)
Due to the size taken to return the answer.

#Optimal
Intuition:
In the earlier approach, scanning every element of the window repeatedly was resulting in increased time complexity. Instead, if there can be a way where the maximum element for a window can be found in constant time, the overall time complexity will improve significantly.
What is the best suitable data structure?
Every time the sliding window moves by one step, an element is added to the window and an previously added element is removed from the window. A data-structure that can push elements from one end and remove elements from the other end is queue. Every time the window moves by one step, the queue is updated to manage the current window elements.

Understanding:
The maximum element in a particular window can be found directly using the concept of monotonic queue, which includes storing the elements in a decreasing order. This way the maximum element will always be the front element in the queue which can be retrieved from the queue in constant time.
In order to maintain the decreasing order of elements in queue, before adding the new element to the queue, all the smaller elements already present in front of the queue can be popped out.

But, a queue data structure does not provide pop operation from the front. To overcome this, a Deque (Double Ended Queue) can be used, which enables efficient insertion and retrieval from both ends.
Approach:
Determine the size of the input array. Prepare a vector to store the results. Utilize a deque to maintain the indices of array elements within the current window.
For each element in the array, update the deque to maintain only the indices of elements within the current window by popping the elements from the front.
Ensure the deque maintains a monotonic decreasing order by removing indices of elements from the back that are less than or equal to the current element. Add the current element's index to the back of the deque.
Once the first window(of required size) is fully traversed, store the maximum element (located at the front of the deque) for each window position by adding the corresponding array value to the result.
Return the result that contains the maximum values for each sliding window position and is returned as the output.

from collections import deque

class Solution:
    # Function to get the maximum sliding window
    def maxSlidingWindow(self, arr, k):
        
        n = len(arr) # Size of array
        
        # To store the answer
        ans = []
        
        # Deque data structure
        dq = deque()
        
        # Traverse the array
        for i in range(n):
            
            # Update deque to maintain current window
            if dq and dq[0] <= (i - k):
                dq.popleft()
            
            # Maintain the monotonic (decreasing) 
            # order of elements in deque
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            
            # Add current element's index to the deque
            dq.append(i)
            
            # Store the maximum element from 
            # the first window possible
            if i >= (k - 1):
                ans.append(arr[dq[0]])
        
        # Return the stored result
        return ans

# Creating an instance of Solution class
sol = Solution()

# Array and window size
arr = [4, 0, -1, 3, 5, 3, 6, 8]
k = 3

# Function call to get the maximum sliding window
ans = sol.maxSlidingWindow(arr, k)

print("The maximum elements in the sliding window are:", ans)

Complexity Analysis:
Time Complexity: O(N) (where N is the size of given array)
The array is traversed once taking O(N) time.
In the worst-case, each element is pushed in and popped out from deque only once taking O(N) time.
Space Complexity: O(N-K) + O(K)
The deque will store K elements at maximum, taking O(K) time.
The result list stores N-K+1 maximums taking O(N-K) space.

'''
from collections import deque
class Solution:
    def maxSlidingWindow(self, arr, k):
        n = len(arr) 
        ans = []
        dq = deque()
        for i in range(n):
            if dq and dq[0] <= (i - k):
                dq.popleft()
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            dq.append(i)
            if i >= (k - 1):
                ans.append(arr[dq[0]])
        return ans
    