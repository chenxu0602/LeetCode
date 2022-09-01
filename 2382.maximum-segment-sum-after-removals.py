#
# @lc app=leetcode id=2382 lang=python3
#
# [2382] Maximum Segment Sum After Removals
#

# @lc code=start
class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:

        mp, cur, res = {}, 0, []
        for q in reversed(removeQueries[1:]):
            mp[q] = (nums[q], 1)
            rv, rl = mp.get(q + 1, (0, 0))
            lv, ll = mp.get(q - 1, (0, 0))

            total = nums[q] + rv + lv
            mp[q + rl] = (total, ll + rl + 1)
            mp[q - ll] = (total, ll + rl + 1)

            cur = max(cur, total)
            res.append(cur)

        return res[::-1] + [0]
        
# @lc code=end

