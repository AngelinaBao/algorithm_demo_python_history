# import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s' %func.__name__) #打印函数名字
#         return func(*args, **kw) #调用原始函数
#     return wrapper

# @log
# def sum2(x, y):
#     print(x, '+', y, '=', x + y)
# sum2(1, 3)

# having arguments in log
# import functools
# def log(text):
#     def decorator(func):
#         @functools.wraps(func) # 需要把原始函数的__name__等属性复制到wrapper()函数中
#         def wrapper(*args, **kw):
#             print('%s %s' %(text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator

# @log('excute')
# def multi(x, y):
#     print(x, '*', y, '=', x * y)   # equals: log('excute')(multi)
   
# multi(3, 4.5)


#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time, functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start = time.time()
        func(*args, **kw)
        execte_time = time.time() - start
        print("%s executed in %s ms" %(func.__name__, execte_time * 1000))
        return func(*args, **kw)
    return wrapper

@log
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@log
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


## remained question:
# if there is a method to realized 'both no args & having args' log?
