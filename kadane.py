
def Kadane(arr, res=0, cur=0):
    for num in arr:
        cur = max(cur+num, num)
        res = max(res, cur)
    return res
