#
# @lc app=leetcode id=2014 lang=python3
#
# [2014] Longest Subsequence Repeated k Times
#

# @lc code=start
from collections import deque, Counter
import itertools

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:

        freq = [0] * 26
        for ch in s: 
            freq[ord(ch) - 97] += 1
        
        candidates = [chr(i + 97) for i, v in enumerate(freq) if v >= k]

        # def fn(ss):
        #     i = cnt = 0
        #     for ch in s:
        #         if ss[i] == ch:
        #             i += 1
        #             if i == len(ss):
        #                 if (cnt := cnt + 1) == k:
        #                     return True
        #                 i = 0

        def fn(ss):
            t = iter(s)
            return all(c in t for c in ss * k)

        ans = ""
        queue = deque([""])
        while queue:
            x = queue.popleft()
            for ch in candidates:
                xx = x + ch
                if fn(xx):
                    ans = xx
                    queue.append(xx)

        return ans

        # def isSubsequence(s, t):
        #     t = iter(t)
        #     return all(c in t for c in s)

        # hot = "".join(el * (freq // k) for el, freq in Counter(s).items())        

        # combs = set()
        # for i in range(len(hot) + 1):
        #     for candidate in itertools.combinations(hot, i):
        #         for perm in itertools.permutations(candidate):
        #             combs.add("".join(perm))

        # combs = sorted(combs, key=lambda x: (len(x), x), reverse=True)
        # for comb in combs:
        #     if isSubsequence(comb * k, s):
        #         return comb

        
# @lc code=end

