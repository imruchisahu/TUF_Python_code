'''
Given a string nums representing a non-negative integer, and an integer k, find the smallest possible integer after removing k digits from num.


Examples:
Input: nums = "541892", k = 2

Output: "1892"

Explanation: Removing the two digits 5 and 4 yields the smallest number, 1892.

Input: nums = "1002991", k = 3

Output: "21"

Explanation: Remove the three digits 1(leading one), 9, and 9 to form the new number 21(Note that the output must not contain leading zeroes) which is the smallest.

Input: nums = "10", k = 2

Output:
"0"
Constraints:
  1 <= k <= nums.length <= 104
  nums consists of only digits.
  nums does not have any leading zeros except for the zero itself.
  
  Intuition:
To get the smallest possible integer, the smaller digits must be kept at the beginning. This can be achieved by getting rid of K larger digits using a simple greedy approach that works by processing each digit and keeping the smallest possible digit, aiming for the smallest resulting number. Prioritizing smaller digits for the leftmost positions ensures the resulting number is minimized.

To facilitate the greedy approach, a stack data structure can be used because:

LIFO (Last In, First Out): The stack allows access to the most recently added element, useful when comparing and potentially removing the last chosen element to eliminate a larger digit.
Order Preservation: The stack maintains the relative order of elements, crucial when the sequence of digits must be preserved.
Approach:
Use a stack to keep track of the digits of the resulting number. Iterate through each digit of the input string.
Remove the previous digits from the stack if they are larger than the current digit and the removal count (k) allows. This step ensures that the remaining digits form the smallest possible number.
If there are still digits left to be removed after the iteration, continue removing the digits from the end of the stack.
Collect the remaining digits from the stack and form the resulting number by reversing the digits.
Edge Cases:
When K is equal to the size of the string:
In such cases, all the digits will be removed from the given numbers, thus "0" can be returned.

When the resulting number contains leading zeroes:
In such cases, the leading zeroes must be removed before returning the resultant number.

When there are still removals left:
Consider the example: nums = "1234" amd k = 2
Here, there will be no removals performed, however, two removals can be performed. Thus, to utilize all the given removals, the last digits of the number can be removed before returning the result.


class Solution:
    # Function to find the smallest possible 
    # integer after removing k digits
    def removeKdigits(self, nums: str, k: int) -> str:
        
        st = [] # Stack
        
        # Traverse on the given string
        for digit in nums:
            
            # Pop last digits (when possible)
            # if a smaller digit is found
            while st and k > 0 and st[-1] > digit:
                st.pop() # Pop the last digit
                k -= 1 # Decrement K by 1
            
            # Push the current digit
            st.append(digit)
        
        # If more digits can be removed
        while st and k > 0:
            st.pop() # Pop the last added digits
            k -= 1 # Decrement K by 1
        
        # Handling edge case
        if not st:
            return "0"
        
        # To store the result
        res = ""
        
        # Adding digits in stack to result
        while st:
            res += st.pop()
        
        # Trimming the zeroes at the back
        res = res.rstrip('0')
        
        # Reverse to get the actual number
        res = res[::-1]
        
        # Edge case
        if not res:
            return "0"
        
        # Return the stored result
        return res

if __name__ == "__main__":
    nums = "541892"
    k = 2
    
    # Creating an instance of 
    # Solution class
    sol = Solution()
    
    # Function call to find the smallest 
    # possible integer after removing k digits
    ans = sol.removeKdigits(nums, k)
    
    print("The smallest possible integer after removing k digits is:", ans)

    
Complexity Analysis:
Time Complexity: O(N) (where N is the length of the given number)
Traversing the given string takes O(N) time.
Each element is pushed onto and popped from the stack at most once in worst-case taking o(N) time.
Removing the remaining digits (if k > 0) takes O(k) time which can go upto O(N) in worst-case.
Forming the result, trimming the zeros and reversing the digits takes O(N) time.
Space Complexity: O(N)

The stack space can be O(N) in the worst-case.
The space required to store the result is O(N) in worst-case.


'''