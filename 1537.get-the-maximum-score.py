#
# @lc app=leetcode id=1537 lang=python3
#
# [1537] Get the Maximum Score
#
# https://leetcode.com/problems/get-the-maximum-score/description/
#
# algorithms
# Hard (36.11%)
# Likes:    273
# Dislikes: 21
# Total Accepted:    8.4K
# Total Submissions: 23.2K
# Testcase Example:  '[2,4,5,8,10]\n[4,6,8,9]'
#
# You are given two sorted arrays of distinct integers nums1 and nums2.
# 
# A valid path is defined as follows:
# 
# 
# Choose array nums1 or nums2 to traverse (from index-0).
# Traverse the current array from left to right.
# If you are reading any value that is present in nums1 and nums2 you are
# allowed to change your path to the other array. (Only one repeated value is
# considered in the valid path).
# 
# 
# Score is defined as the sum of uniques values in a valid path.
# 
# Return the maximum score you can obtain of all possible valid paths.
# 
# Since the answer may be too large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]
# Output: 30
# Explanation: Valid paths:
# [2,4,5,8,10], [2,4,5,8,9], [2,4,6,8,9], [2,4,6,8,10],  (starting from nums1)
# [4,6,8,9], [4,5,8,10], [4,5,8,9], [4,6,8,10]    (starting from nums2)
# The maximum is obtained with the path in green [2,4,6,8,10].
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [1,3,5,7,9], nums2 = [3,5,100]
# Output: 109
# Explanation: Maximum sum is obtained with the path [1,3,5,100].
# 
# 
# Example 3:
# 
# 
# Input: nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10]
# Output: 40
# Explanation: There are no common elements between nums1 and nums2.
# Maximum sum is obtained with the path [6,7,8,9,10].
# 
# 
# Example 4:
# 
# 
# Input: nums1 = [1,4,5,8,9,11,19], nums2 = [2,3,4,11,12]
# Output: 61
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums1.length <= 10^5
# 1 <= nums2.length <= 10^5
# 1 <= nums1[i], nums2[i] <= 10^7
# nums1 and nums2 are strictly increasing.
# 
# 
#

# @lc code=start
from collections import defaultdict, deque

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Since the arrays are stricly increasing, there are no duplicates within each array. 
        # dists[num] = the max score to get to the node num.
        # O(M + N)
        # indeg = defaultdict(int)
        # graph = defaultdict(list)

        # for i in range(len(nums1) - 1):
        #     graph[nums1[i]].append(nums1[i + 1])
        #     indeg[nums1[i + 1]] += 1
        # for i in range(len(nums2) - 1):
        #     graph[nums2[i]].append(nums2[i + 1])
        #     indeg[nums2[i + 1]] += 1

        # queue = deque()
        # ans = 0
        # dists = defaultdict(int)

        # for num in graph:
        #     if indeg[num] == 0:
        #         queue.append((num, num))
        #         dists[num] = num

        # while queue:
        #     num, score = queue.popleft()
        #     ans = max(ans, score)
        #     for nei in graph[num]:
        #         indeg[nei] -= 1
        #         dists[nei] = max(dists[nei], score)
        #         if indeg[nei] == 0:
        #             queue.append((nei, nei + dists[nei]))

        # return ans % (10**9 + 7)


        # O(N) / O(1)
        m, n = map(len, (nums1, nums2))
        i, j, a, b = 0, 0, 0, 0
        MOD = 10**9 + 7

        while i < m or j < n:
            if i < m and (j == n or nums1[i] < nums2[j]):
                a += nums1[i]
                i += 1
            elif j < n and (i == m or nums1[i] > nums2[j]):
                b += nums2[j]
                j += 1
            else:
                a = b = max(a, b) + nums1[i] # nums1[i] == nums2[j], you can always get the max either way
                i += 1
                j += 1

        return max(a, b) % MOD
        
# @lc code=end

