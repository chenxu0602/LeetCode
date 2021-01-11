#
# @lc app=leetcode id=1720 lang=python3
#
# [1720] Decode XORed Array
#

# @lc code=start
import itertools

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # res = [first]
        # for x in encoded:
        #     res.append(res[-1] ^ x )
        # return res

        return list(itertools.accumulate([first] + encoded, lambda x, y: x ^ y))
        
# @lc code=end

