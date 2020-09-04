#
# @lc app=leetcode id=801 lang=python3
#
# [801] Minimum Swaps To Make Sequences Increasing
#
# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/description/
#
# algorithms
# Medium (37.91%)
# Likes:    818
# Dislikes: 60
# Total Accepted:    25.2K
# Total Submissions: 66.4K
# Testcase Example:  '[1,3,5,4]\n[1,2,3,7]'
#
# We have two integer sequences A and B of the same non-zero length.
# 
# We are allowed to swap elements A[i] and B[i].  Note that both elements are
# in the same index position in their respective sequences.
# 
# At the end of some number of swaps, A and B are both strictly increasing.  (A
# sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... <
# A[A.length - 1].)
# 
# Given A and B, return the minimum number of swaps to make both sequences
# strictly increasing.  It is guaranteed that the given input always makes it
# possible.
# 
# 
# Example:
# Input: A = [1,3,5,4], B = [1,2,3,7]
# Output: 1
# Explanation: 
# Swap A[3] and B[3].  Then the sequences are:
# A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
# which are both strictly increasing.
# 
# 
# Note:
# 
# 
# A, B are arrays with the same length, and that length will be in the range
# [1, 1000].
# A[i], B[i] are integer values in the range [0, 2000].
# 
# 
#

# @lc code=start
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        # Dynamic Programming
        # Let's remember n1 (natural1), the cost of making the first i-1 columns 
        # increasing and not swapping the i-1th column; and s1 (swapped1), 
        # the cost of making the first i-1 columns increasing and swapping the i-1th column.
        # Time  complexity: O(N)
        # Space complexity: O(1)
        n1, s1 = 0, 1

        for i in range(1, len(A)):
            n2 = s2 = float("inf")
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                n2, s2 = n1, s1 + 1
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                n2, s2 = min(n2, s1), min(s2, n1 + 1)

            n1, s1 = n2, s2

        return min(n1, s1)
        
# @lc code=end

