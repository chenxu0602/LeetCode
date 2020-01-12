#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#
# https://leetcode.com/problems/task-scheduler/description/
#
# algorithms
# Medium (45.85%)
# Likes:    1794
# Dislikes: 313
# Total Accepted:    95.2K
# Total Submissions: 207.2K
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
from collections import defaultdict, Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        """
        if n == 0:
            return len(tasks)

        hs = defaultdict(int)
        for task in tasks:
            hs[task] += 1

        count = 0
        cycle = n + 1

        heap = []

        for k, i in hs.items():
            if i > 0:
                heapq.heappush(heap, (-i))

        while heap:
            worktime = 0
            tmp = []
            for i in range(cycle):
                if heap:
                    tmp.append(heapq.heappop(heap))
                    worktime += 1
            for cnt in tmp:
                cnt *= -1
                cnt -= 1
                if cnt > 0:
                    heapq.heappush(heap, -cnt)

            count += cycle if len(heap) > 0 else worktime

        return count
        """

        """
        hs = [0] * 26
        for c in tasks:
            hs[ord(c) - ord('A')] += 1
        hs.sort()

        max_val = hs[25] - 1
        idle_slots = max_val * n
        for i in range(24, -1, -1):
            idle_slots -= min(hs[i], max_val)

        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)
        """

        task_counts = Counter(tasks).values()
        M = max(task_counts)
        Mct = list(task_counts).count(M)
        return max(len(tasks), (M-1) * (n+1) + Mct)

        
        

