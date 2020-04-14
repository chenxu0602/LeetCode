#!/usr/bin/python
# coding=utf-8
################################################################################
'''
给你一个字符串数组，代表不同的路径，比如：
[/ab/cd/efg, /ab/cd, /df, /gh]
[/, /ab, /cd, /gh]

要求：
删掉那些冗余的子路径，比如 /ab/cd/efg 是 /ab/cd 的子路径（也就是说在这个目录下），
所以就需要被删除。
注意: '/' 是根路径，是所有路径的父路径

做法：
因为我挂了，所以我也不知道我的做法对不对。我是用prefix tree做的。和普通的前缀树不同的是，
这里树的点不是存字母，是存directory名，接下来就进行正常操作就好了。
'''
################################################################################
'''
我想应该是用hashset来做更简单。
1）把输入的所有路径放到hashset里；
2）逐次读入每个路径，然后split by'/'，查找是否有父路径已经存在于hashset里，如果没有，就把此路径添加到结果列表中；
3）重复步骤2，直到所有路径都检查过；
时间复杂度应该是O(N*M)，N是路径数，M是路径深度；空间复杂度应该O(N)。
python3 的代码（我没有调试过）：
def removeDup(dirs: List[str]) -> List[str]:
    dirs = set(dirs)
    if '/' in dirs:
        return ['/']
 
    ans = []
    for dir in dirs:
        l = len(dir)
        parentExist = False
        while l >= 0:
            i = dir.rfind('/', 0, l)
            if dir[:i] in dirs:
                parentExist = True
                break
            l = i
        if not parentExist:
            ans.append(dir)
 
    return ans
'''

class Solution(object):
    def removd_duplicate(self, dirs):

        dirs = set(dirs)
        if '/' in dirs:
            return '/'

        res = []
        for item in dirs:
            item = item.split('/')
            current = '/'

            flag_duplicate = False
            for i in range(1, len(item) - 1):
                current += item[i]
                if current in dirs:
                    flag_duplicate = True
                    break
                current += '/'

            if not flag_duplicate:
                res.append('/'.join(item))
        return res

a = Solution()
a.removd_duplicate(['/ab/cd', '/ab/cd', '/df', '/gh'])
a.removd_duplicate(['/ab/cd/efg', '/ab/cd', '/df', '/gh'])
a.removd_duplicate(['/', '/ab', '/cd', '/gh'])



