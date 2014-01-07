# coding:utf-8

# 自己的模块.


# Filename: mymodule_demo2.py

# 如果你想要直接输入argv变量到你的程序中（避免在每次使用它时打sys.），那么你可以使用from sys import argv语句。
# 如果你想要输入所有sys模块使用的名字，那么你可以使用from sys import *语句。
# 这对于所有模块都适用。
# 一般说来，应该避免使用from..import而使用import语句，因为这样可以使你的程序更加易读，也可以避免名称的冲突。

from mymodule import sayhi, version


# 输出函数的 文档信息.
print (sayhi.__doc__);

# 调用模块的函数.
sayhi();

# 输出模块版本.
print ('模块的版本：', version);


# End of mymodule_demo2.py

