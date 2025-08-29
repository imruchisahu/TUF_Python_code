'''Given an 2D array Jobs of size Nx3, where Jobs[i][0] represents JobID , Jobs[i][1] represents Deadline , Jobs[i][2] represents Profit associated with that job. Each Job takes 1 unit of time to complete and only one job can be scheduled at a time.



The profit associated with a job is earned only if it is completed by its deadline. Find the number of jobs and maximum profit.


Examples:
Input : Jobs = [ [1, 4, 20] , [2, 1, 10] , [3, 1, 40] , [4, 1, 30] ]

Output : 2 60

Explanation : Job with JobID 3 can be performed at time t=1 giving a profit of 40.

Job with JobID 1 can be performed at time t=2 giving a profit of 20.

No more jobs can be scheduled, So total Profit = 40 + 20 => 60.

Total number of jobs completed are two, JobID 1, JobID 3.

So answer is 2 60.

Input : Jobs = [ [1, 2, 100] , [2, 1, 19] , [3, 2, 27] , [4, 1, 25] , [5, 1, 15] ]

Output : 2 127

Explanation : Job with JobID 1 can be performed at time time t=1 giving a profit of 100.

Job with JobID 3 can be performed at time t=2 giving a profit of 27.

No more jobs can be scheduled, So total Profit = 100 + 27 => 127.

Total number of jobs completed are two, JobID 1, JobID 3.

So answer is 2 127.

Input : Jobs = [ [1, 1, 100] , [2, 2, 200] , [3, 3, 300] , [4, 4, 400] ]

Output:
4 1000
Constraints:
1 <= N <= 104
1 <= Deadline <= N
1 <= Profit <= 500
Intuition
The strategy to maximize profit involves prioritizing jobs that offer higher profits. To achieve this, the jobs should be sorted in descending order of profit. For example, a job with a deadline of 4 can be completed anytime between day 1 and day 4. However, performing the job on its last possible day is more beneficial. This leaves earlier days available for other jobs, optimizing the schedule and allowing more jobs to be completed within their deadlines.
Approach
Sort the jobs in descending order of profit.
Determine the maximum deadline and create an array of that size. Initially, set each array index to -1 to indicate no jobs have been scheduled.
For each job, check if it can be performed on its latest possible day.
If possible, mark that index with the job id and add the profit to the total profit.
If not possible, check the previous days until an empty slot is found.
class Solution:
    # Function to calculate maximum profit
    def JobScheduling(self, Jobs):
        # Sort jobs based on profit in descending order
        Jobs.sort(key=lambda x: -x[2])

        # Total number of jobs
        n = len(Jobs)

        # Get the maximum deadline to complete the jobs
        maxDeadline = -1
        for it in Jobs:
            maxDeadline = max(maxDeadline, it[1])

        # Initialize a hash table to store selected jobs
        hash = [-1] * (maxDeadline + 1)

        # Initialize count
        cnt = 0

        # Initialize the total profit earned
        totalProfit = 0

        # Iterate over each job
        for i in range(n):

            #Iterate over each deadline slot starting from the job's deadline 
            for j in range(Jobs[i][1] - 1, -1, -1):

                # If the current deadline slot is available 
                if hash[j] == -1:
                    cnt += 1 # Count of selected jobs
                    hash[j] = Jobs[i][0] # Mark the job as selected
                    totalProfit += Jobs[i][2] # Update the total profit

                    # Move to the next job
                    break

        # Return the list
        return [cnt, totalProfit]

if __name__ == "__main__":
    jobs = [[1, 4, 20], [2, 1, 10], [3, 1, 40], [4, 1, 30]]

    solution = Solution()
    result = solution.JobScheduling(jobs)

    # Output the result
    print("Number of Jobs:", result[0])
    print("Maximum Profit:", result[1])


Complexity Analysis
Time Complexity: O(N logN + N2) where N is the number of jobs. First, the jobs are sorted based on profit in descending order, resulting in O(N logN) complexity. Then, the algorithm iterates over the jobs to select them. The outer loop runs once for each job (N iterations), and the inner loop iterates up to the job’s deadline, which can be at most N in the worst case, giving a complexity of O(N2).
Space Complexity: O(N) where N is the number of jobs. An array of size N is used to keep track of occupied slots taking O(N) space.


'''
class Solution:
    def JobScheduling(self, Jobs):
        Jobs.sort(key=lambda x: -x[2])
        n = len(Jobs)
        maxDeadline = -1
        for it in Jobs:
            maxDeadline = max(maxDeadline, it[1])
        hash = [-1] * (maxDeadline + 1)
        cnt = 0
        totalProfit = 0
        for i in range(n):
            for j in range(Jobs[i][1] - 1, -1, -1):
                if hash[j] == -1:
                    cnt += 1 
                    hash[j] = Jobs[i][0] 
                    totalProfit += Jobs[i][2] 
                    break
        return [cnt, totalProfit]