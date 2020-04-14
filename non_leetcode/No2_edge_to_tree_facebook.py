#!/usr/bin/python
# coding=utf-8
################################################################################
'''
3.把edges转化成tree，每个edge第一个point是第二个point的parent。

输入是
{{'a','b'}, {'a','d'}, {'b','c'}}
比如第一个：a是b的parent

最终转化成tree
      a
   b     d
  c
'''
################################################################################
'''
ANS:  对，先找到root，然后hashmap存，然后dfs/bfs

(1)find root by set.
set1: all_node
set2: father
(2)save edges into graph
(3)BFS/DFS: convert graph into tree.
'''

