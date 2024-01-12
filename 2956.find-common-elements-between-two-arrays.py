#
# @lc app=leetcode id=2956 lang=python3
#
# [2956] Find Common Elements Between Two Arrays
#

# @lc code=start
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:

        set1 = set(nums1)
        set2 = set(nums2)

        count1 = sum(1 for num in nums1 if num in set2)
        count2 = sum(1 for num in nums2 if num in set1)

        return [count1, count2]
        
# @lc code=end

