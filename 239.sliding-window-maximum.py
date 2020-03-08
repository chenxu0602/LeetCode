#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        queue, r = deque([]), []

        for i, num in enumerate(nums):

            while queue and queue[0][1] <= i - k:
                queue.popleft()

            while queue and num > queue[-1][0]:
                queue.pop()

            queue.append([num, i])

            if i >= k - 1:
                r.append(queue[0][0])

        return r





