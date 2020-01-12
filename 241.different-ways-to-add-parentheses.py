#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#
import operator 

class Solution:
    def search(self, expr):
        return expr if len(expr) == 1 else sum([[expr[i](p, q) for p in self.search(expr[:i]) for q in self.search(expr[i+1:])] for i in range(1, len(expr), 2)], [])

    def diffWaysToCompute(self, input: str) -> List[int]:

        """
        maps = {'+': operator.add, '-':operator.sub, '*':operator.mul}

        expr, digits, i, genNum = [], [], 0, lambda ds: int(''.join(ds))

        for c in input:
            if c.isdigit():
                digits.append(c)
            else:
                expr, digits = expr + [genNum(digits), maps[c]], []

        expr += [genNum(digits)]                
        return sorted(self.search(expr))
        """

        """
        return [eval(`a`+c+`b`)
                for i, c in enumerate(input) if c in '+-*'
                for a in self.diffWaysToCompute(input[:i])
                for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]
        """

        """
        return [a+b if c == '+' else a-b if c == '-' else a*b
                for i, c in enumerate(input) if c in '+-*'
                for a in self.diffWaysToCompute(input[:i])
                for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]
        """

        if input.isdigit():
            return [int(input)]

        res = []

        for i, c in enumerate(input):
            if c in '+-*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for j in left:
                    for k in right:
                        if c == '+':
                            res.append(j+k)
                        elif c == '-':
                            res.append(j-k)
                        elif c == '*':
                            res.append(j*k)

        return res



