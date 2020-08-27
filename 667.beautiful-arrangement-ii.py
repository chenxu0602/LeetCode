#
# @lc app=leetcode id=667 lang=python3
#
# [667] Beautiful Arrangement II
#
# https://leetcode.com/problems/beautiful-arrangement-ii/description/
#
# algorithms
# Medium (52.26%)
# Likes:    232
# Dislikes: 539
# Total Accepted:    19.1K
# Total Submissions: 36.4K
# Testcase Example:  '3\n2'
#
# 
# Given two integers n and k, you need to construct a list which contains n
# different positive integers ranging from 1 to n and obeys the following
# requirement: 
# 
# Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 -
# a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.
# 
# 
# 
# If there are multiple answers, print any of them.
# 
# 
# Example 1:
# 
# Input: n = 3, k = 1
# Output: [1, 2, 3]
# Explanation: The [1, 2, 3] has three different positive integers ranging from
# 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
# 
# 
# 
# Example 2:
# 
# Input: n = 3, k = 2
# Output: [1, 3, 2]
# Explanation: The [1, 3, 2] has three different positive integers ranging from
# 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
# 
# 
# 
# Note:
# 
# The n and k are in the range 1 
# 
# 
#
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        # When k = n-1, a valid construction is [1, n, 2, n-1, 3, n-2, ....]
        # This leads to the following idea: we will put [1, 2, ...., n-k-1] first, and then we have N = k+1 adjacent numbers left, of which we want k different differences. 
        # O(n)
        ans = list(range(1, n - k))
        for i in range(k + 1):
            if i % 2 == 0:
                ans.append(n - k + i // 2)
            else:
                ans.append(n - i // 2)
        return ans
        

