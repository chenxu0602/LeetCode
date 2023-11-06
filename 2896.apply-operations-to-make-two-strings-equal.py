#
# @lc app=leetcode id=2896 lang=python3
#
# [2896] Apply Operations to Make Two Strings Equal
#

# @lc code=start
from functools import lru_cache

class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:

        # s = [i for i in range(len(s1)) if s1[i] != s2[i]]

        # @lru_cache(None)
        # def dfs(i, j):
        #     return 0 if i == j else min(
        #         min(x, s[k] - s[i]) + dfs(i + 1, k) + dfs(k + 1, j)
        #         for k in range(i + 1, j, 2)
        #     )

        # return -1 if len(s) % 2 else dfs(0, len(s))


        # done means we change the prefix to all 0.
        # one means we have one 1 in the prefix.
        # last means the last element in the prefix is still 1.
        # two means we have one 1 in prefix and last 1 at end of prefix.

        # For case s1[i] == s2[i],
        # if we are done, we are still done.
        # if we have one, we still have one.
        # We move the last from A[i - 1] to A[1] with cost is 1,
        # so last++, two++.

        # similar for case s1[i] != s2[i],
        # done = min(one + x, last + 1)
        # two = one;
        # one = min(done, two + 1)
        # last = min(done, two + x)
        # done, one, last, two = 0, float("inf"), float("inf"), float("inf")
        # for a, b in zip(s1, s2):
        #     if a == b:
        #         last, two = last + 1, two + 1
        #     else:
        #         done, one, last, two = min(one + x, last + 1), min(done, two + 1), min(done, two + x), one

        # return done if done < float("inf") else -1


        # The idea is that, we transform the two operation:

        # flip only s[i], cost is x / 2.
        # flip s[i] and s[j], cost is j - i, where i < j.
        # The first operation is equal to original one,
        # as long as it will be done in even times,
        # and we will do a joint order(拼多多).

        # We use odd to count the number of s1[i] != s2[i],
        # After one operation, the odd/even of difference won't change,
        # so if the number of diff is odd, we return -1.

        # res is the current result,
        # pre is the last time result plus the distance.
        # To keep using integer, we double the cost during calculation.
        res, pre, c = 0, float("inf"), 0
        for a, b in zip(s1, s2):
            pre += 2
            if a != b:
                res, pre, c = min(res + x, pre), res, c ^ 1

        return res // 2 if c == 0 else -1


        
# @lc code=end

