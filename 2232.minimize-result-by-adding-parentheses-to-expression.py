#
# @lc app=leetcode id=2232 lang=python3
#
# [2232] Minimize Result by Adding Parentheses to Expression
#

# @lc code=start
class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus_idx, n, ans = expression.find('+'), len(expression), [float("inf"), expression]

        def evaluate(exps: str):
            return eval(exps.replace('(', '*(').replace(')', ')*').lstrip('*').rstrip('*'))

        for l in range(plus_idx):
            for r in range(plus_idx + 1, n):
                exps = f"{expression[:l]}({expression[l:plus_idx]}+{expression[plus_idx + 1:r + 1]}){expression[r + 1:n]}"
                res = evaluate(exps)

                if ans[0] > res:
                    ans[0], ans[1] = res, exps

        return ans[1]
        
# @lc code=end

