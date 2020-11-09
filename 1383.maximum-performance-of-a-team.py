#
# @lc app=leetcode id=1383 lang=python3
#
# [1383] Maximum Performance of a Team
#
# https://leetcode.com/problems/maximum-performance-of-a-team/description/
#
# algorithms
# Hard (33.61%)
# Likes:    296
# Dislikes: 23
# Total Accepted:    8.9K
# Total Submissions: 26.4K
# Testcase Example:  '6\n[2,10,3,1,5,8]\n[5,4,3,9,7,2]\n2'
#
# There are n engineers numbered from 1 to n and two arrays: speed and
# efficiency, where speed[i] and efficiency[i] represent the speed and
# efficiency for the i-th engineer respectively. Return the maximum performance
# of a team composed of at most k engineers, since the answer can be a huge
# number, return this modulo 10^9 + 7.
# 
# The performance of a team is the sum of their engineers' speeds multiplied by
# the minimum efficiency among their engineers. 
# 
# 
# Example 1:
# 
# 
# Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
# Output: 60
# Explanation: 
# We have the maximum performance of the team by selecting engineer 2 (with
# speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7).
# That is, performance = (10 + 5) * min(4, 7) = 60.
# 
# 
# Example 2:
# 
# 
# Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
# Output: 68
# Explanation:
# This is the same example as the first but k = 3. We can select engineer 1,
# engineer 2 and engineer 5 to get the maximum performance of the team. That
# is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.
# 
# 
# Example 3:
# 
# 
# Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
# Output: 72
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^5
# speed.length == n
# efficiency.length == n
# 1 <= speed[i] <= 10^5
# 1 <= efficiency[i] <= 10^8
# 1 <= k <= n
# 
#

# @lc code=start
import heapq, bisect

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        # h = []
        # res = sum_ = 0
        # for eff, spd in sorted(zip(efficiency, speed), reverse=True):
        #     bisect.insort(h, -spd)
        #     sum_ += spd
        #     if len(h) > k:
        #         sum_ += h.pop()
        #     res = max(res, sum_ * eff)
        # return res % (10**9 + 7)


        h = []
        res = sum_ = 0
        for eff, spd in sorted(zip(efficiency, speed), reverse=True):
            heapq.heappush(h, spd)
            sum_ += spd
            if len(h) > k:
                sum_ -= heapq.heappop(h)
            res = max(res, sum_ * eff)
        return res % (10**9 + 7)
        
# @lc code=end

