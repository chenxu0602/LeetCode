#
# @lc app=leetcode id=1830 lang=python3
#
# [1830] Minimum Number of Operations to Make String Sorted
#
# https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/description/
#
# algorithms
# Hard (35.27%)
# Likes:    40
# Dislikes: 42
# Total Accepted:    597
# Total Submissions: 1.7K
# Testcase Example:  '"cba"'
#
# You are given a string s (0-indexed)​​​​​​. You are asked to perform the
# following operation on s​​​​​​ until you get a sorted string:
# 
# 
# Find the largest index i such that 1 <= i < s.length and s[i] < s[i - 1].
# Find the largest index j such that i <= j < s.length and s[k] < s[i - 1] for
# all the possible values of k in the range [i, j] inclusive.
# Swap the two characters at indices i - 1​​​​ and j​​​​​.
# Reverse the suffix starting at index i​​​​​​.
# 
# 
# Return the number of operations needed to make the string sorted. Since the
# answer can be too large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: s = "cba"
# Output: 5
# Explanation: The simulation goes as follows:
# Operation 1: i=2, j=2. Swap s[1] and s[2] to get s="cab", then reverse the
# suffix starting at 2. Now, s="cab".
# Operation 2: i=1, j=2. Swap s[0] and s[2] to get s="bac", then reverse the
# suffix starting at 1. Now, s="bca".
# Operation 3: i=2, j=2. Swap s[1] and s[2] to get s="bac", then reverse the
# suffix starting at 2. Now, s="bac".
# Operation 4: i=1, j=1. Swap s[0] and s[1] to get s="abc", then reverse the
# suffix starting at 1. Now, s="acb".
# Operation 5: i=2, j=2. Swap s[1] and s[2] to get s="abc", then reverse the
# suffix starting at 2. Now, s="abc".
# 
# 
# Example 2:
# 
# 
# Input: s = "aabaa"
# Output: 2
# Explanation: The simulation goes as follows:
# Operation 1: i=3, j=4. Swap s[2] and s[4] to get s="aaaab", then reverse the
# substring starting at 3. Now, s="aaaba".
# Operation 2: i=4, j=4. Swap s[3] and s[4] to get s="aaaab", then reverse the
# substring starting at 4. Now, s="aaaab".
# 
# 
# Example 3:
# 
# 
# Input: s = "cdbea"
# Output: 63
# 
# Example 4:
# 
# 
# Input: s = "leetcodeleetcodeleetcode"
# Output: 982157772
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 3000
# s​​​​​​ consists only of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def makeStringSorted(self, s: str) -> int:
        cnt, ans, tot, comb_tot = [0] * 26, 0, 0, 1
        for cur_letter in s[::-1]:
            num = ord(cur_letter) - ord('a')
            cnt[num] += 1
            tot += 1
            comb_tot = (comb_tot * tot) // cnt[num]
            ans += (comb_tot * sum(cnt[:num])) // tot
        return ans % (10**9 + 7)
        
# @lc code=end

