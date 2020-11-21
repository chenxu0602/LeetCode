#
# @lc app=leetcode id=1438 lang=python3
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#
# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
#
# algorithms
# Medium (43.48%)
# Likes:    941
# Dislikes: 43
# Total Accepted:    38.4K
# Total Submissions: 88.3K
# Testcase Example:  '[8,2,4,7]\n4'
#
# Given an array of integers nums and an integer limit, return the size of the
# longest non-empty subarray such that the absolute difference between any two
# elements of this subarray is less than or equal to limit.
# 
# 
# Example 1:
# 
# 
# Input: nums = [8,2,4,7], limit = 4
# Output: 2 
# Explanation: All subarrays are: 
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4. 
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4. 
# Therefore, the size of the longest subarray is 2.
# 
# 
# Example 2:
# 
# 
# Input: nums = [10,1,2,4,7,2], limit = 5
# Output: 4 
# Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute
# diff is |2-7| = 5 <= 5.
# 
# 
# Example 3:
# 
# 
# Input: nums = [4,2,2,2,4,4,2,2], limit = 0
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 0 <= limit <= 10^9
# 
# 
#

# @lc code=start
import bisect, heapq
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # i, L = 0, []
        # for j in range(len(nums)):
        #     bisect.insort(L, nums[j])
        #     if L[-1] - L[0] > limit:
        #         L.pop(bisect.bisect(L, nums[i]) - 1)
        #         i += 1
        # return j - i + 1


        # maxq, minq = [], []
        # res = i = 0
        # for j, a in enumerate(nums):
        #     heapq.heappush(maxq, [-a, j])
        #     heapq.heappush(minq, [a, j])

        #     while -maxq[0][0] - minq[0][0] > limit:
        #         i = min(maxq[0][1], minq[0][1]) + 1
        #         while maxq[0][1] < i:
        #             heapq.heappop(maxq)
        #         while minq[0][1] < i:
        #             heapq.heappop(minq)

        #     res = max(res, j - i + 1)

        # return res


        maxq, minq, i = deque([]), deque([]), 0
        for _, num in enumerate(nums):
            while maxq and maxq[-1] < num:
                maxq.pop()
            while minq and minq[-1] > num:
                minq.pop()

            maxq.append(num)
            minq.append(num)

            if maxq[0] - minq[0] > limit:
                if maxq[0] == nums[i]:
                    maxq.popleft()
                if minq[0] == nums[i]:
                    minq.popleft()
                i += 1

        return len(nums) - i
        
# @lc code=end

