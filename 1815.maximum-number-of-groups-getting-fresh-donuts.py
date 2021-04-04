#
# @lc app=leetcode id=1815 lang=python3
#
# [1815] Maximum Number of Groups Getting Fresh Donuts
#
# https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/description/
#
# algorithms
# Hard (16.72%)
# Likes:    26
# Dislikes: 6
# Total Accepted:    384
# Total Submissions: 2.2K
# Testcase Example:  '3\n[1,2,3,4,5,6]'
#
# There is a donuts shop that bakes donuts in batches of batchSize. They have a
# rule where they must serve all of the donuts of a batch before serving any
# donuts of the next batch. You are given an integer batchSize and an integer
# array groups, where groups[i] denotes that there is a group of groups[i]
# customers that will visit the shop. Each customer will get exactly one
# donut.
# 
# When a group visits the shop, all customers of the group must be served
# before serving any of the following groups. A group will be happy if they all
# get fresh donuts. That is, the first customer of the group does not receive a
# donut that was left over from the previous group.
# 
# You can freely rearrange the ordering of the groups. Return the maximum
# possible number of happy groups after rearranging the groups.
# 
# 
# Example 1:
# 
# 
# Input: batchSize = 3, groups = [1,2,3,4,5,6]
# Output: 4
# Explanation: You can arrange the groups as [6,2,4,5,1,3]. Then the 1^st,
# 2^nd, 4^th, and 6^th groups will be happy.
# 
# 
# Example 2:
# 
# 
# Input: batchSize = 4, groups = [1,3,2,5,2,2,1,6]
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= batchSize <= 9
# 1 <= groups.length <= 30
# 1 <= groups[i] <= 10^9
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        ans = sum(g % batchSize == 0 for g in groups)
        groups = [g for g in groups if g % batchSize != 0]

        pos = [0] * batchSize
        for g in groups:
            pos[g % batchSize] += 1

        for i in range(1, batchSize):
            t = min(pos[i], pos[batchSize - i]) if 2 * i != batchSize else pos[i] // 2
            ans += t
            pos[i] -= t
            pos[batchSize - i] -= t

        if sum(pos) == 0: 
            return ans

        @lru_cache((None))
        def dfs(position, last):
            if sum(position) == 0:
                return 0

            ans = float("-inf")
            for i in range(batchSize):
                if position[i] > 0:
                    t = [j for j in position]
                    t[i] -= 1
                    U = (last - i) % batchSize 
                    ans = max(ans, dfs(tuple(t), U) + (U == 0))

            return ans

        return max(dfs(tuple(pos), i) for i in range(1, batchSize)) + ans
        
# @lc code=end

