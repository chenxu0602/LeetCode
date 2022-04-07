#
# @lc app=leetcode id=2161 lang=python3
#
# [2161] Partition Array According to Given Pivot
#

# @lc code=start
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        """
        pivotFreq, ans = 0, []

        for num in nums:
            if num < pivot:
                ans.append(num)
            elif num == pivot:
                pivotFreq += 1

        ans.extend([pivot] * pivotFreq)

        for num in nums:
            if num > pivot:
                ans.append(num)

        return ans
        """

        n = len(nums)
        ans = [pivot] * n
        left, right = 0, -1
        for i, num in enumerate(nums):
            if num < pivot:
                ans[left], left = num, left + 1

            if nums[~i] > pivot:
                ans[right], right = nums[~i], right - 1

        return ans
        
# @lc code=end

