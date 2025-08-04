'''Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.


Examples:
Input: n=5, arr = [1,2,3,4,5]



Output: [5,4,3,2,1]



Explanation: The reverse of the array [1,2,3,4,5] is [5,4,3,2,1]

Input: n=6, arr = [1,2,1,1,5,1]



Output: [1,5,1,1,2,1]



Explanation: The reverse of the array [1,2,1,1,5,1] is [1,5,1,1,2,1].

Input: n=3, arr = [1,2,1]

Output:
[1,2,1]
Constraints:
1 <= n <= 104

1 <= arr[i] <= 105

Intuition:
To reverse an array, the objective is to reorder the elements such that the last element becomes the first and the second last becomes the second, and so forth. The straightforward approach involves creating a new array of the same size and populating it by iterating through the input array from end to start, thereby storing elements in reverse order.

Approach:
Declare a new array having the same size as the input array.
Iterate through the input array from the end to the beginning and for each element in the input array, store it in the corresponding position in the new array.
After the loop ends, the new array will contain the reversed elements.
Copy the elements back to the original array to get the reversed array.
Dry Run
Image 1
Image 2
Image 3
Image 4
Image 5
Image 6
Image 7

1/7



Complexity Analysis:
Time Complexity: O(N), A single-pass of the array with N elements is being done to reverse the array.

Space Complexity: O(N), for the extra array of the same size used.

class Solution:
    # Function to reverse array using an auxiliary array
    def reverse(self, arr, n):
        ans = [0] * n
        
        # Fill new array with elements of 
        # original array in reverse order
        for i in range(n - 1, -1, -1):
            ans[n - i - 1] = arr[i]
        
        # Copy the elements back to the original array
        for i in range(n):
            arr[i] = ans[i]
        
        # Return
        return
 
# Function to print array
def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()
 
if __name__ == "__main__":
    n = 5
    arr = [5, 4, 3, 2, 1]
    
    # Creating instance of Solution class
    solution = Solution()
    print("Original array: ", end="")
    printArray(arr, n)
    
    # Function call to reverse the array 
    solution.reverse(arr, n) 
    print("Reversed array: ", end="")
    printArray(arr, n)



'''
class Solution:
    def reverse(self, arr, n):
        left = 0
        right = n - 1
        
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr
    

