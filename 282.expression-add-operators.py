#
# @lc app=leetcode id=282 lang=python3
#
# [282] Expression Add Operators
#
# https://leetcode.com/problems/expression-add-operators/description/
#
# algorithms
# Hard (32.81%)
# Likes:    690
# Dislikes: 95
# Total Accepted:    69K
# Total Submissions: 210.5K
# Testcase Example:  '"123"\n6'
#
# Given a string that contains only digits 0-9 and a target value, return all
# possibilities to add binary operators (not unary) +, -, or * between the
# digits so they evaluate to the target value.
# 
# Example 1:
# 
# 
# Input: num = "123", target = 6
# Output: ["1+2+3", "1*2*3"] 
# 
# 
# Example 2:
# 
# 
# Input: num = "232", target = 8
# Output: ["2*3+2", "2+3*2"]
# 
# Example 3:
# 
# 
# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"]
# 
# Example 4:
# 
# 
# Input: num = "00", target = 0
# Output: ["0+0", "0-0", "0*0"]
# 
# 
# Example 5:
# 
# 
# Input: num = "3456237490", target = 9191
# Output: []
# 
# 
#
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        """
        def recurse(index, prev_operand, current_operand, value, string):
            if index == N:
                if value == target and current_operand == 0:
                    answers.append("".join(string[1:]))
                return

            current_operand = current_operand * 10 + int(num[index])
            str_op = str(current_operand)

            if current_operand > 0:
                recurse(index+1, prev_operand, current_operand, value, string)

            string.append('+'); string.append(str_op)
            recurse(index+1, current_operand, 0, value+current_operand, string)
            string.pop(); string.pop()

            if string:
                string.append('-'); string.append(str_op)
                recurse(index+1, -current_operand, 0, value - current_operand, string)
                string.pop(); string.pop()

                string.append('*'); string.append(str_op)
                recurse(index+1, current_operand*prev_operand, 0, value - prev_operand + (current_operand * prev_operand), string)
                string.pop(); string.pop()

        N = len(num)
        answers = []
        recurse(0, 0, 0, 0, [])
        return answers
        """

        self.res, self.target = [], target
        for i in range(1, len(num)+1):
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), self.res)
        return self.res

    def dfs(self, num, temp, cur, last, res):
        if not num:
            if cur == self.target:
                res.append(temp)
            return
        for i in range(1, len(num)+1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(num[i:], temp+'+'+val, cur+int(val), int(val), res)
                self.dfs(num[i:], temp+'-'+val, cur-int(val), -int(val), res)
                self.dfs(num[i:], temp+'*'+val, cur-last+last*int(val), last*int(val), res)

        
