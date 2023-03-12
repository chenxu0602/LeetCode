#
# @lc app=leetcode id=2468 lang=python3
#
# [2468] Split Message Based on Limit
#

# @lc code=start
class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:

        cur = k = i = 0
        while 3 + len(str(k)) * 2 < limit and cur + len(message) + (3 + len(str(k))) * k > limit * k:
            k += 1
            cur += len(str(k))

        res = []
        if 3 + len(str(k)) * 2 < limit:
            for j in range(1, k + 1):
                l = limit - (len(str(j)) + 3 + len(str(k)))
                res.append("%s<%s/%s>" % (message[i:i + l], j, k))
                i += l

        return res
        
# @lc code=end

