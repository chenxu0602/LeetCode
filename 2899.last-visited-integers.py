#
# @lc app=leetcode id=2899 lang=python3
#
# [2899] Last Visited Integers
#

# @lc code=start
class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:

        k, li, ans = 0, [], []
        for word in words:
            if word == 'prev':
                k += 1
                if k > len(li):
                    ans += -1,
                else:
                    ans += li[-k],
            else:
                k = 0
                li += int(word),

        return ans
        
# @lc code=end

