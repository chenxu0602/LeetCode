#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#
# https://leetcode.com/problems/valid-number/description/
#
# algorithms
# Hard (15.25%)
# Likes:    746
# Dislikes: 4862
# Total Accepted:    172.1K
# Total Submissions: 1.1M
# Testcase Example:  '"0"'
#
# Validate if a given string can be interpreted as a decimal number.
# 
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3   " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false
# 
# Note: It is intended for the problem statement to be ambiguous. You should
# gather all requirements up front before implementing one. However, here is a
# list of characters that can be in a valid decimal number:
# 
# 
# Numbers 0-9
# Exponent - "e"
# Positive/negative sign - "+"/"-"
# Decimal point - "."
# 
# 
# Of course, the context of these characters also matters in the input.
# 
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your
# function signature accepts a const char * argument, please click the reload
# button to reset your code definition.
# 
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:

        s = s.strip()
        if not s: return False
        met_dot = met_e = met_digit = False

        for i, char in enumerate(s):
            if char in ('+', '-'):
                if i > 0 and s[i-1] != 'e':
                    return False
            elif char == '.':
                if met_dot or met_e:
                    return False
                met_dot = True
            elif char == 'e':
                if met_e or not met_digit:
                    return False
                met_e, met_digit = True, False
            elif char.isdigit():
                met_digit = True
            else:
                return False

        return met_digit
        
# @lc code=end

