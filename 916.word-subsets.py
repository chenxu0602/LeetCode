#
# @lc app=leetcode id=916 lang=python3
#
# [916] Word Subsets
#
# https://leetcode.com/problems/word-subsets/description/
#
# algorithms
# Medium (45.58%)
# Likes:    203
# Dislikes: 53
# Total Accepted:    13.1K
# Total Submissions: 28.6K
# Testcase Example:  '["amazon","apple","facebook","google","leetcode"]\n["e","o"]'
#
# We are given two arrays A and B of words.  Each word is a string of lowercase
# letters.
# 
# Now, say that word b is a subset of word a if every letter in b occurs in a,
# including multiplicity.  For example, "wrr" is a subset of "warrior", but is
# not a subset of "world".
# 
# Now say a word a from A is universal if for every b in B, b is a subset of
# a. 
# 
# Return a list of all universal words in A.  You can return the words in any
# order.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
# Output: ["facebook","google","leetcode"]
# 
# 
# 
# Example 2:
# 
# 
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
# Output: ["apple","google","leetcode"]
# 
# 
# 
# Example 3:
# 
# 
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
# Output: ["facebook","google"]
# 
# 
# 
# Example 4:
# 
# 
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
# Output: ["google","leetcode"]
# 
# 
# 
# Example 5:
# 
# 
# Input: A = ["amazon","apple","facebook","google","leetcode"], B =
# ["ec","oc","ceo"]
# Output: ["facebook","leetcode"]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length, B.length <= 10000
# 1 <= A[i].length, B[i].length <= 10
# A[i] and B[i] consist only of lowercase letters.
# All words in A[i] are unique: there isn't i != j with A[i] == A[j].
# 
# 
# 
# 
# 
# 
# 
#
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        bmax = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), bmax)):
                ans.append(a)

        return ans
        

