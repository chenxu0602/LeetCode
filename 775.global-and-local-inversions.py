#
# @lc app=leetcode id=775 lang=python3
#
# [775] Global and Local Inversions
#
# https://leetcode.com/problems/global-and-local-inversions/description/
#
# algorithms
# Medium (42.07%)
# Likes:    405
# Dislikes: 172
# Total Accepted:    22.4K
# Total Submissions: 53.2K
# Testcase Example:  '[0]'
#
# We have some permutation A of [0, 1, ..., N - 1], where N is the length of
# A.
# 
# The number of (global) inversions is the number of i < j with 0 <= i < j < N
# and A[i] > A[j].
# 
# The number of local inversions is the number of i with 0 <= i < N and A[i] >
# A[i+1].
# 
# Return true if and only if the number of global inversions is equal to the
# number of local inversions.
# 
# Example 1:
# 
# 
# Input: A = [1,0,2]
# Output: true
# Explanation: There is 1 global inversion, and 1 local inversion.
# 
# 
# Example 2:
# 
# 
# Input: A = [1,2,0]
# Output: false
# Explanation: There are 2 global inversions, and 1 local inversion.
# 
# 
# Note:
# 
# 
# A will be a permutation of [0, 1, ..., A.length - 1].
# A will have length in range [1, 5000].
# The time limit for this problem has been reduced.
# 
# 
#

# @lc code=start
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        # A local inversion is also a global inversion. 
        # Thus, we only need to check if our permutation 
        # has any non-local inversion (A[i] > A[j], i < j) with j - i > 1.
        # Time  complexity: O(N^2)
        # Space complexity: O(1)
        # return all(x < A[j] for i, x in enumerate(A) for j in range(i + 2, len(A)))


        # Same as checking for A[i] > min(A[i+2:]).
        # Time  complexity: O(N)
        # Space complexity: O(1)
        # N = len(A)
        # floor = N
        # for i in range(N - 1, -1, -1):
        #     floor = min(floor, A[i])
        #     if i >= 2 and A[i - 2] > floor:
        #         return False
        # return True


        # Linear Scan
        return all(abs(i - x) <= 1 for i, x in enumerate(A))
        
# @lc code=end

