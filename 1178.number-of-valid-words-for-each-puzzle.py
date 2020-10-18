#
# @lc app=leetcode id=1178 lang=python3
#
# [1178] Number of Valid Words for Each Puzzle
#
# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/description/
#
# algorithms
# Hard (37.11%)
# Likes:    151
# Dislikes: 13
# Total Accepted:    4.7K
# Total Submissions: 12.8K
# Testcase Example:  '["aaaa","asas","able","ability","actt","actor","access"]\n' + '["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]'
#
# With respect to a given puzzle string, a word is valid if both the following
# conditions are satisfied:
# 
# word contains the first letter of puzzle.
# For each letter in word, that letter is in puzzle.
# For example, if the puzzle is "abcdefg", then valid words are "faced",
# "cabbage", and "baggage"; while invalid words are "beefed" (doesn't include
# "a") and "based" (includes "s" which isn't in the puzzle).
# 
# Return an array answer, where answer[i] is the number of words in the given
# word list words that are valid with respect to the puzzle puzzles[i].
# 
# Example :
# 
# 
# Input: 
# words = ["aaaa","asas","able","ability","actt","actor","access"], 
# puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
# Output: [1,1,3,2,4,0]
# Explanation:
# 1 valid word for "aboveyz" : "aaaa" 
# 1 valid word for "abrodyz" : "aaaa"
# 3 valid words for "abslute" : "aaaa", "asas", "able"
# 2 valid words for "absoryz" : "aaaa", "asas"
# 4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
# There're no valid words for "gaswxyz" cause none of the words in the list
# contains letter 'g'.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 10^5
# 4 <= words[i].length <= 50
# 1 <= puzzles.length <= 10^4
# puzzles[i].length == 7
# words[i][j], puzzles[i][j] are English lowercase letters.
# Each puzzles[i] doesn't contain repeated characters.
# 
# 
#

# @lc code=start
from collections import Counter
from itertools import combinations

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # count = Counter(frozenset(w) for w in words)
        # res = []
        # for p in puzzles:
        #     cur = 0
        #     for k in range(7):
        #         for c in combinations(p[1:], k):
        #             cur += count[frozenset(tuple(p[0]) + c)]
        #     res.append(cur)
        # return res


        # count = Counter(frozenset(w) for w in words)
        # res = []
        # for p in puzzles:
        #     subs = [p[0]]
        #     for c in p[1:]:
        #         subs += [s + c for s in subs]
        #     res.append(sum(count[frozenset(s)] for s in subs))
        # return res


        count = Counter()
        for w in words:
            if len(set(w)) > 7:
                continue
            m = 0
            for c in w:
                m |= 1 << (ord(c) - ord('a'))
            count[m] += 1

        res = []
        for p in puzzles:
            bfs = [1 << ord(p[0]) - ord('a')]
            for c in p[1:]:
                bfs += [m | 1 << ord(c) - ord('a') for m in bfs]
            res.append(sum(count[m] for m in bfs))
        return res

        
# @lc code=end

