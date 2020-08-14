#
# @lc app=leetcode id=353 lang=python3
#
# [353] Design Snake Game
#
# https://leetcode.com/problems/design-snake-game/description/
#
# algorithms
# Medium (32.75%)
# Likes:    313
# Dislikes: 129
# Total Accepted:    28.9K
# Total Submissions: 88.2K
# Testcase Example:  '["SnakeGame","move","move","move","move","move","move"]\n' + '[[3,2,[[1,2],[0,1]]],["R"],["D"],["R"],["U"],["L"],["U"]]'
#
# Design a Snake game that is played on a device with screen size = width x
# height. Play the game online if you are not familiar with the game.
# 
# The snake is initially positioned at the top left corner (0,0) with length =
# 1 unit.
# 
# You are given a list of food's positions in row-column order. When a snake
# eats the food, its length and the game's score both increase by 1.
# 
# Each food appears one by one on the screen. For example, the second food will
# not appear until the first food was eaten by the snake.
# 
# When a food does appear on the screen, it is guaranteed that it will not
# appear on a block occupied by the snake.
# 
# Example:
# 
# 
# Given width = 3, height = 2, and food = [[1,2],[0,1]].
# 
# Snake snake = new Snake(width, height, food);
# 
# Initially the snake appears at position (0,0) and the food at (1,2).
# 
# |S| | |
# | | |F|
# 
# snake.move("R"); -> Returns 0
# 
# | |S| |
# | | |F|
# 
# snake.move("D"); -> Returns 0
# 
# | | | |
# | |S|F|
# 
# snake.move("R"); -> Returns 1 (Snake eats the first food and right after
# that, the second food appears at (0,1) )
# 
# | |F| |
# | |S|S|
# 
# snake.move("U"); -> Returns 1
# 
# | |F|S|
# | | |S|
# 
# snake.move("L"); -> Returns 2 (Snake eats the second food)
# 
# | |S|S|
# | | |S|
# 
# snake.move("U"); -> Returns -1 (Game over because snake collides with
# border)
# 
# 
#

# @lc code=start
from collections import OrderedDict, deque

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.food = [complex(*z) for z in food[::-1]]
        self.snake = OrderedDict([(0, True)])
        self.score = 0
        self.width = width
        self.height = height
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        head = next(reversed(self.snake)) + 1j ** 'DRU'.find(direction)

        if head in self.food[-1:]:
            self.food.pop()
            self.score += 1
        else:
            self.snake.popitem(False)

        if head in self.snake or not (0 <= head.imag < self.width and 0 <= head.real < self.height):
            return -1

        self.snake[head] = True
        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
# @lc code=end

