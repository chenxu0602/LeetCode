#
# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/
#
# algorithms
# Easy (47.45%)
# Likes:    583
# Dislikes: 47
# Total Accepted:    38.9K
# Total Submissions: 82.1K
# Testcase Example:  '[30,20,150,100,40]'
#
# In a list of songs, the i-th song has a duration of time[i] seconds. 
# 
# Return the number of pairs of songs for which their total duration in seconds
# is divisible by 60.  Formally, we want the number of indices i, j such that i
# < j with (time[i] + time[j]) % 60 == 0.
# 
# 
# 
# Example 1:
# 
# 
# Input: [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
# 
# 
# 
# Example 2:
# 
# 
# Input: [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible
# by 60.
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= time.length <= 60000
# 1 <= time[i] <= 500
# 
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # count = Counter()
        # res = 0
        # for t in time:
        #     res += count[-t % 60]
        #     count[t % 60] += 1
        # return res

        T = Counter([i % 60 for i in time])
        return sum([T[i] * T[60 - i] for i in range(1, 30)]) + (T[0] * (T[0] - 1) + T[30] * (T[30] - 1)) // 2
        
# @lc code=end

