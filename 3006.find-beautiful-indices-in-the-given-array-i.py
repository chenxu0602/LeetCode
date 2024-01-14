#
# @lc app=leetcode id=3006 lang=python3
#
# [3006] Find Beautiful Indices in the Given Array I
#

# @lc code=start
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        ans = []
        indices_a, indices_b = [], []

        for i in range(len(s) - len(a) + 1):
            if s[i:i + len(a)] == a:
                indices_a += i,

        for j in range(len(s) - len(b) + 1):
            if s[j:j + len(b)] == b:
                indices_b += j,

        for i in indices_a:
            for j in indices_b:
                if abs(i - j) <= k:
                    ans += i,
                    break

        ans.sort()

        return ans

        
# @lc code=end

