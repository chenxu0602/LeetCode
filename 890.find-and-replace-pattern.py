#
# @lc app=leetcode id=890 lang=python3
#
# [890] Find and Replace Pattern
#
# https://leetcode.com/problems/find-and-replace-pattern/description/
#
# algorithms
# Medium (73.29%)
# Likes:    736
# Dislikes: 70
# Total Accepted:    53.4K
# Total Submissions: 72.6K
# Testcase Example:  '["abc","deq","mee","aqq","dkd","ccc"]\n"abb"'
#
# You have a list of words and a pattern, and you want to know which words in
# words matches the pattern.
# 
# A word matches the pattern if there exists a permutation of letters p so that
# after replacing every letter x in the pattern with p(x), we get the desired
# word.
# 
# (Recall that a permutation of letters is a bijection from letters to letters:
# every letter maps to another letter, and no two letters map to the same
# letter.)
# 
# Return a list of the words in words that match the given pattern. 
# 
# You may return the answer in any order.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a ->
# m, b -> e, ...}. 
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a
# permutation,
# since a and b map to the same letter.
# 
# 
# 
# Note:
# 
# 
# 1 <= words.length <= 50
# 1 <= pattern.length = words[i].length <= 20
# 
# 
# 
#

# @lc code=start
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # Two Maps
        # Time  complexity: O(N x K), where N is the number of words,
        # and K is the length of each word.
        # Space complexity: O(N x K)
        # def match(word):
        #     m1, m2 = {}, {}
        #     for w, p in zip(word, pattern):
        #         if w not in m1: m1[w] = p
        #         if p not in m2: m2[p] = w
        #         if (m1[w], m2[p]) != (p, w):
        #             return False
        #     return True

        # return filter(match, words)


        # One Map
        # Time  complexity: O(N x K), where N is the number of words,
        # and K is the length of each word.
        # Space complexity: O(N x K)
        # def match(word):
        #     P = {}
        #     for x, y in zip(pattern, word):
        #         if P.setdefault(x, y) != y:
        #             return False
        #     return len(set(P.values())) == len(P.values())

        # return filter(match, words)


        return [word for word in words
                if len(word) == len(pattern) and
                len(set(word)) == len(set(pattern)) and
                len(set(zip(word, pattern))) == len(set(word))]

        
# @lc code=end

