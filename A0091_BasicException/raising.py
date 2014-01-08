# coding:utf-8

# 使用raise语句 引发 异常.



import sys



# 下面这个类， 继承了 Exception 类.
class ShortInputException(Exception):
    '''用户自定义异常类！'''
    def __init__(self, length, atleast):
        Exception.__init__(self);
        self.length = length;
        self.atleast = atleast;


try:
    s = input('请输入一些内容 （Ctrl-Z 测试异常的处理）--> ');
    if len(s) < 3:
        raise ShortInputException(len(s), 3);
except EOFError:
    print ('系统捕获到了 EOFError ！');
    sys.exit(); # exit the program
except ShortInputException as x:
    print ('ShortInputException: 输入文字的长度 %d, \
          至少应该输入的长度 %d' % (x.length, x.atleast));
else:
    print ('程序正常执行，未发生异常！');

