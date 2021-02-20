#
# @lc app=leetcode id=1751 lang=python3
#
# [1751] Maximum Number of Events That Can Be Attended II
#
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/description/
#
# algorithms
# Hard (47.31%)
# Likes:    145
# Dislikes: 3
# Total Accepted:    3.8K
# Total Submissions: 8K
# Testcase Example:  '[[1,2,4],[3,4,3],[2,3,1]]\n2'
#
# You are given an array of events where events[i] = [startDayi, endDayi,
# valuei]. The i^th event starts at startDayi and ends at endDayi, and if you
# attend this event, you will receive a value of valuei. You are also given an
# integer k which represents the maximum number of events you can attend.
# 
# You can only attend one event at a time. If you choose to attend an event,
# you must attend the entire event. Note that the end day is inclusive: that
# is, you cannot attend two events where one of them starts and the other ends
# on the same day.
# 
# Return the maximum sum of values that you can receive by attending events.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
# Output: 7
# Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value
# of 4 + 3 = 7.
# 
# Example 2:
# 
# 
# 
# 
# Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
# Output: 10
# Explanation: Choose event 2 for a total value of 10.
# Notice that you cannot attend any other event as they overlap, and that you
# do not have to attend k events.
# 
# Example 3:
# 
# 
# 
# 
# Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
# Output: 9
# Explanation: Although the events do not overlap, you can only attend 3
# events. Pick the highest valued three.
# 
# 
# Constraints:
# 
# 
# 1 <= k <= events.length
# 1 <= k * events.length <= 10^6
# 1 <= startDayi <= endDayi <= 10^9
# 1 <= valuei <= 10^6
# 
# 
#

# @lc code=start
import bisect

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        dp, dp2 = [[0, 0]], [[0, 0]]
        for _ in range(k):
            for s, e, v in events:
                i = bisect.bisect(dp, [s]) - 1
                if dp[i][1] + v > dp2[-1][1]:
                    dp2.append([e, dp[i][1] + v])

            dp, dp2 = dp2, [[0, 0]]
        return dp[-1][-1]

        
# @lc code=end

