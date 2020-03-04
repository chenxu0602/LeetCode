#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
#
# algorithms
# Medium (35.36%)
# Likes:    1027
# Dislikes: 86
# Total Accepted:    87.1K
# Total Submissions: 245.6K
# Testcase Example:  '[1,7,11]\n[2,4,6]\n3'
#
# You are given two integer arrays nums1 and nums2 sorted in ascending order
# and an integer k.
# 
# Define a pair (u,v) which consists of one element from the first array and
# one element from the second array.
# 
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
# 
# Example 1:
# 
# 
# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]] 
# Explanation: The first 3 pairs are returned from the sequence: 
# [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# 
# Example 2:
# 
# 
# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [1,1],[1,1]
# Explanation: The first 2 pairs are returned from the sequence: 
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# 
# Example 3:
# 
# 
# Input: nums1 = [1,2], nums2 = [3], k = 3
# Output: [1,3],[2,3]
# Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
# 
# 
#

# @lc code=start
import heapq, itertools

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # return heapq.nsmallest(k, itertools.product(nums1, nums2), key=sum)

        streams = map(lambda u: ([u + v, u, v] for v in nums2), nums1)
        stream = heapq.merge(*streams)
        return [suv[1:] for suv in itertools.islice(stream, k)]
        
# @lc code=end

