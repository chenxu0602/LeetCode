#
# @lc app=leetcode id=666 lang=python3
#
# [666] Path Sum IV
#
# https://leetcode.com/problems/path-sum-iv/description/
#
# algorithms
# Medium (54.51%)
# Likes:    181
# Dislikes: 245
# Total Accepted:    12.6K
# Total Submissions: 23K
# Testcase Example:  '[113,215,221]'
#
# If the depth of a tree is smaller than 5, then this tree can be represented
# by a list of three-digits integers.
# 
# For each integer in this list:
# 
# 
# The hundreds digit represents the depth D of this node, 1 <= D <= 4.
# The tens digit represents the position P of this node in the level it belongs
# to, 1 <= P <= 8. The position is the same as that in a full binary tree.
# The units digit represents the value V of this node, 0 <= V <= 9.
# 
# 
# Given a list of ascending three-digits integers representing a binary tree
# with the depth smaller than 5, you need to return the sum of all paths from
# the root towards the leaves.
# 
# It's guaranteed that the given list represents a valid connected binary
# tree.
# 
# Example 1:
# 
# 
# Input: [113, 215, 221]
# Output: 12
# Explanation: 
# The tree that the list represents is:
# ⁠   3
# ⁠  / \
# ⁠ 5   1
# 
# The path sum is (3 + 5) + (3 + 1) = 12.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [113, 221]
# Output: 4
# Explanation: 
# The tree that the list represents is: 
# ⁠   3
# ⁠    \
# ⁠     1
# 
# The path sum is (3 + 1) = 4.
# 
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        # Direct Traversal
        # O(N)
        # def dfs(node, running_sum=0):
        #     if node not in values: return
        #     running_sum += values[node]
        #     depth, pos = divmod(node, 10)
        #     left = (depth + 1) * 10 + 2 * pos - 1
        #     right = left + 1

        #     if left not in values and right not in values:
        #         self.ans += running_sum
        #     else:
        #         dfs(left, running_sum)
        #         dfs(right, running_sum)

        # self.ans = 0
        # values = {x // 10: x % 10 for x in nums}

        # dfs(nums[0] // 10)
        # return self.ans


        # Bottom-up
        total, counter = 0, Counter()
        for num in reversed(nums):
            d, l, v = map(int, str(num))
            total += v * counter[d, l] or v
            counter[d - 1, (l + 1) // 2] += counter[d, l] or 1
        return total
        
# @lc code=end

