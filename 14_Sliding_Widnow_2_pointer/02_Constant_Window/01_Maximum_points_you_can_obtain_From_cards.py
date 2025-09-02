'''
Given N cards arranged in a row, each card has an associated score denoted by the cardScore array. Choose exactly k cards. In each step, a card can be chosen either from the beginning or the end of the row. The score is the sum of the scores of the chosen cards.



Return the maximum score that can be obtained.


Examples:
Input : cardScore = [1, 2, 3, 4, 5, 6] , k = 3

Output : 15

Explanation : Choosing the rightmost cards will maximize your total score. So optimal cards chosen are the rightmost three cards 4 , 5 , 6.

Th score is 4 + 5 + 6 => 15.

Input : cardScore = [5, 4, 1, 8, 7, 1, 3 ] , k = 3

Output : 12

Explanation : In first step we will choose card from beginning with score of 5.

In second step we will choose the card from beginning again with score of 4.

In third step we will choose the card from end with score of 3.

The total score is 5 + 4 + 3 => 12

Input : cardScore = [9, 10, 1, 2, 3, 5] , k = 5

Output:
29
Constraints:
1 <= cardScore.length <= 105
1 <= cardScore[i] <=104
1 <= k <= cardScore.length

Intuition:
Here, the idea is to use a window of size k, first calculate the sum of k elements from the beginning. Then, maintain the window size of k by subtracting the beginning elements from the calulated sum one by one and adding the elements from the end of the array. Everytime while doing so we will keep track of the maximum sum encountered so far. This process will continue till we have subtracted all k elements from the beginning of the array from the sum, thus ensuring that we have taken every possible case in consideration.

Approach:
First declare three variables, lSum, rSum, maxSum and initialize them to 0.
Then iterate in the array from 0 till k-1 and calculate the sum of elements and store it in lSum, update maxSum to lSum.

class Solution:
    """ Function to calculate the maximum
     score after picking k cards"""
    def maxScore(self, cardScore, k):
        lSum = 0
        rSum = 0
        maxSum = 0

        # Calculate the initial sum of the first k cards
        for i in range(k):
            lSum += cardScore[i]
            
            """ Initialize maxSum with the
             sum of the first k cards"""
            maxSum = lSum

        # Initialize rightIndex to iterate array from last
        rightIndex = len(cardScore) - 1
        
        for i in range(k - 1, -1, -1):
            
            # Remove the score of the ith card from left sum
            lSum -= cardScore[i]
            
            # Add the score of the card
            # from the right to the right sum
            rSum += cardScore[rightIndex]
            
            # Move to the next card from the right
            rightIndex -= 1

            # Update maxSum with the maximum sum found so far
            maxSum = max(maxSum, lSum + rSum)

        # Return the maximum score found
        return maxSum

nums = [1, 2, 3, 4, 5, 6]

# Create an instance of the Solution class
sol = Solution()

result = sol.maxScore(nums, 3)

# Output the maximum score
print("The maximum score is:")
print(result)

Complexity Analysis: 
Time Complexity:O(2*k). Where k is the size of the window.

Space Complexity: As no additional space is used, so the Space Complexity is O(1)

'''

class Solution:
    def maxScore(self, cardScore, k):
        lSum =0
        rSum=0
        maxSum =0
        for i in range(k):
            lSum += cardScore[i]
            maxSum = lSum

        rightIndex = len(cardScore) - 1
        for i in range(k - 1, -1, -1):
            lSum -= cardScore[i]
            rSum += cardScore[rightIndex]
            rightIndex -= 1
            maxSum = max(maxSum, lSum + rSum)
        return maxSum