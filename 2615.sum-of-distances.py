#
# @lc app=leetcode id=2615 lang=python3
#
# [2615] Sum of Distances
#

# @lc code=start
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = [0] * n
        mp = defaultdict(list)

        for i in range(n):
            mp[nums[i]].append(i)

        for i, indexes in mp.items():
            totSum = 0
            for idx in indexes:
                totSum += idx

            preSum = 0
            for i in range(len(indexes)):
                idx = indexes[i]
                postSum = totSum - preSum - idx

                ans[idx] += idx * i
                ans[idx] -= preSum
                ans[idx] -= idx * (len(indexes) - i - 1)
                ans[idx] += postSum

                preSum += idx

        return ans
        
# @lc code=end

