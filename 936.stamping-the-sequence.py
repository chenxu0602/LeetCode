#
# @lc app=leetcode id=936 lang=python3
#
# [936] Stamping The Sequence
#
# https://leetcode.com/problems/stamping-the-sequence/description/
#
# algorithms
# Hard (35.73%)
# Likes:    107
# Dislikes: 30
# Total Accepted:    3.7K
# Total Submissions: 10.4K
# Testcase Example:  '"abc"\n"ababc"'
#
# You want to form a target string of lowercase letters.
# 
# At the beginning, your sequence is target.length '?' marks.  You also have a
# stamp of lowercase letters.
# 
# On each turn, you may place the stamp over the sequence, and replace every
# letter in the sequence with the corresponding letter from the stamp.  You can
# make up to 10 * target.length turns.
# 
# For example, if the initial sequence is "?????", and your stamp is "abc",
# then you may make "abc??", "?abc?", "??abc" in the first turn.  (Note that
# the stamp must be fully contained in the boundaries of the sequence in order
# to stamp.)
# 
# If the sequence is possible to stamp, then return an array of the index of
# the left-most letter being stamped at each turn.  If the sequence is not
# possible to stamp, return an empty array.
# 
# For example, if the sequence is "ababc", and the stamp is "abc", then we
# could return the answer [0, 2], corresponding to the moves "?????" -> "abc??"
# -> "ababc".
# 
# Also, if the sequence is possible to stamp, it is guaranteed it is possible
# to stamp within 10 * target.length moves.  Any answers specifying more than
# this number of moves will not be accepted.
# 
# 
# 
# Example 1:
# 
# 
# Input: stamp = "abc", target = "ababc"
# Output: [0,2]
# ([1,0,2] would also be accepted as an answer, as well as some other
# answers.)
# 
# 
# 
# Example 2:
# 
# 
# Input: stamp = "abca", target = "aabcaca"
# Output: [3,0,1]
# 
# 
# 
# 
# 
# Note:
# 
# 
# 
# 
# 1 <= stamp.length <= target.length <= 1000
# stamp and target only contain lowercase letters.
# 
#
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        # memo, ls, lt = {}, len(stamp), len(target)
        # def dfs(s, t, seqs):
        #     if t == lt:
        #         memo[s, t] = seqs if s == ls else []
        #     if (s, t) not in memo:
        #         if s == ls:
        #             for i in range(ls):
        #                 cand = dfs(i, t, [t-i] + seqs)
        #                 if cand:
        #                     memo[s, t] = cand
        #                     break
        #             else:
        #                 memo[s, t] = []
        #         elif target[t] == stamp[s]:
        #             cand = dfs(s+1, t+1, seqs)
        #             memo[s, t] = cand if cand else dfs(0, t+1, seqs+[t+1])
        #         else:
        #             memo[s, t] = []
        #     return memo[s, t]

        # return dfs(0, 0, [0])


        # Reversely change from target to ????....??? whenever we find a matched stamp substring.
        n, m, t, s, res = len(target), len(stamp), list(target), list(stamp), []

        def check(i):
            changed = False
            for j in range(m):
                if t[i + j] == '?':
                    continue
                if t[i + j] != s[j]:
                    return False
                changed = True
            if changed:
                t[i:i + m] = ['?'] * m
                res.append(i)

            return changed

        changed = True
        while changed:
            changed = False
            for i in range(n - m + 1):
                changed |= check(i)

        return res[::-1] if t == ['?'] * n else []


