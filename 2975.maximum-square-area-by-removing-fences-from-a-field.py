#
# @lc app=leetcode id=2975 lang=python3
#
# [2975] Maximum Square Area by Removing Fences From a Field
#

# @lc code=start
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:

        MOD = 10**9 + 7
        s1, s2 = set(), set()
        hFences.extend([1, m])
        vFences.extend([1, n])
        hFences.sort(); vFences.sort()

        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                s1.add(hFences[j] - hFences[i])

        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                s2.add(vFences[j] - vFences[i])

        ans = 0
        for i in s1:
            if i in s2:
                k = i * i
                ans = max(ans, k)

        if ans == 0: return -1
        return ans % MOD
        
        
# @lc code=end

