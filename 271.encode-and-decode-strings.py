#
# @lc app=leetcode id=271 lang=python3
#
# [271] Encode and Decode Strings
#
# https://leetcode.com/problems/encode-and-decode-strings/description/
#
# algorithms
# Medium (31.38%)
# Likes:    443
# Dislikes: 152
# Total Accepted:    59.6K
# Total Submissions: 189.4K
# Testcase Example:  '["Hello","World"]'
#
# Design an algorithm to encode a list of strings to a string. The encoded
# string is then sent over the network and is decoded back to the original list
# of strings.
# 
# Machine 1 (sender) has the function:
# 
# 
# string encode(vector<string> strs) {
# ⁠ // ... your code
# ⁠ return encoded_string;
# }
# Machine 2 (receiver) has the function:
# 
# 
# vector<string> decode(string s) {
# ⁠ //... your code
# ⁠ return strs;
# }
# 
# 
# So Machine 1 does:
# 
# 
# string encoded_string = encode(strs);
# 
# 
# and Machine 2 does:
# 
# 
# vector<string> strs2 = decode(encoded_string);
# 
# 
# strs2 in Machine 2 should be the same as strs in Machine 1.
# 
# Implement the encode and decode methods.
# 
# 
# 
# Note:
# 
# 
# The string may contain any possible characters out of 256 valid ascii
# characters. Your algorithm should be generalized enough to work on any
# possible characters.
# Do not use class member/global/static variables to store states. Your encode
# and decode algorithms should be stateless.
# Do not rely on any library method such as eval or serialize methods. You
# should implement your own encode/decode algorithm.
# 
# 
#

# @lc code=start
class Codec:
    def len_to_str(self, x):
        """
        Encodes length of string to bytes string
        """
        x = len(x)
        bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
        bytes.reverse()
        bytes_str = ''.join(bytes)
        return bytes_str

    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return "".join(self.len_to_str(x) + x for x in strs)
        
    def str_to_int(self, bytes_str):
        """
        Decodes bytes string to integer.
        """
        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        i, n = 0, len(s)
        output = []
        while i < n:
            length = self.str_to_int(s[i:i + 4])
            i += 4
            output.append(s[i:i + length])
            i += length
        return output
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
# @lc code=end

