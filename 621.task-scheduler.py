#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#
# https://leetcode.com/problems/task-scheduler/description/
#
# algorithms
# Medium (47.47%)
# Likes:    2375
# Dislikes: 485
# Total Accepted:    130.4K
# Total Submissions: 274.5K
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# Given a char array representing tasks CPU need to do. It contains capital
# letters A to Z where different letters represent different tasks. Tasks could
# be done without original order. Each task could be done in one interval. For
# each interval, CPU could finish one task or just be idle.
# 
# However, there is a non-negative cooling interval n that means between two
# same tasks, there must be at least n intervals that CPU are doing different
# tasks or just be idle.
# 
# You need to return the least number of intervals the CPU will take to finish
# all the given tasks.
# 
# 
# 
# Example:
# 
# 
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
# 
# 
# 
# 
# Note:
# 
# 
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].
# 
# 
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Greedy
        # Time  complexity: O(N_total), where N_total is the number of tasks to execute.
        # Space complexity: O(1).
        # frequencies = [0] * 26
        # for t in tasks:
        #     frequencies[ord(t) - ord('A')] += 1

        # frequencies.sort()

        # # max frequency
        # f_max = frequencies.pop()
        # idle_time = (f_max - 1) * n

        # while frequencies and idle_time > 0:
        #     idle_time -= min(f_max - 1, frequencies.pop())
        # idle_time = max(0, idle_time)

        # return idle_time + len(tasks)


        # Math
        # Time  complexity: O(N_total), where N_total is the number of tasks to execute.
        # Space complexity: O(1).
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1

        # max frequency
        f_max = max(frequencies)
        # count the most frequent tasks
        n_max = frequencies.count(f_max)

        return max(len(tasks), (f_max - 1) * (n + 1) + n_max)

        
# @lc code=end

