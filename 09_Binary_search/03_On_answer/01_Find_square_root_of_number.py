'''
Given a positive integer n. Find and return its square root. If n is not a perfect square, then return the floor value of sqrt(n).


Examples:
Input: n = 36

Output: 6

Explanation: 6 is the square root of 36.

Input: n = 28

Output: 5

Explanation: The square root of 28 is approximately 5.292. So, the floor value will be 5.

Input: n=50

Output:
7
Constraints:
 0 <= n <= 231 - 1

 #Linear Search

 Intuition: 
The idea here is to search for the floor of the square root of the given number linearly. For each number from 1 to the given number, find its square and check if it is smaller than the given number, if it is, store the current integer as potential root, else break out of the loop as the further calculations will only provide larger square roots.

Approach: 
Start with ans initialized to 0, which will eventually hold the floor of the square root of n.
Iterate using a for loop, ranging from 1 to n. For each integer compute 'val' as the square of the current integer.
Check if 'val' is less than or equal to n. If true update 'ans' to the current value of the integer, because the current integer is a candidate for the square root.
If val exceeds n, break out of the loop since further values of the next integer will only yield larger squares.
Once the loop completes, ans contains the largest integer such that ans * ans is less than or equal to n, providing the floor of the square root of n. Finally return ans.

Cpp
Java
Python
Javascript
C#
Go


class Solution:
    """ Function to compute the floor of
        square root of a given integer """
    def floorSqrt(self, n: int) -> int:
        ans = 0
        
        # Linear search in the answer space
        for i in range(1, n + 1):
            val = i * i
            
            # Check if val is less than or equal to n
            if val <= n:
                # Update ans to current value of i
                ans = i
            else:
                break
        
        # Return the computed floor of square root
        return ans

if __name__ == "__main__":
    n = 28
    
    # Create an object of the Solution class
    sol = Solution()
    
    ans = sol.floorSqrt(n)
    
    # Print the result
    print(f"The floor of square root of {n} is: {ans}")
Complexity Analysis: 
Time Complexity:O(N1/2), where N is the given number. Since we are using linear search, and the loop iterates up to sqrt(N) before breaking out.

Space Complexity: As no additional space is used, so the Space Complexity is O(1).

#Binary Search
Intuition: 
Binary Search algorithm can be used to optimize the brute force solution. While applying the binary search algorithm, compare the square of mid with the given number, if the square is less than or equal to the given number, store the mid as it can be a potential root and eliminate the left half of the search space, else eliminate the right half.

Approach: 
Start with initializing low to 1 and high initialized to n, where n is the given number, defining the search range for ans. Also, initialize ans to 0 to store the answer.
Use a while loop, where it continues to search until low exceeds high. Calculate 'mid' as the midpoint between low and high. Compute val as mid * mid, the square of the midpoint.
Check if 'val' is less than or equal to n, if true, it means mid could be a potential candidate for the square root. Store the mid in 'ans' and move the search to the right part by updating low to mid + 1. If false, move the search to the left part by updating high to mid - 1 because mid is too high and mid * mid exceeds n
Once the while loop exits, 'ans' holds the largest integer ans such that ans * ans does not exceed n.


Cpp
Java
Python
Javascript
C#
Go


class Solution:
    """ Function to compute the floor of
        square root of a given integer """
    def floorSqrt(self, n: int) -> int:
        low, high = 1, n
        
        # Binary search on the answer space
        while low <= high:
            mid = (low + high) // 2
            val = mid * mid
            
            # Check if val is less than or equal to n
            if val <= n:
                # Move to the right part
                low = mid + 1
            else:
                # Move to the left part
                high = mid - 1
        
        # Return the floor of square root
        return high

if __name__ == "__main__":
    n = 28
    
    # Create an object of the Solution class
    sol = Solution()
    
    ans = sol.floorSqrt(n)
    
    # Print the result
    print(f"The floor of square root of {n} is: {ans}")
Complexity Analysis: 
Time Complexity:O(logN), where N is the given number. We are basically using the Binary Search algorithm.

Space Complexity: As no additional space is used, so the Space Complexity is O(1).



'''
class Solution:
    def floorSqrt(self, n: int) -> int:
        low, high = 0, n
        while low <= high:
            mid = (low + high) // 2
            val = mid * mid
            if val <= n:
                low= mid + 1
            else:
                high = mid - 1
        return high
