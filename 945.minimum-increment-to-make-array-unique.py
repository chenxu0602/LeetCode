#
# @lc app=leetcode id=945 lang=python3
#
# [945] Minimum Increment to Make Array Unique
#
# https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/
#
# algorithms
# Medium (46.21%)
# Likes:    467
# Dislikes: 25
# Total Accepted:    28K
# Total Submissions: 60.3K
# Testcase Example:  '[1,2,2]'
#
# Given an array of integers A, a move consists of choosing any A[i], and
# incrementing it by 1.
# 
# Return the least number of moves to make every value in A unique.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,2]
# Output: 1
# Explanation:  After 1 move, the array could be [1, 2, 3].
# 
# 
# 
# Example 2:
# 
# 
# Input: [3,2,1,2,1,7]
# Output: 6
# Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
# It can be shown with 5 or less moves that it is impossible for the array to
# have all unique values.
# 
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= A.length <= 40000
# 0 <= A[i] < 40000
# 
# 
# 
# 
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        # Counting
        # If there are 2 or more values x in A, save the extra duplicated values to increment later.
        # If there are 0 values x in A, then a saved value v gets incremented to x.
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # count = Counter(A)
        # taken = []

        # ans = 0
        # for x in range(100000):
        #     if count[x] >= 2:
        #         taken.extend([x] * (count[x] - 1))
        #     elif taken and count[x] == 0:
        #         ans += x - taken.pop()

        # return ans


        # O(NlogN) 

        m, c, _ = float("-inf"), 0, A.sort()
        for a in A:
            if a <= m:
                c += 1 + m - a
                m += 1
            else:
                m = a
        return c


        # res = need = 0
        # for i in sorted(A):
        #     res += max(need - i, 0)
        #     need = max(need + 1, i + 1)
        # return res
# @lc code=end

