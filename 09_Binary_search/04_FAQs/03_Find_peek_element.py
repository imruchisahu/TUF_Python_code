'''
Given an array arr of integers. A peak element is defined as an element greater than both of its neighbors.

Formally, if arr[i] is the peak element, arr[i - 1] < arr[i] and arr[i + 1] < arr[i].



Find the index(0-based) of a peak element in the array. If there are multiple peak numbers, return the index of any peak number.



Note:

As there can be many peak values, 1 is given as output if the returned index is a peak number, otherwise 0.

Examples:
Input : arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]

Output: 7

Explanation: In this example, there is only 1 peak that is at index 7.

Input : arr = [1, 2, 1, 3, 5, 6, 4]

Output: 1

Explanation: In this example, there are 2 peak numbers at indices 1 and 5. We can consider any of them.

Input : arr = [-2, -1, 3, 4, 5]

Output:
4
Constraints:
 1 <= arr.length <= 1000
 -231 <= arr[i] <= 231 - 1
 arr[i] != arr[i + 1] for all valid i.
For arr[0], its left element can be considered as -∞
For arr[n-1], its right element can be considered as -∞

#Linear Search
Intuition: 
A simple approach involves iterating through the array and checking the adjacent elements of the current element, if the adjacent elements are smaller than the current element then the current element will be the peak element.

Approach: 
Edge cases:
If n == 1(n is size of the array): If the size of the array is one, then the only element present will the peak element. So, return its index.
If the current index is 0: While checking for 0th index, it will have only one adjacent element, so just check for the element at 1st index, as -1 index will be invalid index.
If the current index is (n-1): The last index will also have only one adjacent element as the nth index will be invalid(for 0 based indexing). So just check (n-2)th index.
Start traversing the array and for every index, check its adjacent index.
If an element is greater than its adjacent elements, return the index of that element.
If no such element is found, return -1 as an answer.


class Solution:
    # Function to find peak element in the array
    def findPeakElement(self, arr):
        # Size of array
        n = len(arr)
        
        """ Iterate through the array
            to find the peak element """
        for i in range(n):
            
            # Check if arr[i] is a peak
            if (i == 0 or arr[i - 1] < arr[i]) and (i == n - 1 or arr[i] > arr[i + 1]):
                
                # Return the index of peak element
                return i
        
        """ Return -1 if no peak element
            found (dummy return) """
        return -1

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
    
    # Create an instance of the Solution class
    sol = Solution()
    
    ans = sol.findPeakElement(arr)
    
    # Output the result
    print("The peak is at index:", ans)

# Call the main function
if __name__ == "__main__":
    main()
Complexity Analysis: 
Time Complexity:O( N), where N is size of the array. As the for loop is running for N times only.

Space Complexity: As no additional space is used, so the Space Complexity is O(1).



#Binary Search
Intuition: 
Here, the idea is to use binary search algorithm to optimize the brute-force solution where linear serch was being used. For each element (mid), we check if it is greater than its previous and next elements. If so, mid is identified as a peak element. Alternatively, if mid is smaller than its previous element, a peak must exist on the left side, so the right half is eliminated. Similarly, if mid is less than the next element, a peak must exist on the right side, so the left half is eliminated. This approach trims down the search space in each iteration, thereby enhancing the time complexity.


How to identify the halves:
The left half of the peak element has an increasing order and the right half of the peak element has a decreasing order. So if the current element is greater than the previous element, it means we are in left half and if current element is greater than the next element, it means we are in the right half of the search space.

Approach: 
Edge cases:
If n == 1(n is size of the array): If the size of the array is one, then the only element present will the peak element. So, return its index.
If the current index is 0: While checking for 0th index, it will have only one adjacent element, so just check for the element at 1st index, as -1 index will be invalid index.
If the current index is (n-1): The last index will also have only one adjacent element as the nth index will be invalid(for 0 based indexing). So just check (n-2)th index.
Initialize two pointers: low to 1 and high to n-2(n is the size of the array), as the 0th and (n-1)th index has already been dealt with in the edge cases. This will describe our search space.
Intialize a while loop which will run till low is less than or equal to high. Now, inside a loop, calculate the value of ‘mid’ using the following formula: mid = (low+high) // 2 ( ‘//’ refers to integer division)
Check if element at [mid] is the peak element, if yes, return the value of 'mid' as the peak element is found at index 'mid'.
If element at [mid] greater than element at [mid-1], this means we are in the left half and eliminate it as the peak element appears on the right.
Otherwise, we are in the right half and eliminate it as the peak element appears on the left. This case also handles the case for the index ‘mid’ being a common point of a decreasing and increasing sequence. It will consider the left peak and eliminate the right peak.
At last if no peak element is found return -1 as an answer.


class Solution:
    # Function to find peak element in the array
    def findPeakElement(self, arr):
        # Size of array
        n = len(arr)
        
        # Edge cases:
        if n == 1:
            return 0
        if arr[0] > arr[1]:
            return 0
        if arr[n - 1] > arr[n - 2]:
            return n - 1

        low = 1
        high = n - 2
        while low <= high:
            mid = (low + high) // 2  

            # If arr[mid] is the peak
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid

            # If we are in the left part of array
            if arr[mid] < arr[mid - 1]:
                high = mid - 1
            else:
                low = mid + 1
        
        # Return -1 if no peak element found
        return -1

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
    
    # Create an instance of the Solution class
    sol = Solution()
    
    ans = sol.findPeakElement(arr)
    
    # Output the result
    print("The peak is at index:", ans)

# Call the main function
if __name__ == "__main__":
    main()
Complexity Analysis: 
Time Complexity:O(logN), N is size of the given array. As binary search is being used to find the minimum.

Space Complexity: As no additional space is used, so the Space Complexity is O(1).
'''
class Solution:
    def findPeakElement(self, arr):
        n=len(arr)
        for i in range(n):
            if (i==0 or arr[i-1] < arr[i]) and (i== n-1 or arr[i] > arr[i+1]):
                return i
        return -1