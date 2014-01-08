# coding:utf-8

# try..except 处理异常.



import sys



try:
    s = input('请输入一些内容 （Ctrl-Z 测试异常的处理）--> ');
except EOFError:
    print ('系统捕获到了 EOFError ！');
    sys.exit(); # exit the program
except:
    print ('\nSome error/exception occurred.');
    # here, we are not exiting the program

print ('执行完毕！');