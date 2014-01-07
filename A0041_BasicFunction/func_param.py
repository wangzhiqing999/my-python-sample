# coding:utf-8

# 函数形参.


# 函数通过def关键字定义。
# def关键字后跟一个函数的 标识符 名称，然后跟一对圆括号。
# 圆括号之中可以包括一些变量名，该行以冒号结尾。
# 接下来是一块语句，它们是函数体。
def printMax(a, b):
    # 从这里开始，就是函数体了.
    if a > b:
        print (a, 'is maximum!');
    else:
        print (b, 'is maximum!');

        
# 直接调用函数(数值).
printMax(3, 4);


# 定义变量，然后调用 函数(变量名)
x = 5;
y = 7;
printMax(x, y);
