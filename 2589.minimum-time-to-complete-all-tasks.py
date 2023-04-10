#
# @lc app=leetcode id=2589 lang=python3
#
# [2589] Minimum Time to Complete All Tasks
#

# @lc code=start
import heapq

class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:

        # O(nlogn)

        # 1. Each task has a latest start time.
        # 2. If there are several tasks being executed at the same time (i.e., their intervals overlap), the latest start time of all running tasks will be pushed back by a certain amount of time w.
        # 3. Sort the tasks by their start times in ascending order. Use a min-heap to maintain the running tasks that have the smallest latest start time.
        # 4. Add each task one by one. For the current task T (with the left endpoint ts) and the task T' in the task pool with the smallest latest start time (with the latest start time t's), if t'e + offset - 1 < ts - 1, it means that task T can start running first for time w without overlapping with task T. Here, w is equal to min(t'e, ts-1) - (t's + offset - 1), where offset is the time that the current task pool has already been running.
        # 5. Add w to ans, and add w to offset. If this condition is not satisfied, it means that the current task can be added to the task pool and started in parallel with the other tasks in the pool.
        # 6. When added to the task pool, the latest start time of task T can be set to te - p + 1 - offset, where p is the time it takes to complete task T.

        tasks.append([10**9+1, 10**9+1, 1])
        res, queue = 0, []

        for s, e, d in sorted(tasks):
            while queue and queue[0][0] + res < s:
                if queue[0][0] + res >= queue[0][1]:
                    heapq.heappop(queue)
                else:
                    res += min(queue[0][1], s) - (queue[0][0] + res)

            heapq.heappush(queue, [e - d + 1 - res, e + 1])

        return res

        
# @lc code=end

