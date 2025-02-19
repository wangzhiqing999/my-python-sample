# coding:utf-8

# 类与对象的变量.



# 使用class语句后跟类名，创建了一个新的类。
class Person:
    """员工测试类."""

    # population属于Person类，是一个类的变量。
    # 在类里面， 没有写 self. 开头的变量.
    # 这个可以理解为 C# 里面的 一个类的 静态变量.
    population = 0

    # __init__方法在类的一个对象被建立时，马上运行。
    def __init__(self, name):
        """初始化员工的数据."""
        # 设置姓名.
        self.name = name
        print ('(初始化 %s ...)' % self.name)

        # 注意： 这里没有写 self.变量名， 而是写 Person.变量名
        Person.population += 1

    # __del__在对象消逝的时候被调用。对象消逝即对象不再被使用，它所占用的内存将返回给系统作它用。
    def __del__(self):
        """释放对象的相关资源."""
        print ('%s 的资源被释放...' % self.name)

        # 注意： 这里没有写 self.变量名， 而是写 Person.变量名
        Person.population -= 1

        if Person.population == 0:
            print ('我是最后一个被释放的了，我被释放以后，这里就没人了。')
        else:
            print ('我被释放以后，还有 %d 个人在这里.' % Person.population)

    # 类里面定义的方法.
    def sayHi(self):
        """Greeting by the person.

        Really, that's all it does."""
        print ('您好，我叫 %s.' % self.name)

    @staticmethod
    def howMany():
        """Prints the current population."""
        if Person.population == 1:
            print ('只有我一个人在这里！')
        else:
            print ('现在有 %d 个人在这里.' % Person.population)



zhang3 = Person('张三')
zhang3.sayHi()
zhang3.howMany()

li4 = Person('李四')
li4.sayHi()
li4.howMany()

zhang3.sayHi()
zhang3.howMany()

del li4
del zhang3

print ("处理结束！")
