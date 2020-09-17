#
# @lc app=leetcode id=845 lang=python3
#
# [845] Longest Mountain in Array
#
# https://leetcode.com/problems/longest-mountain-in-array/description/
#
# algorithms
# Medium (37.11%)
# Likes:    657
# Dislikes: 27
# Total Accepted:    37K
# Total Submissions: 98.9K
# Testcase Example:  '[2,1,4,7,3,2,5]'
#
# Let's call any (contiguous) subarray B (of A) a mountain if the following
# properties hold:
# 
# 
# B.length >= 3
# There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] <
# B[i] > B[i+1] > ... > B[B.length - 1]
# 
# 
# (Note that B could be any subarray of A, including the entire array A.)
# 
# Given an array A of integers, return the length of the longest mountain. 
# 
# Return 0 if there is no mountain.
# 
# Example 1:
# 
# 
# Input: [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
# 
# 
# Example 2:
# 
# 
# Input: [2,2,2]
# Output: 0
# Explanation: There is no mountain.
# 
# 
# Note:
# 
# 
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000
# 
# 
# Follow up:
# 
# 
# Can you solve it using only one pass?
# Can you solve it in O(1) space?
# 
# 
#

# @lc code=start
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        # Time  complexity: O(N)
        # Space complexity: O(1)
        # start, ans = None, 0
        # i, L = 0, len(A)
        # while i < L - 1:
        #     if A[i] < A[i + 1]:
        #         start = i
        #         while i + 1 < L and A[i] < A[i + 1]:
        #             i += 1
        #     elif A[i] == A[i + 1]:
        #         i += 1 
        #         start = None
        #     else:
        #         i += 1
        #         if start != None:
        #             ans = max(ans, i - start + 1)

        # return ans


        N, ans, base = len(A), 0, 0

        while base < N:
            end = base
            if end + 1 < N and A[end] < A[end + 1]:
                while end + 1 < N and A[end] < A[end + 1]:
                    end += 1

                if end + 1 < N and A[end] > A[end + 1]:
                    while end + 1 < N and A[end] > A[end + 1]:
                        end += 1
                    ans = max(ans, end - base + 1)

            base = max(end, base + 1)

        return ans
        
# @lc code=end

