#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (32.17%)
# Likes:    823
# Dislikes: 349
# Total Accepted:    155.8K
# Total Submissions: 476.9K
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
        """
        def dfs(s, index, path, res):
            if index == 4:
                if not s:
                    res.append(path[:-1])
                
            for i in range(1, 4):
                if i <= len(s):
                    if i == 1:
                        dfs(s[i:], index+1, path+s[:i]+".", res)
                    elif i == 2 and s[0] != '0':
                        dfs(s[i:], index+1, path+s[:i]+".", res)
                    elif i == 3 and s[0] != '0' and int(s[:3]) <= 255:
                        dfs(s[i:], index+1, path+s[:i]+".", res)

        res = []
        dfs(s, 0, "", res)
        return res
        """

        """
        def valid(segment):
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1

        def update_output(curr_pos):
            segment = s[curr_pos+1:n]
            if valid(segment):
                segments.append(segment)
                output.append('.'.join(segments))
                segments.pop()

        def backtrack(prev_pos=-1, dots=3):
            for curr_pos in range(prev_pos+1, min(n-1, prev_pos+4)):
                segment = s[prev_pos+1:curr_pos+1]
                if valid(segment):
                    segments.append(segment)
                    if dots - 1 == 0:
                        update_output(curr_pos)
                    else:
                        backtrack(curr_pos, dots-1)
                    segments.pop()

        n = len(s)
        output, segments = [], []
        backtrack()
        return output
        """

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

