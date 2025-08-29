'''A line of N kids is standing there. The rating values listed in the integer array ratings are assigned to each kid.



These kids are receiving candy, according to the following criteria:



There must be at least one candy for every child.


Kids whose scores are higher than their neighbours receive more candies than their neighbours.


Return the minimum number of candies needed to distribute among children.


Examples:
Input : ratings = [1, 0, 5]



Output : 5



Explanation : The distribution of candies will be 2 , 1 , 2 to first , second , third child respectively.

Input : ratings = [1, 2, 2]



Output : 4



Explanation : The distribution of candies will be 1 , 2 , 1 to first , second , third child respectively.

The third gets only 1 candy because it satisfy above two criteria.

Input : ratings = [1, 2, 1, 4, 5]

Output:
9
Constraints:
1 <= n <= 104
0 <= ratings[i] <= 105

#Brute Approach
Intuition
First, scan the children from left to right, giving more candies to those with higher ratings than the child before them. Then, scan from right to left, ensuring children with higher ratings than the children after them also get more candies. The total number of candies needed is the sum of the maximum number of candies assigned from both directions for each child.
Approach
Start by creating two lists, both the same length as the ratings list, and fill them with 1s. One list will track the minimum candies needed when considering the children to the left, and the other will do the same for the children to the right.
Move through the ratings from left to right, starting with the second child. For each child, compare their rating with the child immediately before them. If a child has a higher rating than the previous child, give them one more candy than the previous child.
Now, move through the ratings from right to left, starting with the second-to-last child. For each child, compare their rating with the child immediately after them. If a child has a higher rating than the next child, give them one more candy than the next child.
To find the total number of candies needed, look at each child and take the higher value between the two lists for each position. Sum these values to get the total number of candies required. This ensures each child gets the correct number of candies according to the rules.

class Solution:
    # To calculate number of candies
    def candy(self, ratings):
        # Get number of children
        n = len(ratings)
        # If no children, return 0
        if n == 0:
            return 0

        # Initialize lists to store candies
        # for each child from left and right
        left = [1] * n
        right = [1] * n

        # Left to right pass
        # Traverse the ratings from left to right
        # to adjust candies based on ratings
        for i in range(1, n):
            # If the current child's rating is
            # higher than the previous one
            if ratings[i] > ratings[i - 1]:
                # Give the current child one
                # more candy than the previous one
                left[i] = left[i - 1] + 1

        # Right to left pass
        # Traverse the ratings from right to left
        # to adjust candies based on ratings
        for i in range(n - 2, -1, -1):
            # If the current child's rating is
            # higher than the next one
            if ratings[i] > ratings[i + 1]:
                # Give the current child one
                # more candy than the next one
                right[i] = right[i + 1] + 1

        # Combine results
        # Calculate the total number of candies
        # needed by taking the maximum from
        # left and right for each child
        ans = 0
        for i in range(n):
            # Each child gets the maximum
            # candies from left and right
            ans += max(left[i], right[i])

        # Return total
        return ans

if __name__ == "__main__":
    ratings = [1, 0, 2]
    sol = Solution()
    result = sol.candy(ratings)
    print("Minimum candies required:", result)

Complexity Analysis
Time Complexity: O(3N) where N is the number of children. We make a left-to-right pass, a right-to-left pass and a last pass to combine the results.

Space Complexity: O(2N) where N is the number of children. We create two additional arrays left and right to keep track of the minimum number of candies when considering left and right neighbours.

#Better Approach
Intuition:
As, we need to consider both the left and right neighbours, what we can do is take a 'left' array and store the minimum number of candies for each child based on the ratings of left neighbours. Now for the candies based on the rating of right neighbour, we can take take a 'right' variable which will keep track of the candies that the right neighbour own. Thus in each iteration we will have number of candies of both the left and right neighbours, using both of them we can calculate 'cur' and add it to the answer.

Approach:
Start by creating a list, of the same length as the ratings list, and fill them with 1s. The list will track the minimum candies needed when considering the children to the left.
Move through the ratings from left to right, starting with the second child. For each child, compare their rating with the child immediately before them. If a child has a higher rating than the previous child, give them one more candy than the previous child.
Take two variables: 'cur' to show the number of candies of the current child and 'right' to keep track of the number of candies that the right neighbour own.
Now, move through the ratings from right to left, starting with the second-to-last child. For each child, compare their rating with the child immediately after them. If a child has a higher rating than the next child, give them one more candy than the next child.
To find the total number of candies needed, look at each child and take the higher value between the 'cur' and 'left' lists for each position. For the next iteration assign the 'cur' value to the 'right'.
Sum these values to get the total number of candies required. This ensures each child gets the correct number of candies according to the rules.

class Solution:
    # To calculate number of candies
    def candy(self, ratings):
        # Get number of children
        n = len(ratings)
        # If no children, return 0
        if n == 0:
            return 0

        """ Initialize vectors to store candies
        for each child from left and right"""
        left = [1] * n
        
        # Left to right pass
        for i in range(1, n):
            """ If the current child's rating
            is higher than the previous one"""
            if ratings[i] > ratings[i - 1]:
                """ Give the current child one 
                more candy than the previous one"""
                left[i] = left[i - 1] + 1
        
        cur = 1
        right = 1
        sum_candies = max(1, left[n - 1])
        
        # Right to left pass
        for i in range(n - 2, -1, -1):
            """ If the current child's rating
            is higher than the next one"""
            if ratings[i] > ratings[i + 1]:
                """ Give the current child one
                more candy than the next one"""
                cur = right + 1
            else:
                cur = 1
            right = cur
            sum_candies += max(left[i], cur)
        
        # Return total
        return sum_candies

if __name__ == "__main__":
    sol = Solution()
    ratings = [1, 0, 2]

    result = sol.candy(ratings)

    print(f"Minimum candies required: {result}")

Complexity Analysis
Time Complexity: O(2N) where N is the number of children. We make a left-to-right pass and in the next pass we are calculating the sum and the candies for left-to-right pass together.

Space Complexity: O(N) where N is the number of children. We create only one additional array 'left' to keep track of the minimum number of candies when considering left neighbours.

#Optimal
Intuition
Instead of iterating over the rating array three times, the Greedy Approach optimizes it by handling the ratings in a single pass. The trend of the ratings is tracked as the array is traversed: increasing trends result in more candies for higher ratings, and decreasing trends ensure proper distribution for lower ratings. By balancing these trends, children with higher ratings receive more candies, achieving optimal and minimal candy distribution.
Approach
Start by initializing the total number of candies to 1 and set the current slope to stable.
Begin iterating through the ratings array from the second child to the last.
If the current child's rating is equal to the previous one, give the current child one more candy than the previous child and move to the next child.
If the ratings are not equal, identify an increasing trend. Assign more candies to each child in this trend, incrementing as the ratings increase.
After the increasing trend, identify a decreasing trend. Assign more candies to each child in this trend, incrementing as the ratings decrease.
Compare the candy counts from the increasing and decreasing trends. If the decreasing trend exceeds the peak from the increasing trend, adjust the total number of candies to ensure children with higher ratings get more candies than their neighbors.
After processing all children, return the total number of candies distributed.

class Solution:
    # To calculate the number of candies
    def candy(self, ratings):
        # Size of the ratings array
        n = len(ratings)
        
        # Initialize index variable
        i = 1
        
        #Initialize the total number of candies, starting with one candy for the first child
        sum = 1
        
        # Loop the ratings array
        while i < n:
            
            #Check if the current child's rating is equal to the previous one
            if ratings[i] == ratings[i - 1]:
                
                #If so, give the current child one more candy than the previous one
                sum += 1
                
                #Move to the next child
                i += 1
                
                #Skip the rest of the loop and move to the next iteration
                continue
            
           #Initialize the candy count for increasing rating trend
            peak = 1
            
            # Loop through increasing ratings trend
            while i < n and ratings[i] > ratings[i - 1]:
                
            #Increment candy count for increasing trend
                peak += 1
                
                #Update the total number of candies
                sum += peak
                
                # Move to next
                i += 1
            
            #Initialize the candy count for decreasing rating trend
            down = 1
            
            # Loop through decreasing ratings trend
            while i < n and ratings[i] < ratings[i - 1]:
                
                #Update the total number of candies for decreasing trend
                sum += down
                
                # Move to next
                i += 1
                
            #Increment the candy count for decreasing trend
                down += 1
            
            #Check if the candy count for decreasing trend exceeds the peak
            if down > peak:
                #Adjust the total number of candies to satisfy the condition
                sum += (down - peak)
        
        # Return total candies
        return sum

if __name__ == "__main__":
    ratings = [0, 2, 4, 3, 2, 1, 1, 3, 4, 6, 4, 0, 0]
    print("Ratings of Children: ", ratings)
    sol = Solution()
    result = sol.candy(ratings)
    print("Minimum number of candies needed:", result)

Complexity Analysis
Time Complexity: O(N) where N is the number of children in the line. The algorithm makes a single pass through the rating array, processing each child a fixed number of times. Each child is evaluated once during the main loop, and at most once more during the increasing and decreasing sequences.

Space Complexity: O(1) as the algorithm uses no extra space.

'''
class Solution:
    def candy(self, ratings):
        n = len(ratings)
        i = 1
        sum = 1
        while i < n:
            if ratings[i] == ratings[i - 1]:
                sum += 1
                i += 1
                continue
            peak = 1
            while i < n and ratings[i] > ratings[i - 1]:
                peak += 1
                sum += peak
                i += 1
            down = 1
            while i < n and ratings[i] < ratings[i - 1]:
                sum += down
                i += 1
                down += 1
            if down > peak:
                sum += (down - peak)
        return sum