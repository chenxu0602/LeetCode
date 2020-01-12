#
# @lc app=leetcode id=1138 lang=python3
#
# [1138] Alphabet Board Path
#
# https://leetcode.com/problems/alphabet-board-path/description/
#
# algorithms
# Medium (42.56%)
# Likes:    67
# Dislikes: 40
# Total Accepted:    7.1K
# Total Submissions: 16.1K
# Testcase Example:  '"leet"'
#
# On an alphabet board, we start at position (0, 0), corresponding to character
# board[0][0].
# 
# Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in
# the diagram below.
# 
# 
# 
# We may make the following moves:
# 
# 
# 'U' moves our position up one row, if the position exists on the board;
# 'D' moves our position down one row, if the position exists on the board;
# 'L' moves our position left one column, if the position exists on the
# board;
# 'R' moves our position right one column, if the position exists on the
# board;
# '!' adds the character board[r][c] at our current position (r, c) to the
# answer.
# 
# 
# (Here, the only positions that exist on the board are positions with letters
# on them.)
# 
# Return a sequence of moves that makes our answer equal to target in the
# minimum number of moves.  You may return any path that does so.
# 
# 
# Example 1:
# Input: target = "leet"
# Output: "DDR!UURRR!!DDD!"
# Example 2:
# Input: target = "code"
# Output: "RR!DDRR!UUL!R!"
# 
# 
# Constraints:
# 
# 
# 1 <= target.length <= 100
# target consists only of English lowercase letters.
# 
#

# @lc code=start
import string 

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        d = {c: divmod(i, 5) for i, c in enumerate(string.ascii_lowercase)}
        prev = d['a']
        res = ""

        for x in target:
            subtract = [d[x][0] - prev[0], d[x][1] - prev[1]]
            prev = d[x]

            if subtract[1] < 0: res += 'L'*abs(subtract[1])
            if subtract[0] < 0: res += 'U'*abs(subtract[0])
            if subtract[0] > 0: res += 'D'*subtract[0]
            if subtract[1] > 0: res += 'R'*subtract[1]

            res += '!'
        
        return res
        
# @lc code=end

