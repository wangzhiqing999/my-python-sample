﻿# coding:utf-8

# 默认参数值.


# 函数通过def关键字定义。
# def关键字后跟一个函数的 标识符 名称，然后跟一对圆括号。
# 圆括号之中可以包括一些变量名，该行以冒号结尾。
# 接下来是一块语句，它们是函数体。


# 对于一些函数，你可能希望它的一些参数是 可选 的，如果用户不想要为这些参数提供值的话，这些参数就使用默认值。
# 这个功能借助于默认参数值完成。
# 你可以在函数定义的形参名后加上赋值运算符（=）和默认值，从而给形参指定默认参数值。
# 注意，默认参数值应该是一个参数。更加准确的说，默认参数值应该是不可变的
def say(message, times = 1):
    print (message * times);

# 重要
# 只有在形参表末尾的那些参数可以有默认参数值，即你不能在声明函数形参的时候，先声明有默认值的形参而后声明没有默认值的形参。
# 这是因为赋给形参的值是根据位置而赋值的。例如，def func(a, b=5)是有效的，但是def func(a=5, b)是 无效 的。






# 调用函数， 第2个参数使用默认值.
say('Hello');

# 调用函数， 第2个参数自己指定.
say('World', 5);