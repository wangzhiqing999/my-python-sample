# coding:utf-8

# __str__方法.



# 使用class语句后跟类名，创建了一个新的类。
class Person:
    # __init__方法在类的一个对象被建立时，马上运行。
    # 这个方法可以用来对你的对象做一些你希望的 初始化 。
    # 注意，这个名称的开始和结尾都是双下划线。
    # 这个方法，从功能上面来说， 相当于 C# 当中的 构造函数.
    def __init__(self, name, age):
        # 注意：由于 Python 中， 没有定义变量这样的处理.
        # 因此，需要使用类里面的成员变量的时候， 就直接  self.变量名  来进行处理了.
        self.name = name
        self.age = age

    # 定义对象打印时的输出格式
    def __str__(self):
        return f"姓名：{self.name}，年龄：{self.age}"

    # 定义加法操作的行为
    def __add__(self, other):
        # 注意： 加法操作， 相当于 C# 的 重载 + 运算符.
        return Person(self.name + other.name, self.age + other.age)

    # 定义比较的方法.
    def __eq__(self, other):
        # 检查 other 是否为 Person 类的实例.
        if isinstance(other, Person):
            # 比较两个实例的 name 与 age 属性
            return self.name == other.name and self.age == other.age
        return False



# 构造新的对象. 传入一个初始化的参数.
p3 = Person('张三', 18)
p4 = Person('李四', 20)
p33 = Person('张三', 18)

# 调用对象的方法.
print(p3)
print(p4)

print(p3+p4)

print(p3 == p4)
print(p3 == p33)