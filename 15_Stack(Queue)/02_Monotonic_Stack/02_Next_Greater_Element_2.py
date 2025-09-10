'''
Given a circular integer array arr, return the next greater element for every element in arr.



The next greater element for an element x is the first element greater than x that we come across while traversing the array in a clockwise manner.



If it doesn't exist, return -1 for that element element.


Examples:
Input: arr = [3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]

Output: [10, -1, 6, 6, 2, 6, 7, 7, 9, 9, 10]

Explanation: For the first element in arr i.e, 3, the greater element which comes next to it while traversing and is closest to it is 10. Hence,10 is present on index 0 in the resultant array. Now for the second element i.e, 10, there is no greater number and hence -1 is it’s next greater element (NGE). Similarly, we got the NGEs for all other elements present in arr.  

Input: arr = [5, 7, 1, 7, 6, 0]

Output: [7, -1, 7, -1, 7, 5]

Explanation: For the first element in arr i.e, 5, the greater element which comes next to it while traversing and is closest to it is 7. Now for the second element i.e, 7, there is no greater number and hence -1 is it’s next greater element (NGE). Similarly, we got the NGEs for all other elements present in arr.

Input: arr = [1, 2, 3, 4, 5]

Output:
[2, 3, 4, 5, 5]
[5, 5, 5, 5, -1]
[2, 3, 4, 5, 2]
[2, 3, 4, 5, -1]

Submit
Constraints:
  1 ≤ n≤ 105
  0 ≤ arr[i] ≤ 109


#BRute
Intuition:
The only difference between this problem and the earlier problem is that the array is circular in nature in this problem.
Handling circular arrays:
One way is to double the array by pushing all the elements of array at the back in order. But this will cost an extra space for only storing elements, making it an unpreferrable method.

The preferred way to handle circular array is to use the modulus operator that will help in traversing the array in a circular manner. This will double the array hypothetically saving the extra space.


Now, the brute force way to solve this question will be to use a loop to pick up an element of the array, and then find its next greater element using a nested loop (that will traverse the array in a circular manner) to check all the elements. In case there is no larger element found, the next greater element will be set to -1.
Approach:
Initialize an answer array to store the next greater elements for the given array with all elements initially set to -1.
Traverse the array using a for loop to select the current element for which next greater element must be found.
Use a nested for loop to traverse the array (in a circular fashion, using modulus operator) to find the next greater element. If found, store the answer in the array and break from the inner loop.
Once the outer for loop ends, the answer array storing the result can be returned.

class Solution:

    # Function to find the next greater element
    # for each element in the circular array
    def nextGreaterElements(self, arr):
       
        n = len(arr) # size of array
       
        # To store the next greater elements
        ans = [-1] * n
        
        for i in range(n):
            
            # Get the current element
            currEle = arr[i]
           
            # Nested loop to get the 
            # next greater element
            for j in range(1, n):
               
                # Getting the hypothetical index
                ind = (j + i) % n
               
                # If the next greater element is found
                if arr[ind] > currEle:
                   
                    # Store the next greater element
                    ans[i] = arr[ind]
                   
                    # Break from the loop
                    break
       
        # Return the answer
        return ans

if __name__ == "__main__":
    n = 6
    arr = [5, 7, 1, 7, 6, 0]
   
    # Creating an instance of 
    # Solution class
    sol = Solution()
   
    # Function call to find the next greater element
    # for each element in the circular array
    ans = sol.nextGreaterElements(arr)
   
    print("The next greater elements are: ", end="")
    for i in range(n):
        print(ans[i], end=" ")

Complexity Analysis:
Time Complexity: O(N2) (where N is the size of given array)
Using two nested for loops to find the next greater elements.

Space Complexity: O(N) The space required to store the answer is O(N).

#Optimal
Intuition:
Since the better way to solve this problem is already discussed in the Next greater element problem which is by using a stack. The only thing left to handle in this problem is circular nature of array.

Handling circular arrays:
One way is to double the array by pushing all the elements of array at the back in order. But this will cost an extra space for only storing elements, making it an unpreferrable method.

The preferred way to handle circular array is to use the modulus operator that will help in traversing the array in a circular manner. This will double the array hypothetically saving the extra space.

Since, we have to start the traversal from the back of the hypothetically doubled array, we must perform the stack operations for all elements. But the next greater element must be stored only for the second half of elements skipping the first half (as they are hypothetical elements).
Approach:
Initialize an answer array to store the next greater elements for the given array. Declare a stack data structure.
Start traversing the hypothetically doubled array from back using the modulus operator. For the current element, pop the elements from stack till the top is less than or equal to the current element.
For the first half of the elements, discard the greatest element if found. For the second half of the elements, if a greater element is found, store it in the answer array, otherwise store -1. Push the current element on top of stack (for both halves).
Once the traversal on array is complete, the answer array stores the result.

class Solution:
    
    # Function to find the next greater 
    # element for each element in the array
    def nextGreaterElements(self, arr):
        
        n = len(arr)  # size of array
        
        # To store the next greater elements
        ans = [-1] * n
        
        # Stack to get elements in LIFO fashion
        st = []
        
        # Start traversing from the back
        for i in range(2 * n - 1, -1, -1):
            
            # Get the actual index
            ind = i % n
            
            # Get the current element
            currEle = arr[ind]
            
            # Pop the elements in the stack until 
            # the stack is not empty and the top 
            # element is not the greater element
            while st and st[-1] <= currEle:
                st.pop()
            
            # Store the answer for the second half
            if i < n:
                
                # If the greater element is not 
                # found, stack will be empty
                if st:
                    ans[i] = st[-1]
            
            # Push the current element in the stack 
            # maintaining the decreasing order
            st.append(currEle)
        
        # Return the result
        return ans

# Driver Code
if __name__ == "__main__":
    arr = [5, 7, 1, 7, 6, 0]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to find the next greater 
    # element for each element in the array
    ans = sol.nextGreaterElements(arr)
    
    print("The next greater elements are:", ans)

Complexity Analysis:
Time Complexity: O(N) (where N is the size of the array)
Traversing on the array takes O(N) time and traversing the stack will take overall O(N) time as all the elements are pushed in the stack once.

Space Complexity: O(N)
The answer array takes O(N) space and the space used by stack will be O(N) in the worst case.


'''
class Solution:
    def nextGreaterElements(self, arr):
        n=len(arr)
        ans=[-1] * n
        st = []
        for i in range(2*n-1, -1, -1):
            ind = i%n
            currEle = arr[ind]
            while st and st[-1] <= currEle:
                st.pop()
            if i < n:
                if st:
                    ans[i] = st[-1]
            st.append(currEle)
        return ans
    