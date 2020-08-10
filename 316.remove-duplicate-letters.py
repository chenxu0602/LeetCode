#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#
# https://leetcode.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Hard (34.20%)
# Likes:    1059
# Dislikes: 94
# Total Accepted:    69.4K
# Total Submissions: 202.4K
# Testcase Example:  '"bcabc"'
#
# Given a string which contains only lowercase letters, remove duplicate
# letters so that every letter appears once and only once. You must make sure
# your result is the smallest in lexicographical order among all possible
# results.
# 
# Example 1:
# 
# 
# Input: "bcabc"
# Output: "abc"
# 
# 
# Example 2:
# 
# 
# Input: "cbacdcbc"
# Output: "acdb"
# 
# 
# Note: This question is the same as 1081:
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        # Greedy - Solving Letter by Letter
        # find pos - the index of the leftmost letter in our solution
        # we create a counter and end the iteration once the suffix doesn't have each unique character
        # pos will be the index of the smallest character we encounter before the iteration ends
        # Time  complexity: O(N) x C = O(N)
        # Space complexity: O(N) x C = O(N)
        # c = Counter(s)
        # pos = 0
        # for i in range(len(s)):
        #     if s[i] < s[pos]: pos = i
        #     c[s[i]] -= 1
        #     if c[s[i]] == 0: break
        #     # our answer is the leftmost letter plus the recursive call on the remainder of the string
        #     # note we have to get rid of further occurrences of s[pos] to ensure that there are no duplicates
        # return s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos], "")) if s else ""


        # Greedy - Solving with Stack
        # Time  complexity: O(N)
        # Space complexity: O(1)
        # stack, seen = [], set()
        # last_coccurrence = {c: i for i, c in enumerate(s)}

        # for i, c in enumerate(s):
        #     if c not in seen:
        #         while stack and c < stack[-1] and i < last_coccurrence[stack[-1]]:
        #             seen.discard(stack.pop())
        #         seen.add(c)
        #         stack.append(c)
        # return "".join(stack)


        rindex = {c: i for i, c in enumerate(s)}
        result = ""
        for i, c in enumerate(s):
            if c not in result:
                while c < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]
                result += c
        return result


        # result = ""
        # while s:
        #     i = min(map(s.rindex, set(s)))
        #     c = min(s[:i+1])
        #     result += c
        #     s = s[s.index(c):].replace(c, "")
        # return result



        
# @lc code=end

