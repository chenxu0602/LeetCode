#
# @lc app=leetcode id=468 lang=python3
#
# [468] Validate IP Address
#
# https://leetcode.com/problems/validate-ip-address/description/
#
# algorithms
# Medium (24.01%)
# Likes:    350
# Dislikes: 1760
# Total Accepted:    79.5K
# Total Submissions: 330.4K
# Testcase Example:  '"172.16.254.1"'
#
# Given a string IP. We need to check If IP is a valid IPv4 address, valid IPv6
# address or not a valid IP address.
# 
# Return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6
# address or "Neither" if IP is not a valid IP of any type.
# 
# A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255
# and xi cannot contain leading zeros. For example, "192.168.1.1" and
# "192.168.1.0" are valid IPv4 addresses but "192.168.01.1", "192.168.1.00" and
# "192.168@1.1" are invalid IPv4 adresses.
# 
# A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8"
# where:
# 
# 
# 1 <= xi.length <= 4
# xi is hexadecimal string whcih may contain digits, lower-case English letter
# ('a' to 'f') and/or upper-case English letters ('A' to 'F').
# Leading zeros are allowed in xi.
# 
# 
# For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and
# "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses but
# "2001:0db8:85a3::8A2E:037j:7334" and
# "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.
# 
# 
# Example 1:
# 
# 
# Input: IP = "172.16.254.1"
# Output: "IPv4"
# Explanation: This is a valid IPv4 address, return "IPv4".
# 
# 
# Example 2:
# 
# 
# Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
# Output: "IPv6"
# Explanation: This is a valid IPv6 address, return "IPv6".
# 
# 
# Example 3:
# 
# 
# Input: IP = "256.256.256.256"
# Output: "Neither"
# Explanation: This is neither a IPv4 address nor a IPv6 address.
# 
# 
# Example 4:
# 
# 
# Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
# Output: "Neither"
# 
# 
# Example 5:
# 
# 
# Input: IP = "1e1.4.5.6"
# Output: "Neither"
# 
# 
# 
# Constraints:
# 
# 
# IP consists only of English letters, digits and the characters '.' and ':'.
# 
# 
#

# @lc code=start
class Solution:
    def validIPAddress(self, IP: str) -> str:
        # Time  complexity: O(1)
        # Space complexity: O(1)
        import re
        chunk_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
        patten_IPv4 = re.compile(r'^(' + chunk_IPv4 + r'\.){3}' + chunk_IPv4 + r'$')

        chunk_IPv6 = r'([0-9a-fA-F]{1,4})'
        patten_IPv6 = re.compile(r'^(' + chunk_IPv6 + r'\:){7}' + chunk_IPv6 + r'$')

        if patten_IPv4.match(IP):
            return "IPv4"
        return "IPv6" if patten_IPv6.match(IP) else "Neither"
        
# @lc code=end

