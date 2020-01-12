#
# @lc app=leetcode id=353 lang=python3
#
# [353] Design Snake Game
#
# https://leetcode.com/problems/design-snake-game/description/
#
# algorithms
# Medium (30.51%)
# Likes:    214
# Dislikes: 80
# Total Accepted:    21.2K
# Total Submissions: 69.1K
# Testcase Example:  '["SnakeGame","move","move","move","move","move","move"]\n' +
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
# snake.move("U"); -> Returns -1 (Game over because snake collides with border)
# 
#

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
        """

        self.foodIndex = 0
        self.snake = deque()
        self.snake.append((0, 0))
        self.body = {(0, 0)}
        self.foods = food
        self.width = width
        self.height = height
        self.moves = {'U': (0, -1), 'L': (-1, 0), 'R': (1, 0), 'D': (0, 1)}
        """
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """

        head = next(reversed(self.snake)) + 1j ** 'DRU'.find(direction) # 'DRU'.find('L') = -1

        if head in self.food[-1:]:
            self.food.pop()
            self.score += 1
        else:
            self.snake.popitem(False)

        if head in self.snake or not (0 <= head.imag < self.width and 0 <= head.real < self.height):
            return -1

        self.snake[head] = True
        return self.score
        """

        tail = self.snake.popleft()
        self.body.remove(tail)

        if not self.snake:
            head = tail
        else:
            head = self.snake[-1]

        xm, ym = self.moves[direction]
        nx, ny = head[0] + xm, head[1] + ym

        if (nx, ny) in self.body or nx < 0 or nx >= self.width or ny < 0 or ny >= self.height:
            return -1

        self.snake.append((nx, ny))
        self.body.add((nx, ny))

        if self.foodIndex < len(self.foods) and nx == self.foods[self.foodIndex][1] and ny == self.foods[self.foodIndex][0]:
            self.foodIndex += 1
            self.snake.appendleft(tail)
            self.body.add(tail)

        return len(self.snake) - 1
        """
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

