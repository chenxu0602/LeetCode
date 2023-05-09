#
# @lc app=leetcode id=2670 lang=python3
#
# [2670] Find the Distinct Difference Array
#

# @lc code=start
from collections import defaultdict, Counter

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:

        prefix, suffix = defaultdict(int), Counter(nums)
        result = []
        for x in nums:
            prefix[x] += 1
            suffix[x] -= 1
            if suffix[x] == 0:
                del suffix[x]

            result.append(len(prefix) - len(suffix))

        return result

        
# @lc code=end

