#
# @lc app=leetcode id=954 lang=python3
#
# [954] Array of Doubled Pairs
#
# https://leetcode.com/problems/array-of-doubled-pairs/description/
#
# algorithms
# Medium (35.53%)
# Likes:    310
# Dislikes: 51
# Total Accepted:    20K
# Total Submissions: 56.2K
# Testcase Example:  '[3,1,3,6]'
#
# Given an array of integers A with even length, return true if and only if it
# is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0
# <= i < len(A) / 2.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [3,1,3,6]
# Output: false
# 
# 
# 
# Example 2:
# 
# 
# Input: [2,1,2,6]
# Output: false
# 
# 
# 
# Example 3:
# 
# 
# Input: [4,-2,2,-4]
# Output: true
# Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or
# [2,4,-2,-4].
# 
# 
# 
# Example 4:
# 
# 
# Input: [1,2,4,16,8,4]
# Output: false
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= A.length <= 30000
# A.length is even
# -100000 <= A[i] <= 100000
# 
# 
# 
# 
# 
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        # Greedy
        # Time  complexity: O(NlogN)
        # Space complexity: O(N)
        # count = Counter(A)
        # for x in sorted(A, key=abs):
        #     if count[x] == 0: continue
        #     if count[2 * x] == 0: return False
        #     count[x] -= 1
        #     count[2 * x] -= 1
        # return True


        count = Counter(A)
        for x in sorted(count, key=abs):
            if count[x] > count[2 * x]:
                return False
            count[2 * x] -= count[x]
        return True
        
# @lc code=end

