﻿# coding:utf-8

# exec和eval语句




# exec语句用来执行储存在字符串或文件中的Python语句。
exec("print('Hello World')");



# eval语句用来计算存储在字符串中的有效Python表达式。
c = "1+2+3+4";
print(c, "=", eval(c));