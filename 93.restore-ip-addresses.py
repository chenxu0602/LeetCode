#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (33.64%)
# Likes:    970
# Dislikes: 436
# Total Accepted:    170.9K
# Total Submissions: 506.5K
# Testcase Example:  '"25525511135"'
#
# Given a string containing only digits, restore it by returning all possible
# valid IP address combinations.
# 
# Example:
# 
# 
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
# 
# 
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def dfs(s, sub, ips, ip):
            if sub == 4:
                if s == "":
                    ips.append(ip[1:])
                return

            for i in range(1, 4):
                if i <= len(s):
                    if int(s[:i]) <= 255:
                        dfs(s[i:], sub+1, ips, ip+'.'+s[:i])

                    if s[0] == '0': break

        ips = []
        dfs(s, 0, ips, "")
        return ips
        
# @lc code=end

