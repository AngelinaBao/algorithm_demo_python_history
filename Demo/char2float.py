# 利用 map & reduce, 把字符串'123.4567'转化为123.4567
# 把数字分为整数部分和小数部分，分别转化为int后再处理为整数+小数，即浮点数

from functools import reduce
def char2float(s):
    def char2num(s):
        DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        return DIGITS[s]

    L = s.split('.')
    dot = len(L[1])
    L[0] = map(char2num, L[0])
    L[1] = map(char2num, L[1])

    big = reduce(lambda x, y: x *10 + y, L[0])
    small = reduce(lambda x, y: x * 10 + y, L[1])

    return big + small/(10 ** dot)

# test
print('char2float(\'123.4567\') =', char2float('123.4567'))
if abs(char2float('123.4567') - 123.4567) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
    