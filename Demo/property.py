class Screen(object):
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError('width must be positive!')
        self.__width = value

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError('height must be positive!')
        self.__height = value

    @property
    def resolution(self):
        return self.__width * self.__height
    
# test:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')