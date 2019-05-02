def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    else:
        m= L[0]
        n = L[0]
        for i in L:
            if i <= n:
                n = i
            if i >= m:
                m = i
        return (n, m)
   
print(findMinAndMax([1, 3, 4, -1]))



 
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')