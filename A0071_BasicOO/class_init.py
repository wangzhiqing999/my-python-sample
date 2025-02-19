# coding:utf-8

# __init__方法.



# 使用class语句后跟类名，创建了一个新的类。
class Person:
    # __init__方法在类的一个对象被建立时，马上运行。
    # 这个方法可以用来对你的对象做一些你希望的 初始化 。
    # 注意，这个名称的开始和结尾都是双下划线。
    # 这个方法，从功能上面来说， 相当于 C# 当中的 构造函数.
    def __init__(self, name):
        # 注意：由于 Python 中， 没有定义变量这样的处理.
        # 因此，需要使用类里面的成员变量的时候， 就直接  self.变量名  来进行处理了.
        self.name = name
    # 类里面定义一个方法.
    def sayHi(self):
        print ('Hello, my name is', self.name)



# 构造新的对象. 传入一个初始化的参数.
p3 = Person('张三')
p4 = Person('李四')

# 调用对象的方法.
p3.sayHi()
p4.sayHi()
