#
# @lc app=leetcode id=1481 lang=python3
#
# [1481] Least Number of Unique Integers after K Removals
#
# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/
#
# algorithms
# Medium (55.15%)
# Likes:    227
# Dislikes: 23
# Total Accepted:    22.3K
# Total Submissions: 40.3K
# Testcase Example:  '[5,5,4]\n1'
#
# Given an array of integers arr and an integer k. Find the least number of
# unique integers after removing exactly k elements.
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.
# 
# Example 2:
# 
# 
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3
# will be left.
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 10^9
# 0 <= k <= arr.length
# 
#

# @lc code=start
from collections import Counter
import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # c = Counter(arr)
        # s = sorted(arr, key=lambda x: (c[x], x))
        # return len(set(s[k:]))

        heap = [(val, key) for key, val in Counter(arr).items()]
        heapq.heapify(heap)

        while k > 0:
            k -= heapq.heappop(heap)[0]

        return len(heap) + (k < 0)
# @lc code=end

