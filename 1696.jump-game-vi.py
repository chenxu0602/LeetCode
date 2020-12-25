#
# @lc app=leetcode id=1696 lang=python3
#
# [1696] Jump Game VI
#
# https://leetcode.com/problems/jump-game-vi/description/
#
# algorithms
# Medium (59.44%)
# Likes:    203
# Dislikes: 13
# Total Accepted:    8.5K
# Total Submissions: 14.3K
# Testcase Example:  '[1,-1,-2,4,-7,3]\n2'
#
# You are given a 0-indexed integer array nums and an integer k.
# 
# You are initially standing at index 0. In one move, you can jump at most k
# steps forward without going outside the boundaries of the array. That is, you
# can jump from index i to any index in the range [i + 1, min(n - 1, i + k)]
# inclusive.
# 
# You want to reach the last index of the array (index n - 1). Your score is
# the sum of all nums[j] for each index j you visited in the array.
# 
# Return the maximum score you can get.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,-1,-2,4,-7,3], k = 2
# Output: 7
# Explanation: You can choose your jumps forming the subsequence [1,-1,4,3]
# (underlined above). The sum is 7.
# 
# 
# Example 2:
# 
# 
# Input: nums = [10,-5,-2,4,0,3], k = 3
# Output: 17
# Explanation: You can choose your jumps forming the subsequence [10,4,3]
# (underlined above). The sum is 17.
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length, k <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start
from collections import deque
import heapq

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # Dynamic Programming + Deque
        # score[i] represents the max score starting at nums[0] and ending at nums[i].
        # O(N)
        # n = len(nums)
        # score = [0] * n
        # score[0] = nums[0]
        # dq = deque([0])
        # for i in range(1, n):
        #     # pop the old index
        #     while dq and dq[0] < i - k:
        #         dq.popleft()
        #     score[i] = score[dq[0]] + nums[i]
        #     # pop the smaller value
        #     while dq and score[i] >= score[dq[-1]]:
        #         dq.pop()
        #     dq.append(i)
        # return score[-1]

        n = len(nums)
        score = nums[0]
        dq = deque()
        dq.append((0, score))
        for i in range(1, n):
            while dq and dq[0][0] < i - k:
                dq.popleft()
            score = dq[0][1] + nums[i]
            while dq and score >= dq[-1][1]:
                dq.pop()
            dq.append((i, score))
        return score


        # Dynamic Programming + Priority Queue
        # Time  complexity: O(NlogN)
        # Space complexity: O(N)
        # n = len(nums)
        # score = [0] * n
        # score[0] = nums[0]
        # priority_queue = []
        # heapq.heappush(priority_queue, (-nums[0], 0))
        # for i in range(1, n):
        #     while priority_queue[0][1] < i - k:
        #         heapq.heappop(priority_queue)
        #     score[i] = nums[i] + score[priority_queue[0][1]]
        #     heapq.heappush(priority_queue, (-score[i], i))
        # return score[-1]

        
# @lc code=end

