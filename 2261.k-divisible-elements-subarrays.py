#
# @lc app=leetcode id=2261 lang=python3
#
# [2261] K Divisible Elements Subarrays
#

# @lc code=start
from collections import defaultdict

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        s = set()

        for i in range(n):
            cnt = 0
            temp = ""
            for j in range(i, n):
                if nums[j] % p == 0:
                    cnt += 1

                temp += str(nums[j]) + ','
                if cnt > k: break

                s.add(temp)

        return len(s)

        
# @lc code=end

