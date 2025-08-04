'''Given an array of n elements. The task is to return the count of the number of odd numbers in the array.


Examples:
Input: n=5, array = [1,2,3,4,5]



Output: 3



Explanation: The three odd elements are (1,3,5).

Input: n=6, array = [1,2,1,1,5,1]



Output: 5



Explanation: The five odd elements are one 5 and four 1's.

Input: n=5, array = [1,3,5,7,9]

Output:
5
Constraints:
1 <= n <= 105
1 <= arr[i] <= 104
Intuition:
A simple way to solve this problem is by traversing the whole array and checking each element if it is odd. The count of the odd numbers found will be the answer.

Approach:
Initialize a counter to zero to keep track of odd numbers. Initialize a for loop to iterate through each element in the array.
For each element, check if it is odd by checking it divisibility by 2 and increment counter if odd.
After iterating through all elements, the counter will contain the total count of odd numbers.
Dry Run:
Image 1
Image 2
Image 3
Image 4
Image 5
Image 6
Image 7

1/7


Solution:

Complexity Analysis:
Time Complexity : O(N)
Each element in the array has to be inspected once to determine if it's odd, resulting in a linear time complexity where N is the number of elements in the array.

Space Complexity : O(1)
The space used is constant, as we only use a single counter regardless of the size of the input array.

class Solution:
    # Function to count the odd numbers in an array 
    def countOdd(self, arr, n):
        count = 0
        # Iterate through the array
        for num in arr:
        # Check for odd values and increment
            if num % 2 != 0:
                count += 1
        return count
        
# Main method
if __name__ == "__main__":
    # Creating an instance of Solution class
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    
    # Function call to count the odd numbers in an array 
    count = sol.countOdd(arr, n)
    print("Count of odd numbers:", count)



'''
class Solution:
    def countOdd(self, arr, n):
        # Your code goes here
        count=0
        for n in arr:
            if n%2 != 0:
                count += 1
        return count