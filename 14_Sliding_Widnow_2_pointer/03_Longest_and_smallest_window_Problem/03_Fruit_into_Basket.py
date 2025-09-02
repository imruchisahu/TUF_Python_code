'''

There is only one row of fruit trees on the farm, oriented left to right. An integer array called fruits represents the trees, where fruits[i] denotes the kind of fruit produced by the ith tree.



The goal is to gather as much fruit as possible, adhering to the owner's stringent rules:



1) There are two baskets available, and each basket can only contain one kind of fruit. The quantity of fruit each basket can contain is unlimited.

2) Start at any tree, but as you proceed to the right, select exactly one fruit from each tree, including the starting tree. One of the baskets must hold the harvested fruits.

3) Once reaching a tree with fruit that cannot fit into any basket, stop.



Return the maximum number of fruits that can be picked.


Examples:
Input : fruits = [1, 2, 1]

Output : 3

Explanation : We will start from first tree.

The first tree produces the fruit of kind '1' and we will put that in the first basket.

The second tree produces the fruit of kind '2' and we will put that in the second basket.

The third tree produces the fruit of kind '1' and we have first basket that is already holding fruit of kind '1'. So we will put it in first basket.

Hence we were able to collect total of 3 fruits.

Input : fruits = [1, 2, 3, 2, 2]

Output : 4

Explanation : we will start from second tree.

The first basket contains fruits from second , fourth and fifth.

The second basket will contain fruit from third tree.

Hence we collected total of 4 fruits.

Input : fruits = [1, 2, 3, 4, 5]

Output:
1
2
3
4

Submit
Constraints:
1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length


#BRute
# Intuition: 
The idea here is to generate all possible substrings of the given array using two loops and while doing so, check if the number of different fruits is within the allowed limit in the current substring, using a set data structure. If the number of different fruits exceed limit, then no need to consider that substring, else calculate the length of the current substring and update the maximum length of substring.

Approach: 
Start by initializing variables n to store the length of the input array fruits, and maxLen to track the maximum length of substrings with at most 2 different types of fruits.
Iterate the array for each index from 0 to sizeOfArray-1 to consider each index as the starting point of a substring.
For each starting point, initialize an empty unordered_set named set to keep track of the types of fruits in the current substring and start another loop from starting point of the substring till sizeOfArray-1. Add each fruit to the set.
After adding each fruit, check the size of the set. The set will only contain fruits that appear in the current substring.
If the size of set is less than or equal to 2, it means the current substring has at most 2 different types of fruits. Calculate the length of this substring and update maxLen. Else, break out of the loop.
After the outer and inner loops complete execution, return maxLen as an answer.
class Solution:
    """ Function to find the maximum
    fruits the basket can have """
    def totalFruits(self, fruits):
        
        # Length of the input array
        n = len(fruits)
        
        """ Variable to store the 
        maximum length of substring"""
        maxLen = 0
        
        """ Iterate through all possible 
        starting points of the substring"""
        for i in range(n):
            
            """ Use set to track
            different types of fruits"""
            s = set()
            
            for j in range(i, n):
                
                # Add fruit type to the set
                s.add(fruits[j])
                
                """ Check if the number of different
                fruits is within the allowed limit"""
                if len(s) <= 2:
                    
                    """ Calculate the length 
                    of current substring"""
                    length = j - i + 1
  
                    maxLen = max(maxLen, length)
                else:
                    break
        
        # Return the maximum length
        return maxLen

if __name__ == "__main__":
    input = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    
    # Create an instance of Solution class
    sol = Solution()
    
    length = sol.totalFruits(input)
    
    # Print the result
    print("Maximum fruits in the basket is:", length)

Complexity Analysis: 
Time Complexity:O(N2), where N is the size of the array. As for every element of the array the inner loop runs for N times. Ignore the contribution of set data structure in the time complexity as it takes O(log3), which can be considered as constant.

Space Complexity: O(3) , as at most the set data structure is holding 3 elements.

#Better
Intuition: 
The idea here is to use sliding window approach with a hashMap data structure to keep track of the different types of the fruits found so far. Expand the window by moving the right pointer and if the the number of different types of fruits exceeds 2 then shrink the window until is becomes less than or equal to 2, thus eliminating fruits from the basket because of which the limit has exceed. This ensures to consider every possible case in optimised way.

Approach: 
First, initialize few variables as: l , ras 0, maxLen variable to store the maximum length of substrings with at most 2 different types of fruits, mpp hashMap to track the count of each fruit type in the current sliding window defined by indices l (left) and r (right).
Iterate through the array using the r pointer and add the current fruit to the HashMap mpp with its count incremented by one. Check if the number of different fruits exceeds 2. If it does, shrink the window from the left (l++) until the number of different fruits is at most 2. Else, Calculate the length of the current valid substring and update maximum length of substring.
Move the r pointer to the right (r++) to expand the window and repeat the process. Finally, return the maximum length of the substring.
class Solution:
    """ Function to find the maximum
    fruits the basket can have """
    def totalFruits(self, fruits):
        
        # Length of the input array
        n = len(fruits)
        
        """ Variable to store the 
        maximum length of substring """
        maxLen = 0  
        
        """ Dictionary to track the count of each
        fruit type in the current window """
        mpp = {}
        
        # Pointers for the sliding window approach
        l, r = 0, 0
        
        while r < n:
            mpp[fruits[r]] = mpp.get(fruits[r], 0) + 1
            
            """ If number of different fruits exceeds
             2 shrink the window from the left """
            if len(mpp) > 2:
                while len(mpp) > 2:
                    mpp[fruits[l]] -= 1
                    if mpp[fruits[l]] == 0:
                        del mpp[fruits[l]]
                    l += 1
            
            """ If number of different fruits 
            is at most 2, update maxLen """
            if len(mpp) <= 2:
                maxLen = max(maxLen, r - l + 1)
            
            r += 1
        
        # Return the maximum fruit
        return maxLen

# Test the solution
if __name__ == "__main__":
    input = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    
    # Create an instance of Solution class
    sol = Solution()
    
    length = sol.totalFruits(input)
    
    # Print the result
    print(f"Maximum fruits the basket can have: {length}")

Complexity Analysis: 
Time Complexity:O(2N), where N is the size of the array. As the other while loop runs for N time and the inner while loop runs for N time in total throghto the program. Ignore the contribution of map data structure in the time complexity as size of the map is extremely small.

Space Complexity: O(3) , as at most the map data structure is holding 3 elements.

#Optimal
Intuition: 
The idea here is to employ the sliding window approach efficiently by avoiding the additional O(N) time complexity incurred when shifting the window entirely in the better solution, to ensure that the different types of fruits does not exceed 2. Instead of moving the left pointer (l) to eliminate the extra fruits completely, shift the window by one position at a time. This method ensures that the problem can be solved in O(N) time complexity only.

Approach: 
First, initialize few variables as: l and r pointers as 0 for the sliding window approach, maxLen variable to store the maximum length of substrings with at most 2 different types of fruits, mpp an unordered_map to track the count of each fruit type in the current sliding window.
Iterate through the array using the r pointer and add the current fruit to the map with its count incremented by one.
Check if the number of different fruits exceeds 2.If so, it means there are more than 2 different types of fruits in the current window. Therefore, shrink the window from the left (l++). Adjust the count in mpp accordingly. If the count of fruits[l] becomes 0, remove it from map. Else, calculate the length of the current valid substring.
Update maxLen, move the r pointer to the right (r++) to expand the window and repeat the process. Finally, return the maxLen as an ans.
class Solution:
    """ Function to find the maximum
    fruits the basket can have """
    def totalFruits(self, fruits):
        
        # Length of the input array
        n = len(fruits)
        
        """ Variable to store the 
        maximum length of substring """
        maxLen = 0  
        
        """ Dictionary to track the count of each
        fruit type in the current window """
        mpp = {}
        
        # Pointers for the sliding window approach
        l, r = 0, 0
        
        while r < n:
            mpp[fruits[r]] = mpp.get(fruits[r], 0) + 1
            
            """ If number of different fruits exceeds
             2 shrink the window from the left """
            if len(mpp) > 2:
                mpp[fruits[l]] -= 1
                if mpp[fruits[l]] == 0:
                    del mpp[fruits[l]]
                l += 1
            
            """ If number of different fruits 
            is at most 2, update maxLen """
            if len(mpp) <= 2:
                maxLen = max(maxLen, r - l + 1)
            
            r += 1
        
        # Return the maximum fruit
        return maxLen

if __name__ == "__main__":
    input = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    
    # Create an instance of Solution class
    sol = Solution()
    
    len = sol.totalFruits(input)
    
    # Print the result
    print(f"Maximum fruits the basket can have: {len}")

    
Complexity Analysis: 
Time Complexity:O(N), where N is the size of the array. As the while loop runs for N time only. Ignore the contribution of map data structure in the time complexity as size of the map is extremely small.

Space Complexity: O(N) , as the map may store up to N unique fruit types in the worst case.


'''
class Solution:
    def totalFruits(self, fruits):
        n = len(fruits)
        maxLen = 0  
        mpp = {}
        l, r = 0, 0
        
        while r < n:
            mpp[fruits[r]] = mpp.get(fruits[r], 0) + 1
            if len(mpp) > 2:
                mpp[fruits[l]] -= 1
                if mpp[fruits[l]] == 0:
                    del mpp[fruits[l]]
                l += 1
            if len(mpp) <= 2:
                maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen