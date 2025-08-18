'''Given two integers start and goal. 
Flip the minimum number of bits of start integer to convert it into goal integer.

A bits flip in the number val is to choose any bit in binary representation of val and flipping it from either 0 to 1 or 1 to 0.

Examples:
Input : start = 10 , goal = 7

Output : 3

Explanation : The binary representation of 10 is "1010".

The binary representation of 7 is "111".

If we flip the underlined bits in binary representation of 10 then we will obtain our goal.

Input : start = 3 , goal = 4

Output : 3

Explanation : The binary representation of 3 is "011".

The binary representation of 4 is "100".

So if we flip all the three bits of 3 then we will reach our goal number.

Input : start = 1 , goal = 7

Output:
2
Constraints:
1 <= start , end <= 109
Intuition
Since the problem is asking about number of bits that needs to be changed, it could be easily find out if it is known that which are bits are different.
And for this purpose, XOR operation will come in hand which will only set the bit if both corresponding bits are different.

Approach
Use the XOR operation between the two numbers. This will produce a new number where each bit is set to 1 if the corresponding bits in the original numbers were different.
Count the number of 1s in this new number because each 1 represents a bit that needs to be flipped to convert one number to the other.
Run a loop 32 times (to check all 32 bits in the number) and shift the bits of this new number one by one. Check if the least significant bit (the rightmost bit) is 1. If it is, increment the count.
Repeat this shifting process until all bits in the number have been checked. The count will give the minimum number of bit flips required to convert the first number into the second.

class Solution:
    # Function to get the minimum 
    # bit flips to convert number
    def minBitsFlip(self, start, goal):
        
        # Variable to store bits that 
        # are different in both numbers
        num = start ^ goal
        
        # Variable to count 
        # number of set bits
        count = 0

        for i in range(32):
            # Update count if the 
            # rightmost bit is set
            count += (num & 1)
            
            # Shift the number every
            # time by 1 place
            num = num >> 1
        
        return count

Complexity Analysis:
Time Complexity: O(1)

The XOR operation between two integers is performed in constant time, O(1).
The for loop iterates over a fixed number of bits (32 bits for a standard integer), which is as good as O(1).
Space Complexity: O(1) – Using a couple of variables i.e., constant space.

'''
class Solution:
    def minBitsFlip(self, start, goal):
        num = start ^ goal
        count = 0
        for i in range(32):
            count += (num & 1)
            num = num >> 1
        return count
