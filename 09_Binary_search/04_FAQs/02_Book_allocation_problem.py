'''
Given an array nums of n integers, where nums[i] represents the number of pages in the i-th book, and an integer m representing the number of students, allocate all the books to the students so that each student gets at least one book, each book is allocated to only one student, and the allocation is contiguous.



Allocate the books to m students in such a way that the maximum number of pages assigned to a student is minimized. If the allocation of books is not possible, return -1.


Examples:
Input: nums = [12, 34, 67, 90], m=2

Output: 113

Explanation: The allocation of books will be 12, 34, 67 | 90. One student will get the first 3 books and the other will get the last one.

Input: nums = [25, 46, 28, 49, 24], m=4

Output: 71

Explanation: The allocation of books will be 25, 46 | 28 | 49 | 24.

Input: nums = [15, 17, 20], m=2

Output:
32
Constraints:
  1 <= n, m <= 104
  1 <= nums[i] <= 105

  
  #Linear Search
  Intuition: 
The extremely naive approach is to check all possible pages from max element of the array to sum of all the elements of the array. The minimum pages for which all the books can be allocated to M students will be our answer.

Approach: 
Working of findPages(nums, m):
Edge case: If the number of students given is greater than the total number books, then the allocation is impossible and return -1 as answer.
First, find the range of the search space, which will be [low, high], where low is the maximum element of the array and high is the sum of all elements of the array.
Now, iterate from low to high using a for loop, inside this loop call the countStudent() function to get the number of students to whom books can be allocated.
If the value returned from the helper function is less than or equal to the given limit(m) then return the current value of the iteration.
Finally, if no suitable answer is found then return low(max element of the array) as an answer.

Working of countStudents(nums, pages):
Start by getting the size of the array nums and store in in 'n'. Initialize students to 1, assuming at least one student is required and also initialize pagesStudent to 0, which will keep track of the total number of pages assigned to the current student.
Iterate through the array and check if adding current element to pagesStudent will keep the total pages assigned to the current student within the limit specified by pages. If true, add the current element to pagesStudent, indicating that the current student can handle these additional pages.
If adding the current element would exceed the limit pages, it indicates that a new student is needed to handle these pages. Increment the students counter to account for the new student. Reset pagesStudent to the current element, starting a new student with the current element's pages. Finally, return the 'student' variable.


class Solution:
    """Function to count the number of 
    students required given the maximum 
    pages each student can read"""
    def countStudents(self, nums, pages):
        # Size of array
        n = len(nums)
        
        students = 1
        pagesStudent = 0
        
        for i in range(n):
            if pagesStudent + nums[i] <= pages:
                # Add pages to current student
                pagesStudent += nums[i]
            else:
                # Add pages to next student
                students += 1
                pagesStudent = nums[i]
        
        return students
    
    """Function to allocate the book to ‘m’ 
    students such that the maximum number 
    of pages assigned to a student is minimum"""
    def findPages(self, nums, m):
        n = len(nums)
        
        # Book allocation impossible
        if m > n:
            return -1
        
        # Calculate the range for binary search
        low = max(nums)
        high = sum(nums)
        
        # Linear search for minimum maximum pages
        for pages in range(low, high + 1):
            if self.countStudents(nums, pages) <= m:
                return pages
        
        return low

if __name__ == "__main__":
    arr = [
    
    25, 46, 28, 49, 24]
    m = 4

    # Create an instance of the Solution class
    sol = Solution()

    ans = sol.findPages(arr, m)

    # Output the result
    print("The answer is:", ans)
Complexity Analysis: 
Time Complexity:O(N * (sum-max)), where N is size of the array, sum is the sum of all array elements, max is the maximum of all array elements.
As the loop runs from max to sum to check all possible numbers of pages. Inside the loop, the countStudents() function is being called for each number, and the loop inside this runs for N times.

Space Complexity: As no additional space is used, so the Space Complexity is O(1).

#Binary Search
Intuition: 
Here, the idea is to use binary search algorithm to optimize the brute-force solution which was using linear search algorithm. The answer space, represented as [max element, sum of all elements], is actually sorted so, binary search algorithm can be applied here. Based on certain conditions, the search space can be divided into halves in each iteration thus enhancing the overall time complexity.

Approach: 
Working of findPages(nums, m):
Edge case: If the number of students given is greater than the total number books, then the allocation is impossible and return -1 as answer.
Take two pointers, low and high. Initialize low to max(maximum element of the array) and high to sum(sum of all the elements of the array). The range from [low,high] will define the search space.
Now, initialize a while loop, which runs till low is less than or equal to high. Inside this loop calculate the 'mid' by using mid = (low+high) // 2 ( ‘//’ refers to integer division). The mid will be the defining the minimum possible maximum pages that can be allocated to any student.
Calculate students by using the countStudents function, which determines how many students are needed if each student can read up to 'mid' pages.
If the number of students required is greater than m, it means mid (the maximum pages assigned to a student) is too small. More pages are needed, so we need to increase the value of low (i.e., low = mid + 1). If the number of students required is less than or equal to m, it means mid might be a valid solution, so we try to minimize it by adjusting high = mid - 1.
After the binary search concludes (low > high), low will represent the minimum possible maximum pages that can be allocated to any student while ensuring m or fewer students are needed. Return low as the result.

Working of countStudents(nums, pages):
Start by getting the size of the array nums and store in in 'n'. Initialize students to 1, assuming at least one student is required and also initialize pagesStudent to 0, which will keep track of the total number of pages assigned to the current student.
Iterate through the array and check if adding current element to pagesStudent will keep the total pages assigned to the current student within the limit specified by pages. If true, add the current element to pagesStudent, indicating that the current student can handle these additional pages.
If adding the current element would exceed the limit pages, it indicates that a new student is needed to handle these pages. Increment the students counter to account for the new student. Reset pagesStudent to the current element, starting a new student with the current element's pages. Finally, return the 'student' variable.


class Solution:
    """Function to count the number of 
    students required given the maximum 
    pages each student can read"""
    def countStudents(self, nums, pages):
        # Size of array
        n = len(nums)
        
        students = 1
        pagesStudent = 0
        
        for i in range(n):
            if pagesStudent + nums[i] <= pages:
                # Add pages to current student
                pagesStudent += nums[i]
            else:
                # Add pages to next student
                students += 1
                pagesStudent = nums[i]
        
        return students
    
    """Function to allocate the book to ‘m’ 
    students such that the maximum number 
    of pages assigned to a student is minimum"""
    def findPages(self, nums, m):
        n = len(nums)
        
        # Book allocation impossible
        if m > n:
            return -1
        
        # Calculate the range for binary search
        low = max(nums)
        high = sum(nums)
        
        # Binary search for minimum maximum pages
        while low <= high:
            mid = (low + high) // 2
            students = self.countStudents(nums, mid)
            if students > m:
                low = mid + 1
            else:
                high = mid - 1
                
        return low

if __name__ == "__main__":
    arr = [25, 46, 28, 49, 24]
    m = 4

    # Create an instance of the Solution class
    sol = Solution()

    ans = sol.findPages(arr, m)

    # Output the result
    print("The answer is:", ans)
Complexity Analysis: 
Time Complexity:O(N * log(sum-max)), where N is size of the array, sum is the sum of all array elements, max is the maximum of all array elements.
As, binary search is being applied on [max, sum]. Inside the loop, we are calling the countStudents() function for the value of ‘mid’. Now, inside the countStudents() function, the loop runs for N times.

Space Complexity: As no additional space is used, so the Space Complexity is O(1).

'''
class Solution:
    def countStudents(self, nums, pages):
        n=len(nums)
        students = 1
        pagesStudent=0
        for i in range(n):
            if pagesStudent + nums[i] <= pages:
                pagesStudent += nums[i]
            else:
                students += 1
                pagesStudent = nums[i]
        return students
    
    def findPages(self, nums, m):
        n= len(nums)
        if m>n:
            return -1
        low = max(nums)
        high = sum (nums)
        while(low <= high):
            mid = (low + high) // 2
            students = self.countStudents(nums, mid)
            if students > m:
                low = mid + 1
            else:
                high = mid - 1
        return low
