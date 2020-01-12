#
# @lc app=leetcode id=393 lang=python3
#
# [393] UTF-8 Validation
#
# https://leetcode.com/problems/utf-8-validation/description/
#
# algorithms
# Medium (35.91%)
# Likes:    143
# Dislikes: 675
# Total Accepted:    36.1K
# Total Submissions: 100.4K
# Testcase Example:  '[197,130,1]'
#
# A character in UTF8 can be from 1 to 4 bytes long, subjected to the following
# rules:
# 
# For 1-byte character, the first bit is a 0, followed by its unicode code.
# For n-bytes character, the first n-bits are all one's, the n+1 bit is 0,
# followed by n-1 bytes with most significant 2 bits being 10.
# 
# This is how the UTF-8 encoding would work:
# 
# ⁠  Char. number range  |        UTF-8 octet sequence
# ⁠     (hexadecimal)    |              (binary)
# ⁠  --------------------+---------------------------------------------
# ⁠  0000 0000-0000 007F | 0xxxxxxx
# ⁠  0000 0080-0000 07FF | 110xxxxx 10xxxxxx
# ⁠  0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
# ⁠  0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
# 
# 
# Given an array of integers representing the data, return whether it is a
# valid utf-8 encoding.
# 
# 
# Note:
# The input is an array of integers. Only the least significant 8 bits of each
# integer is used to store the data. This means each integer represents only 1
# byte of data.
# 
# 
# 
# Example 1:
# 
# data = [197, 130, 1], which represents the octet sequence: 11000101 10000010
# 00000001.
# 
# Return true.
# It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte
# character.
# 
# 
# 
# 
# Example 2:
# 
# data = [235, 140, 4], which represented the octet sequence: 11101011 10001100
# 00000100.
# 
# Return false.
# The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes
# character.
# The next byte is a continuation byte which starts with 10 and that's correct.
# But the second continuation byte does not start with 10, so it is invalid.
# 
# 
#
class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        """
        if not data:
            return False

        i, n = 0, len(data)
        arr = [bin(x)[2:].rjust(8, '0') for x in data]
        while i < n:
            cnt = len(arr[i]) - len(arr[i].lstrip('1'))
            if cnt == 0:
                i += 1
            elif 2 <= cnt <= 4:
                while i + 1 < n and arr[i+1].startswith('10') and cnt > 1:
                    i += 1
                    cnt -= 1
                if not cnt == 1:
                    return False
                i += 1
            else:
                return False

        return True
        """

        """
        n_bytes = 0

        for num in data:

            bin_rep = format(num, '#010b')[-8:]

            if n_bytes == 0:

                for bit in bin_rep:
                    if bit == '0': break
                    n_bytes += 1

                if n_bytes == 0:
                    continue

                if n_bytes == 1 or n_bytes > 4:
                    return False

            else:
                if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                    return False

            n_bytes -= 1

        return n_bytes == 0
        """

        n_bytes = 0

        mask1 = 1 << 7
        mask2 = 1 << 6

        for num in data:
            mask = 1 << 7
            if n_bytes == 0:
                while mask & num:
                    n_bytes += 1
                    mask = mask >> 1

                if n_bytes == 0:
                    continue

                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:
                if not (num & mask1 and not (num & mask2)):
                    return False
            n_bytes -= 1
        return n_bytes == 0


        





