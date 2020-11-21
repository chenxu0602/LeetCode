#
# @lc app=leetcode id=1461 lang=python3
#
# [1461] Check If a String Contains All Binary Codes of Size K
#
# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/
#
# algorithms
# Medium (46.17%)
# Likes:    180
# Dislikes: 44
# Total Accepted:    12.9K
# Total Submissions: 28K
# Testcase Example:  '"00110110"\n2'
#
# Given a binary string s and an integer k.
# 
# Return True if every binary code of length k is a substring of s. Otherwise,
# return False.
# 
# 
# Example 1:
# 
# 
# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They
# can be all found as substrings at indicies 0, 1, 3 and 2 respectively.
# 
# 
# Example 2:
# 
# 
# Input: s = "00110", k = 2
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "0110", k = 1
# Output: true
# Explanation: The binary codes of length 1 are "0" and "1", it is clear that
# both exist as a substring. 
# 
# 
# Example 4:
# 
# 
# Input: s = "0110", k = 2
# Output: false
# Explanation: The binary code "00" is of length 2 and doesn't exist in the
# array.
# 
# 
# Example 5:
# 
# 
# Input: s = "0000000001011100", k = 4
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 5 * 10^5
# s consists of 0's and 1's only.
# 1 <= k <= 20
# 
# 
#

# @lc code=start
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # Time  complexity: O(NK)
        # Space complexity: O(NK)
        # need = 1 << k
        # got = set()

        # for i in range(k, len(s) + 1):
        #     tmp = s[i - k:i]
        #     if tmp not in got:
        #         got.add(tmp)
        #         need -= 1
        #         if need == 0:
        #             return True

        # return False


        # got = {s[i - k:i] for i in range(k, len(s) + 1)}
        # return len(got) == 1 << k


        # Time  complexity: O(N)
        # Space complexity: O(2^k)
        need = 1 << k
        got = [False] * need
        all_one = need - 1
        hash_val = 0

        for i in range(len(s)):
            # calculate hash for s[i-k+1:i+1]
            hash_val = ((hash_val << 1) & all_one) | (int(s[i]))
            # hash only available when i-k+1 > 0
            if i >= k - 1 and got[hash_val] is False:
                got[hash_val] = True
                need -= 1
                if need == 0:
                    return True

        return False


        
# @lc code=end

