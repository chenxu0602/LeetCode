#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#
# https://leetcode.com/problems/maximum-length-of-pair-chain/description/
#
# algorithms
# Medium (51.68%)
# Likes:    991
# Dislikes: 81
# Total Accepted:    60.7K
# Total Submissions: 116.7K
# Testcase Example:  '[[1,2], [2,3], [3,4]]'
#
# 
# You are given n pairs of numbers. In every pair, the first number is always
# smaller than the second number.
# 
# 
# 
# Now, we define a pair (c, d) can follow another pair (a, b) if and only if b
# < c. Chain of pairs can be formed in this fashion. 
# 
# 
# 
# Given a set of pairs, find the length longest chain which can be formed. You
# needn't use up all the given pairs. You can select pairs in any order.
# 
# 
# 
# Example 1:
# 
# Input: [[1,2], [2,3], [3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4]
# 
# 
# 
# Note:
# 
# The number of given pairs will be in the range [1, 1000].
# 
# 
#

# @lc code=start
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Dynamic Programming
        # Time  complexity: O(N^2)
        # Space complexity: O(N)
        # pairs.sort()
        # dp = [1] * len(pairs)

        # for j in range(len(pairs)):
        #     for i in range(j):
        #         if pairs[i][1] < pairs[j][0]:
        #             dp[j] = max(dp[j], dp[i] + 1)

        # return max(dp)


        # Greedy
        # Time  complexity: O(NlogN)
        # Space complexity: O(N)
        cur, ans = float("-inf"), 0
        for x, y in sorted(pairs, key=lambda x: x[1]):
            if cur < x:
                cur = y
                ans += 1
        return ans
        
# @lc code=end

