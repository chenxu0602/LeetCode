#!/usr/bin/python
# coding=utf-8
################################################################################
'''
模拟fb好友推荐。给一个function，可以return某一个id的所有好友。需要完成一个function
就是input 一个id，output list of friends of friends, ordered by number of mutual
 friends.

ANS: 大概就是新建一个class，有id和number of mutual friends field,
然后override hash function(保证不用重新计算已经算过mutual friends的id)。
在immediate friends list里面iterate，然后把每一个朋友的朋友和他们的mutual friend number
加入list。最后写一个comparator，用collection.sort 按照mutual friends排序就好。
当时没有那么多时间，可能有更好的解法~
'''
################################################################################
from collections import defaultdict
class Friends(object):
    #graph is {key=ID, value=set_of_friends}
    def find_friends_of_friends(self, ID, graph):
        count = defaultdict(int)

        for friend in graph[ID]:

            for friend_of_friend in graph[friend]:
                if friend_of_friend == ID:
                    continue
                if friend_of_friend in graph[ID]:
                    count[friend_of_friend] += 1

        res = [(key, value) for (key, value) in count.iteritems()]
        return sorted(res, key=lambda x: x[1])



    def find_friend(self, ID):
        pass
        return []
