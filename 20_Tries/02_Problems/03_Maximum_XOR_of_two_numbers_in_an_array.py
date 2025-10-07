'''
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.


Examples:
Input : nums = [3, 9, 10, 5, 1]

Output : 15

Explanation :

The maximum XOR value is 10 XOR 5 => 15.

Input : nums = [26, 49, 30, 15, 69]

Output : 116

Explanation :

The maximum XOR value is 69 XOR 49 => 116.

Input : nums = [1, 2, 3, 4, 5, 6]

Output:

7

Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 231 - 1

Intuition
XOR, or exclusive OR, is a binary bitwise operation that outputs true (1) only when the input bits differ. If the input bits are the same, the result is 0. If they are different, the result is 1.
Here's the truth table for XOR:

Input1		Input2		Output	
0		0		0	
0		1		1	
1		0		1	
1		1		0	
The objective is to maximize the XOR result between two numbers. This is achieved by ensuring that for each bit position, the XOR result is maximized. Therefore, we aim to maximize the number of opposite bits between the numbers.
To achieve this, we use a Trie data structure. The Trie allows us to traverse each bit of the numbers in the array and maximize the XOR value by selecting the opposite bit when available, ensuring the highest possible XOR result.
Approach
Create a Trie Node Structure: This structure represents a node in the Trie. It contains an array to store links to child nodes (0 and 1) and provides methods to interact with these child nodes, such as checking if a node exists, retrieving it, and adding a new one.
Insert Bit Values into the Trie: Iterate through the given array and insert the bit values of each number into the Trie from left to right. For each number, if the current node does not have a child node for the current bit, create a new child node. Move to the corresponding child node for the current bit.
Initialize Maximum XOR Value: Start from the root node and set the maximum XOR value to 0.
Maximize XOR for Each Number: For each bit of the number, from left to right, check if the opposite bit exists in the Trie. If it does, update the maximum XOR value and move to the child node for the opposite bit. If the opposite bit does not exist, move to the child node for the current bit.
Return the Result: After processing all bits of all numbers, return the maximum XOR value obtained.

class Node:
    def __init__(self):
        self.links = [None] * 2

    # To check if a specific bit 
    # key is present in the child nodes
    def containsKey(self, bit):
        return self.links[bit] is not None

    # To get the child node 
    # corresponding to a specific bit
    def get(self, bit):
        return self.links[bit]

    # To set a child node at 
    # a specific index in the 
    # links array
    def put(self, bit, node):
        self.links[bit] = node


# Trie class
class Trie:
    def __init__(self):
        self.root = Node()

    # To insert number in Trie
    def insert(self, num):
        # Start from the root
        node = self.root
        # Iterate each bit
        for i in range(31, -1, -1):
            # Extract i-th bit
            bit = (num >> i) & 1
            # If the current node doesn't 
            # have a child node with the 
            # current bit
            if not node.containsKey(bit):
                node.put(bit, Node())
            node = node.get(bit)

    # Method to find the maximum XOR
    def getMax(self, num):
        # Start from root
        node = self.root
        # Initialize maximum XOR value
        maxNum = 0
        # Iterate each bit
        for i in range(31, -1, -1):
            # Extract the i-th bit
            bit = (num >> i) & 1
            #If the complement of the current bit exists in the Trie update the maximum 
            # XOR value with the current bit
            # move to the child node corresponding to 
            # the complement of the current bit
            # Else move to the child node 
            # corresponding to the current bit
            if node.containsKey(1 - bit):
                maxNum |= (1 << i)
                node = node.get(1 - bit)
            else:
                node = node.get(bit)
        # Return maximum XOR
        return maxNum


# Solution class
class Solution:
    def findMaximumXOR(self, nums):
        # Create Trie
        trie = Trie()
        # Insert number
        for num in nums:
            trie.insert(num)

        # Maximum XOR value
        maxi = 0

        # Iterate each number
        for num in nums:
            # Update the maximum XOR
            maxi = max(maxi, trie.getMax(num))

        # Return maximum XOR value
        return maxi


# Main function
if __name__ == "__main__":
    solution = Solution()

    # Test case
    nums = [3, 10, 5, 25, 2, 8]

    # Print the input array
    print("Input:", " ".join(map(str, nums)))

    # Find and print the maximum XOR value
    result = solution.findMaximumXOR(nums)
    print("Maximum XOR value:", result)

Complexity Analysis
Time Complexity: O(32N + 32M) where N is the length of the input array.
Insertion Phase (O(32N)): For each number in the input array, we need to insert its 32-bit binary representation into the Trie. Since there are N numbers, and each number has 32 bits, the time complexity for insertion is 32N.
Query Phase (O(32M)): For each number in the input array, we query the Trie to find the maximum XOR value. Again, for each of the M numbers, we need to traverse 32 bits. Hence, the time complexity for the querying phase is 32M.

Space Complexity: O(32N) where N is the length of the input array. This code has a linear space complexity with respect to the size of the input array and each number takes up space proportional to 32 which is the size in Binary Representation.

'''
class Node:
    def __init__(self):
        self.links = [None] * 2

    def containsKey(self, bit):
        return self.links[bit] is not None

    def get(self, bit):
        return self.links[bit]

    def put(self, bit, node):
        self.links[bit] = node
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if not node.containsKey(bit):
                node.put(bit, Node())
            node = node.get(bit)

    def getMax(self, num):
        node = self.root
        maxNum = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if node.containsKey(1 - bit):
                maxNum |= (1 << i)
                node = node.get(1 - bit)
            else:
                node = node.get(bit)
        return maxNum

class Solution:
    def findMaximumXOR(self, nums):
        trie = Trie()
        for num in nums:
            trie.insert(num)
        maxi = 0
        for num in nums:
            maxi = max(maxi, trie.getMax(num))
        return maxi
