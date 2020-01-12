#
# @lc app=leetcode id=555 lang=python3
#
# [555] Split Concatenated Strings
#
# https://leetcode.com/problems/split-concatenated-strings/description/
#
# algorithms
# Medium (40.10%)
# Likes:    35
# Dislikes: 159
# Total Accepted:    3.9K
# Total Submissions: 9.6K
# Testcase Example:  '["abc","xyz"]'
#
# Given a list of strings, you could concatenate these strings together into a
# loop, where for each string you could choose to reverse it or not. Among all
# the possible loops, you need to find the lexicographically biggest string
# after cutting the loop, which will make the looped string into a regular
# one.
# 
# Specifically, to find the lexicographically biggest string, you need to
# experience two phases: 
# 
# Concatenate all the strings into a loop, where you can reverse some strings
# or not and connect them in the same order as given.
# Cut and make one breakpoint in any place of the loop, which will make the
# looped string into a regular one starting from the character at the
# cutpoint. 
# 
# 
# 
# And your job is to find the lexicographically biggest one among all the
# possible regular strings.
# 
# 
# Example:
# 
# Input: "abc", "xyz"
# Output: "zyxcba"
# Explanation: You can get the looped string "-abcxyz-", "-abczyx-",
# "-cbaxyz-", "-cbazyx-", where '-' represents the looped status. The answer
# string came from the fourth looped one, where you could cut from the middle
# character 'a' and get "zyxcba".
# 
# 
# 
# Note:
# 
# The input strings will only contain lowercase letters.
# The total length of all the strings will not over 1,000.
# 
# 
#
class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        max_strs = [max(x, x[::-1]) for x in strs]
        ans = ""
        for i, token in enumerate(max_strs):
            for start in (token, token[::-1]):
                for j in range(len(start)+1):
                    ans = max(ans, start[j:] + "".join(max_strs[i+1:] + max_strs[:i]) + start[:j])

        return ans

        

