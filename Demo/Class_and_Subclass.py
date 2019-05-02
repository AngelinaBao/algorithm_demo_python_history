class Animal(object):
    def run(self):
        print('Animal is runing...')

class Dog(Animal):
    def run(self):
        print('Dog is runing...')

class Cat(Animal):
    def run(self):
        print('Cat is runing...')

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

# add a new class under Animal class
class Pig(Animal):
    def run(self):
        print('Pig is runing...')
run_twice(Pig())

# 继承性
class Smart_pig(Pig):
    def run(self):
        print('Smart_pig is runing...')
run_twice(Smart_pig())

smart_pig = Smart_pig()
isinstance(smart_pig, Smart_pig)
isinstance(smart_pig, Pig)
isinstance(smart_pig, Animal)

# 鸭子类型
# 不要求传入的参数一定是Animal类，只需要含有run（）方法就可以了
class Timer(object):
    def run(self):
        print('Start runing Timer...')
run_twice(Timer())
