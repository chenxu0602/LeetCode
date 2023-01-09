#
# @lc app=leetcode id=1723 lang=python3
#
# [1723] Find Minimum Time to Finish All Jobs
#
# https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/description/
#
# algorithms
# Hard (35.80%)
# Likes:    106
# Dislikes: 5
# Total Accepted:    3.7K
# Total Submissions: 9.9K
# Testcase Example:  '[3,2,3]\n3'
#
# You are given an integer array jobs, where jobs[i] is the amount of time it
# takes to complete the i^th job.
# 
# There are k workers that you can assign jobs to. Each job should be assigned
# to exactly one worker. The working time of a worker is the sum of the time it
# takes to complete all jobs assigned to them. Your goal is to devise an
# optimal assignment such that the maximum working time of any worker is
# minimized.
# 
# Return the minimum possible maximum working time of any assignment. 
# 
# 
# Example 1:
# 
# 
# Input: jobs = [3,2,3], k = 3
# Output: 3
# Explanation: By assigning each person one job, the maximum time is 3.
# 
# 
# Example 2:
# 
# 
# Input: jobs = [1,2,4,7,8], k = 2
# Output: 11
# Explanation: Assign the jobs the following way:
# Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
# Worker 2: 4, 7 (working time = 4 + 7 = 11)
# The maximum working time is 11.
# 
# 
# Constraints:
# 
# 
# 1 <= k <= jobs.length <= 12
# 1 <= jobs[i] <= 10^7
# 
# 
#

# @lc code=start
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # DFS
        # we assign the most time consuming work first.
        # Assign a work to totally free worker only once.
        # Update the res and don't go forward if work load already >= result
        # n = len(jobs)
        # jobs.sort(reverse=True)
        # self.res = sum(jobs)
        # count = [0] * k

        # def dfs(i):
        #     if i == n:
        #         self.res = min(self.res, max(count))
        #         return

        #     for j in range(k):
        #         if count[j] + jobs[i] < self.res:
        #             count[j] += jobs[i]
        #             dfs(i + 1)
        #             count[j] -= jobs[i]

        #         if count[j] == 0:
        #             break

        #     return False

        # dfs(0)
        # return self.res


        # Binary Search
        n = len(jobs)
        jobs.sort(reverse=True)

        def dfs(i):
            if i == n:
                return True
            for j in range(k):
                if cap[j] >= jobs[i]:
                    cap[j] -= jobs[i]
                    if dfs(i + 1):
                        return True
                    cap[j] += jobs[i]

                if cap[j] == x:
                    break

            return False

        left, right = max(jobs), sum(jobs)
        while left < right:
            x = (left + right) // 2
            cap = [x] * k
            if dfs(0):
                right = x
            else:
                left = x + 1

        return left

        

        
# @lc code=end

