#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (27.02%)
# Likes:    5180
# Dislikes: 752
# Total Accepted:    522.6K
# Total Submissions: 1.9M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def kth(a, b, k):
            if not a: return b[k]
            if not b: return a[k]

            ia, ib = len(a) // 2, len(b) // 2
            ma, mb = a[ia], b[ib]

            if ia + ib < k:
                if ma > mb:
                    return kth(a, b[ib+1:], k-ib-1)
                else:
                    return kth(a[ia+1:], b, k-ia-1)
            else:
                if ma > mb:
                    return kth(a[:ia], b, k)
                else:
                    return kth(a, b[:ib], k)

        l = len(nums1) + len(nums2)
        if l % 2:
            return kth(nums1, nums2, l // 2)
        else:
            return 0.5 * (kth(nums1, nums2, l // 2 - 1) + kth(nums1, nums2, l // 2))


            
# @lc code=end

