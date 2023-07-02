#
# @lc app=leetcode id=6894 lang=python3
#
# [6894] Sum of Imbalance Numbers of All Subarrays
#

# @lc code=start
class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:

        """
        n, res = len(nums), 0
        for i in range(n):
            s = set()
            cur = -1
            for j in range(i, n):
                cur += 0 if nums[j] in s else 1 - (nums[j] + 1 in s) - (nums[j] - 1 in s)
                s.add(nums[j])
                res += cur

        return res
        """

        n, res = len(nums), 0
        left = [0] * n
        seen = [-1] * (n + 10)
        for i in range(n):
            left[i] = max(seen[nums[i] + 1], seen[nums[i]])
            seen[nums[i]] = i

        seen = [n] * (n + 10)
        for i in range(n - 1, -1, -1):
            seen[nums[i]] = i
            res += (i - left[i]) * (seen[nums[i] + 1] - i)

        return res - n * (n + 1) // 2
        
# @lc code=end

