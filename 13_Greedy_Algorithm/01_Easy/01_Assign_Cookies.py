'''
Consider a scenario where a teacher wants to distribute cookies to students, with each student receiving at most one cookie.



Given two arrays, Student and Cookie, the ith value in the Student array describes the minimum size of cookie that the ith student can be assigned. The jth value in the Cookie array represents the size of the jth cookie. If Cookie[j] >= Student[i], the jth cookie can be assigned to the ith student. Maximize the number of students assigned with cookies and output the maximum number.


Examples:
Input : Student = [1, 2, 3] , Cookie = [1, 1]

Output :1

Explanation : You have 3 students and 2 cookies.

The minimum size of cookies required for students are 1 , 2 ,3.

You have 2 cookies both of size 1, So you can assign the cookie only to student having minimum cookie size 1.

So your answer is 1.

Input : Student = [1, 2] , Cookie = [1, 2, 3]

Output : 2

Explanation : You have 2 students and 3 cookies.

The minimum size of cookies required for students are 1 , 2.

You have 3 cookies and their sizes are big enough to assign cookies to all students.

So your answer is 2.

Input : Student = [4, 5, 1] , Cookie = [6, 4, 2]

Output:
3
Constraints:
1 <= Student.length <= 3*104
0 <= Cookie.length <= 3*104
1 <= Student[i] , Cookie[j] <= 231 - 1

Intuition
The goal is to maximize the number of students who can be satisfied with the given cookies. By sorting both the students' greed factors and the cookie sizes, we can efficiently assign the smallest available cookie that satisfies each student's greed. We iterate through the arrays, assigning cookies to students until we either run out of students or cookies, ensuring the maximum number of satisfied students.
Approach
Sort both the students' greed and cookie sizes to efficiently pair the smallest cookies with the least greedy children.
Use two pointers to iterate through the arrays, representing the smallest available cookie and the least greedy child.
For each pair, check if the current cookie can satisfy the current child's greed.
If a child's greed is satisfied, move to the next child; always move to the next cookie.
The final count of satisfied children indicates the maximum number of children who can be content with the given cookies.

class Solution:
    def findMaximumCookieStudents(self, Student, Cookie):
        n = len(Student)
        m = len(Cookie)
        # Pointers
        l, r = 0, 0
        # Sorting of lists
        Student.sort()
        Cookie.sort()

        # Traverse through both lists
        while l < n and r < m:
            """If the current cookie can satisfy 
            the current student, move to the 
            next student"""
            if Cookie[r] >= Student[l]:
                l += 1
            # Move to next cookie
            r += 1
        # Return number of students
        return l

# Example input
Student = [1, 2]
Cookie = [1, 2, 3]

# Create a Solution object
solution = Solution()

# Call the findMaximumCookieStudents function
result = solution.findMaximumCookieStudents(Student, Cookie)

# Output the result
print("Number of students satisfied:", result)


Complexity Analysis
Time Complexity: O(N logN + M logM + M) where N is the length of the student array, and M is the length of the cookies array. Sorting the student array takes O(N logN) time, and sorting the cookies array takes O(M logM) time.
After sorting, we iterate through the arrays up to M times, where M is the number of cookies. Each student and each cookie is considered at most once, making the time complexity of this iteration linear, which is O(M). Therefore, the total time complexity is O(N logN + M logM + M).

Space Complexity: O(1) no extra space used.

'''
class Solution:
    def findMaximumCookieStudents(self, Student, Cookie):
        n = len(Student)
        m = len(Cookie)
        l, r = 0, 0
        Student.sort()
        Cookie.sort()
        while l < n and r < m:
            if Cookie[r] >= Student[l]:
                l += 1
            r += 1
        return l