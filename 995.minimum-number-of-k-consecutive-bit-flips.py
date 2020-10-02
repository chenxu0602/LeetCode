#
# @lc app=leetcode id=995 lang=python3
#
# [995] Minimum Number of K Consecutive Bit Flips
#
# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/description/
#
# algorithms
# Hard (46.48%)
# Likes:    203
# Dislikes: 26
# Total Accepted:    7.9K
# Total Submissions: 17.1K
# Testcase Example:  '[0,1,0]\n1'
#
# In an array A containing only 0s and 1s, a K-bit flip consists of choosing a
# (contiguous) subarray of length K and simultaneously changing every 0 in the
# subarray to 1, and every 1 in the subarray to 0.
# 
# Return the minimum number of K-bit flips required so that there is no 0 in
# the array.  If it is not possible, return -1.
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [0,1,0], K = 1
# Output: 2
# Explanation: Flip A[0], then flip A[2].
# 
# 
# 
# Example 2:
# 
# 
# Input: A = [1,1,0], K = 2
# Output: -1
# Explanation: No matter how we flip subarrays of size 2, we can't make the
# array become [1,1,1].
# 
# 
# 
# Example 3:
# 
# 
# Input: A = [0,0,0,1,0,1,1,0], K = 3
# Output: 3
# Explanation:
# Flip A[0],A[1],A[2]: A becomes [1,1,1,1,0,1,1,0]
# Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
# Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 30000
# 1 <= K <= A.length
# 
#

# @lc code=start
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        # Greedy + Events
        # Time  complexity: O(N)
        # Space complexity: O(N)
        N = len(A)
        hint = [0] * N
        ans = flip = 0

        # When we flip a subarray like A[i], A[i+1], ..., A[i+K-1]
        # we can instead flip our current writing state, and put a hint at
        # position i+K to flip back our writing state.
        for i, x in enumerate(A):
            flip ^= hint[i]
            if x ^ flip == 0: # If we must flip the subarray starting here...
                ans += 1 # We're flipping the subarray from A[i] to A[i+K-1]

                if i + K > N: return -1 # If we can't flip the entire subarray, its impossible
                flip ^= 1
                if i + K < N: hint[i + K] ^= 1

        return ans


        # cur = res = 0
        # for i in range(len(A)):
        #     if i >= K and A[i - K] == 2:
        #         cur -= 1
        #     if cur % 2 == A[i]:
        #         if i + K > len(A):
        #             return -1
        #         A[i] = 2
        #         cur, res = cur + 1, res + 1
        # return res
        
# @lc code=end

