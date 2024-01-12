#
# @lc app=leetcode id=2948 lang=python3
#
# [2948] Make Lexicographically Smallest Array by Swapping Elements
#

# @lc code=start
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        n = len(nums)
        pairs = [[nums[i], i] for i in range(n)]
        pairs = sorted(pairs, key=lambda x: x[0])

        result = [0] * n
        start = 0
        for end in range(n):
            if end + 1 >= n or pairs[end + 1][0] - pairs[end][0] > limit:
                temp = [pairs[i][1] for i in range(start, end + 1)]
                temp = sorted(temp)
                j = start
                for idx in temp:
                    result[idx] = pairs[j][0]
                    j += 1
                start = end + 1

        return result
        
# @lc code=end

