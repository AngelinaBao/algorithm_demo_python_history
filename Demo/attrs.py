class MyObject(object):
    def __init__(self):
        self.x = 9

def power(self):
    return self.x * self.x
obj = MyObject()

print(hasattr(obj, 'x')) # 有属性'x'吗？
print(obj.x)
setattr(obj, 'y', 19)
print(getattr(obj, 'y'))   # getattr(obj, 'y) = object.y
