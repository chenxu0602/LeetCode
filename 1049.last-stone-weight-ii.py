#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#
# https://leetcode.com/problems/last-stone-weight-ii/description/
#
# algorithms
# Medium (43.97%)
# Likes:    842
# Dislikes: 30
# Total Accepted:    21.8K
# Total Submissions: 49.3K
# Testcase Example:  '[2,7,4,1,8,1]'
#
# We have a collection of rocks, each rock has a positive integer weight.
# 
# Each turn, we choose any two rocks and smash them together.  Suppose the
# stones have weights x and y with x <= y.  The result of this smash is:
# 
# 
# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of
# weight y has new weight y-x.
# 
# 
# At the end, there is at most 1 stone left.  Return the smallest possible
# weight of this stone (the weight is 0 if there are no stones left.)
# 
# 
# 
# Example 1:
# 
# 
# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
# we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
# we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we can combine 1 and 1 to get 0 so the array converts to [1] then that's the
# optimal value.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 100
# 
#

# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Same problem as:
        # Divide all numbers into two groups,
        # what is the minimum difference between the sum of two groups.
        # Now it's a easy classic knapsack problem.
        # dp to record the achievable sum of the smaller group.
        # Time  complexity: O(N x S) where S = sum(stones)
        # Space complexity: O(S)

        # dp = {0}
        # sumA = sum(stones)
        # for a in stones:
        #     dp |= {a + i for i in dp}
        # return min(abs(sumA - i * 2) for i in dp)


        # dp, sumA = {0}, sum(stones)
        # for a in stones:
        #     dp = {a + x for x in dp} | {a - x for x in dp}
        # return min(abs(x) for x in dp)


        from functools import reduce
        return min(reduce(lambda dp, y: {x + y for x in dp} | {abs(x - y) for x in dp}, stones, {0}))


        
# @lc code=end

