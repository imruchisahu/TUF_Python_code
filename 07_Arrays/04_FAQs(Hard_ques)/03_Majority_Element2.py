'''Given an integer array nums of size n. Return all elements which appear more than n/3 times in the array. The output can be returned in any order.


Examples:
Input: nums = [1, 2, 1, 1, 3, 2]

Output: [1]

Explanation: Here, n / 3 = 6 / 3 = 2.

Therefore the elements appearing 3 or more times is : [1]

Input: nums = [1, 2, 1, 1, 3, 2, 2]

Output: [1, 2]

Explanation: Here, n / 3 = 7 / 3 = 2.

Therefore the elements appearing 3 or more times is : [1, 2]

Input: nums = [1, 2, 1, 1, 3, 2, 2, 3](Give the solution sorted in ascending order)

Output:
[1, 2]
Constraints:
n == nums.length.
1 <= n <= 105
-104 <= nums[i] <= 104

Similar Problems

Hint 1

Hint 2
Intuition 
The naive way is to use nested loops to count the occurrences of each of the elements and if the count is greater than one third of the size of array, include the element in the answer.

Can there be more than 2 majority elements ? Let's understand the scenario!
To understand why there can't be more than two majority elements (elements that appear more than n/3 times) in an array of size n, let's use a simple mathematical reasoning. A majority element in this context is defined as an element that appears more than n/3 times in the array. For an element to be a majority element, it must appear more than n/3 times. Let's assume there are more than two such majority elements. Let's denote these elements as A, B, and C.

Since each of these elements appears more than n/3 times, the combined frequency of these three elements would be: frequency of 𝐴 + frequency of 𝐵 + frequency of 𝐶 > 𝑛/3 + 𝑛/3 + 𝑛/3 = 𝑛

Now, the total number of occurrences of all elements in the array cannot exceed n, the size of the array. This means the combined frequency of any three elements each appearing more than n/3 times would exceed the total size of the array, which is a contradiction. Therefore, it's mathematically impossible for there to be more than two elements in the array that each appear more than n/3 times.

Approach 
Iterate in the array to select the elements of the array one by one. Now, for each unique element, run another loop and count its occurrence in the given array. If any element occurs more than the floor of (N/3), include it in our answer.
While traversing if any element that is already included in our answer is found, just skip it. When the answer array size is already 2, break out of loop, as there cant be more than 2 elements.
Return the answer array or -1 if no such element is found.


Complexity Analysis 
Time Complexity: O(N2), where N is the size of the array. As for every element of the array the inner loop runs for N times.

Space Complexity: O(1) the space used is so small that it can be considered constant.

from typing import List

class Solution:
    # Function to find majority elements in an array
    def majorityElementTwo(self, nums: List[int]) -> List[int]:
        
        # Size of the array
        n = len(nums)
        
        # List of answers
        result = []
        
        for i in range(n):
            """ Checking if nums[i] is not 
            already part of the answer """
            if len(result) == 0 or result[0] != nums[i]:
                
                cnt = 0
                
                for j in range(n):
                    # counting the frequency of nums[i]
                    if nums[j] == nums[i]:
                        cnt += 1
                
                # check if frequency is greater than n/3
                if cnt > (n // 3):
                    result.append(nums[i])
                
            # if result size is equal to 2 break out of loop
            if len(result) == 2:
                break
        
        # return the majority elements
        return result

if __name__ == "__main__":
    arr = [11, 33, 33, 11, 33, 11]
    
    # Create an instance of Solution class
    sol = Solution()
    
    ans = sol.majorityElementTwo(arr)
    
    # Print the majority elements found
    print("The majority elements are:", end=" ")
    for it in ans:
        print(it, end=" ")
    print()

'''
class Solution:
    def majorityElementTwo(self, nums):
        n=len(nums)
        result = []
        for i in range(n):
            if len(result) == 0 or result[0] != nums[i]:
                count=0
                for j in range(n):
                    if nums[j] == nums[i]:
                        count += 1
                if count > (n//3):
                    result.append(nums[i])
            if len(result) == 2:
                break
        return result
        
