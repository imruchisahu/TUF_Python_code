'''
Given an array of nums of n integers. Every integer in the array appears twice except one integer. Find the number that appeared once in the array.


Examples:
Input : nums = [1, 2, 2, 4, 3, 1, 4]

Output : 3

Explanation : The integer 3 has appeared only once.

Input : nums = [5]

Output : 5

Explanation : The integer 5 has appeared only once.

Input : nums = [1, 3, 10, 3, 5, 1, 5]

Output:
10
Constraints:
1 <= n <= 105
-3*105 <= nums[i] <= 3*105

Brute:
Intuition:
The brute force way to solve this will be to utilize a frequency counting approach. By keeping track of the frequency of each element in the array, the element that appears only once can be easily identified.

Approach:
Use a hash map to store the frequency of each element in the array. The keys of the map are the elements of the array, and the values are their corresponding frequencies.
Traverse the entire array once, and for each element, update its frequency count in the map.
After populating the map with frequency counts, iterate over the map to find the element with a frequency of 1. This element is the unique integer that appears only once in the array.
Return the unique element found in the map. If no such element exists (though the problem guarantees that one does), return -1.

class Solution:
    # Function to get the single 
    # number in the given array
    def singleNumber(self, nums):
        
        # Map to store the elements 
        # and their frequencies
        mpp = {}
        
        # Iterate on the array
        for num in nums:
            if num in mpp:
                mpp[num] += 1  #Update the map
            else:
                mpp[num] = 1  #Update the map
        
        # Iterate on the map
        for key, value in mpp.items():
            # If frequency is 1
            if value == 1:
                # Return the element
                return key
        
        # Return -1, if there is no 
        # number having frequency 1
        return -1

# Example usage
nums = [1, 2, 2, 4, 3, 1, 4]

# Creating an instance of 
# Solution class
sol = Solution() 

# Function call to get the single 
# number in the given array
ans = sol.singleNumber(nums)

print("The single number in given array is:", ans)

Complexity Analysis:
Time Complexity: O(N) (where N is the size of the array) –
Traversing the array to update the Hash Map - O(N).
Traversing on the map - O(N) (in worst case).
Space Complexity: O(N) – Using a hashmap data structure and in the worst-case (when all elements in the array are unique), it will store N key-value pairs.

#Optimal:
Intuition:
The problem can be efficiently solved using the properties of the XOR bitwise operator. The key properties of XOR are:

a^a = 0 (XOR of any number with itself is 0).
a^0 = a (XOR of any number with 0 is the number itself).
XOR is both commutative and associative, meaning the order in which you apply XOR does not matter.

Using these properties, calculating XOR all the numbers in the array, the pairs of identical numbers will cancel each other out (because a ^ a = 0), and the result will be the number that appears only once.
Approach:
Start with a variable initialized to 0. This variable will be used to store the cumulative XOR of all numbers in the array.
Loop through each element in the array. For each element, update the cumulative XOR by applying the XOR operation between the current cumulative XOR value and the current array element.
After iterating through all the elements, the cumulative XOR will hold the value of the integer that appears only once in the array.

class Solution:
    # Function to get the single 
    # number in the given array 
    def singleNumber(self, nums):
        # Variable to store XOR
        # of all numbers in array
        XOR = 0
        
        # Iterate on the array to
        # find XOR of all elements
        for num in nums:
            XOR ^= num
        
        # XOR stores the required answer
        return XOR

if __name__ == "__main__":
    nums = [1, 2, 2, 4, 3, 1, 4]
    
    # Creating an instance of 
    # Solution class 
    sol = Solution()
    
    # Function call to get the single 
    # number in the given array 
    ans = sol.singleNumber(nums)
    
    print(f"The single number in given array is: {ans}")

Complexity Analysis:
Time Complexity: O(N) (where N is the size of array) – Traversing through the array once will result in O(N) TC.

Space Complexity: O(1) – Using constant space.

'''
class Solution:
    def singleNumber(self, nums):
        XOR = 0
        for num in nums:
            XOR ^= num
        return XOR
