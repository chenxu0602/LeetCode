#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (60.42%)
# Likes:    1492
# Dislikes: 41
# Total Accepted:    81.9K
# Total Submissions: 135.6K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# 
# Given a list of daily temperatures T, return a list such that, for each day
# in the input, tells you how many days you would have to wait until a warmer
# temperature.  If there is no future day for which this is possible, put 0
# instead.
# 
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76,
# 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
# 
# 
# Note:
# The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].
# 
#
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        """
        nxt = [float("inf")] * 102
        ans = [0] * len(T)
        for i in range(len(T)-1, -1, -1):
            warmer_index = min(nxt[t] for t in range(T[i]+1, 102))
            if warmer_index < float("inf"):
                ans[i] = warmer_index - i
            nxt[T[i]] = i
        return ans
        """

        """
        ans = [0] * len(T)
        stack = []
        for i in range(len(T)-1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans
        """

        res = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)
        return res



        

